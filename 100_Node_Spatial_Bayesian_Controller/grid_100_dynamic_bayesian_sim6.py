"""
-------------------------------------------------------------------------------
TITLE: 
    Spatial Bayesian Wake-on-Energy: Territorial Coverage Optimisation

SCENARIO: 
    UAV-Aided 'Data Mule' Mission (100-Node Grid).
    
FEATURES:
    - ℓ = 2.5: High spatial correlation for broad territorial confidence.
    - β = 4.0: High exploration weight to eliminate 'white space'.
    - Axes & Grids: Restored for spatial reference (essential for COMSEC/Mission Planning).
-------------------------------------------------------------------------------
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

# Reset for true randomized mission profiles
np.random.seed()

# --------------------------------------------------
# 1. ENVIRONMENT: DYNAMIC SHADING (CLOUDS)
# --------------------------------------------------
GRID_DIM = 10
coords = np.array([[i % GRID_DIM, i // GRID_DIM] for i in range(100)])

num_clouds = np.random.randint(1, 4)
clouds = [
    {'center': np.random.uniform(2, 8, 2), 'radius': np.random.uniform(1.8, 3.2)} 
    for _ in range(num_clouds)
]

def get_node_status(x, y):
    for cloud in clouds:
        dist = np.sqrt((x - cloud['center'][0])**2 + (y - cloud['center'][1])**2)
        if dist < cloud['radius']:
            return -0.5
    return 1.0

true_states = np.array([get_node_status(c[0], c[1]) for c in coords])

# --------------------------------------------------
# 2. GP CONTROLLER CONFIGURATION
# --------------------------------------------------
kernel = C(1.0) * RBF(length_scale=2.5) 

gp = GaussianProcessRegressor(
    kernel=kernel, 
    alpha=0.05,
    normalize_y=True,
    optimizer=None
)

polled_indices = []
observations = []
exploration_weight = 4.0 

# --------------------------------------------------
# 3. MISSION SIMULATION
# --------------------------------------------------
fig, axes = plt.subplots(3, 3, figsize=(15, 13))
axes = axes.flatten()

print(f"COMMENCING MISSION: Mapping {num_clouds} Shading Obstacles...")

for t in range(9):
    if t > 0:
        gp.fit(coords[polled_indices], np.array(observations))
    
    y_pred, sigma = gp.predict(coords, return_std=True)

    # ACQUISITION
    if t < 2:
        remaining = list(set(range(100)) - set(polled_indices))
        next_node = np.random.choice(remaining)
    else:
        acquisition_score = y_pred + exploration_weight * sigma
        acquisition_score[polled_indices] = -999
        next_node = np.random.choice(np.where(acquisition_score == np.max(acquisition_score))[0])

    polled_indices.append(next_node)
    result = true_states[next_node]
    observations.append(result)

    # --- VISUALISATION ---
    ax = axes[t]
    belief_map = y_pred.reshape(GRID_DIM, GRID_DIM)
    
    # Render Belief
    im = ax.imshow(belief_map, cmap='RdYlGn', origin='lower', vmin=-0.6, vmax=0.6, extent=[-0.5, 9.5, -0.5, 9.5])
    
    # Overlay Ground Truth Clouds
    for cloud in clouds:
        circle = plt.Circle(cloud['center'], cloud['radius'], color='gray', alpha=0.15, linestyle='--')
        ax.add_patch(circle)

    # Mark Samples
    for i, idx in enumerate(polled_indices):
        dot_color = "black" if observations[i] == 1.0 else "white"
        ax.scatter(coords[idx, 0], coords[idx, 1], c=dot_color, edgecolors="blue", s=70, zorder=10)

    # Titles, Labels, and Grid
    status_text = 'HARVEST' if result==1 else 'SHADE'
    ax.set_title(f"t={t} | Node {next_node} ({status_text})", fontsize=10, fontweight='bold')
    
    ax.set_xticks(range(10))
    ax.set_yticks(range(10))
    ax.set_xticklabels(range(10), fontsize=7)
    ax.set_yticklabels(range(10), fontsize=7)
    ax.grid(True, which='both', color='black', linestyle='-', linewidth=0.1, alpha=0.3)

# Add a colourbar to explain the probability/energy field
cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])
fig.colorbar(im, cax=cbar_ax, label='Inferred Energy Probability')

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.08, right=0.90, hspace=0.3, wspace=0.3)
fig.suptitle(f"Wake-on-Energy: Bayesian Territorial Mapping (Surgical Extraction)", fontsize=20, y=0.98)

plt.show()
