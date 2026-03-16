"""
-------------------------------------------------------------------------------
100-Node Large-Scale Spatial Bayesian Controller
Sequential Search & Information Gathering on a 10x10 Sensor Grid

HARDWARE CONTEXT:
    - 100 ATMega4808 nodes (Indices 0-99)
    - Communication: XBee S2C API Mode
    - Power: Ambient light harvesting (non-uniform distribution)

ALGORITHM LOGIC:
    1. SPATIAL PRIOR: Controller starts with zero knowledge.
    2. GAUSSIAN PROCESS: Uses RBF kernel to model spatial correlation.
    3. ACQUISITION FUNCTION: Upper Confidence Bound (UCB)
       balances exploration and exploitation.
    4. RANDOM SEED POLLS: First two polls are random to break symmetry.

FIDELITY MAPPING:
    SUCCESS (1.0)  = High-Fi sensor data
    FAILURE (-1.0) = Low-Fi environmental inference

GROUND TRUTH:
    Randomised "sunlight hotspot" hidden in the grid.
-------------------------------------------------------------------------------
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

np.random.seed()  # allow true randomness

# --------------------------------------------------
# 1. GRID CONFIGURATION
# --------------------------------------------------

GRID_DIM = 10
NUM_NODES = GRID_DIM * GRID_DIM

node_indices = np.arange(NUM_NODES)

coords = np.array([
    [i % GRID_DIM, i // GRID_DIM] for i in node_indices
])

# --------------------------------------------------
# 2. DYNAMIC ENVIRONMENT (Hidden Sun)
# --------------------------------------------------

sun_x, sun_y = np.random.uniform(2, 8, 2)
sun_radius = 3.0

def get_node_status(x, y):

    dist = np.sqrt((x - sun_x)**2 + (y - sun_y)**2)

    if dist < sun_radius:
        return 1
    else:
        return -1

true_states = np.array([
    get_node_status(c[0], c[1]) for c in coords
])

# --------------------------------------------------
# 3. GAUSSIAN PROCESS CONTROLLER
# --------------------------------------------------

kernel = C(1.0) * RBF(length_scale=2.0)

gp = GaussianProcessRegressor(
    kernel=kernel,
    alpha=0.15,
    optimizer=None
)

polled_indices = []
observations = []

# --------------------------------------------------
# 4. VISUALISATION SETUP
# --------------------------------------------------

fig, axes = plt.subplots(3,3, figsize=(15,15))
axes = axes.flatten()

print(f"Hidden Sun Center: ({sun_x:.2f}, {sun_y:.2f})")

# --------------------------------------------------
# 5. EVOLUTIONARY POLLING LOOP
# --------------------------------------------------

exploration_weight = 1.5

for t in range(9):

    # --------------------------------
    # Node Selection
    # --------------------------------

    if t < 2:
        # Random seed polls
        remaining = list(set(node_indices) - set(polled_indices))
        next_node = np.random.choice(remaining)

    else:

        # GP prediction
        y_pred, sigma = gp.predict(coords, return_std=True)

        acquisition_score = y_pred + exploration_weight * sigma

        # Mask already polled nodes
        acquisition_score[polled_indices] = -999

        # Random tie-breaking
        max_val = np.max(acquisition_score)
        candidates = np.where(acquisition_score == max_val)[0]
        next_node = np.random.choice(candidates)

    # --------------------------------
    # Execute Poll
    # --------------------------------

    polled_indices.append(next_node)

    result = true_states[next_node]
    observations.append(result)

    # --------------------------------
    # Update Bayesian Model
    # --------------------------------

    gp.fit(coords[polled_indices], np.array(observations))

    y_pred, sigma = gp.predict(coords, return_std=True)

    # --------------------------------
    # Visualisation
    # --------------------------------

    ax = axes[t]

    belief_map = y_pred.reshape(GRID_DIM, GRID_DIM)

    im = ax.imshow(
        belief_map,
        cmap='RdYlGn',
        origin='lower',
        vmin=-1,
        vmax=1
    )

    ax.set_title(
        f"t={t} | Node {next_node} "
        f"({'High-Fi' if result==1 else 'Low-Fi'})"
    )

    # draw poll locations
    for i, idx in enumerate(polled_indices):

        dot_color = "black" if observations[i] == 1 else "white"

        ax.scatter(
            coords[idx,0],
            coords[idx,1],
            c=dot_color,
            edgecolors="blue",
            s=80,
            linewidth=1.5
        )

plt.tight_layout()
plt.show()
