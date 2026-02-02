# Raw Data

This directory contains raw numerical data from quantum many-body simulations of the constrained Rydberg spin chain.

## Data Files

### Ground State Properties

- **`ground_state_energies.npz`**: Ground state energies as a function of system size and parameters
  - Format: NumPy compressed array
  - Keys:
    - `L`: System sizes (array of integers)
    - `g`: Coupling parameter values (array of floats)
    - `E`: Ground state energies (2D array: [g, L])
    - `E_per_site`: Energy per site (2D array: [g, L])

### Order Parameters

- **`order_parameters.npz`**: Various order parameters for phase characterization
  - Format: NumPy compressed array
  - Keys:
    - `L`: System sizes
    - `g`: Coupling parameters
    - `magnetization`: Magnetization in z-direction
    - `staggered_magnetization`: Staggered magnetization
    - `density`: Rydberg density

### Correlation Functions

- **`correlation_functions.npz`**: Two-point correlation functions
  - Format: NumPy compressed array
  - Keys:
    - `L`: System sizes
    - `g`: Coupling parameters
    - `r`: Spatial separations
    - `Czz`: Spin-spin correlations (3D array: [g, L, r])
    - `Cnn`: Density-density correlations (3D array: [g, L, r])

### Entanglement Measures

- **`entanglement.npz`**: Entanglement entropy and related quantities
  - Format: NumPy compressed array
  - Keys:
    - `L`: System sizes
    - `g`: Coupling parameters
    - `S_vN`: von Neumann entropy (2D array: [g, L])
    - `S_renyi`: Rényi entropy (2D array: [g, L])
    - `schmidt_gap`: Schmidt gap (2D array: [g, L])

## Data Collection Parameters

- **System sizes**: L = 8, 12, 16, 20, 24, 28, 32
- **Coupling range**: g ∈ [0.0, 2.0] with Δg = 0.02
- **Constraint**: PXP (Rydberg blockade constraint)
- **Numerical method**: Exact diagonalization (ED) for L ≤ 20, DMRG for L > 20
- **DMRG bond dimension**: χ = 512
- **Energy convergence**: 10⁻¹⁰

## File Format Details

All `.npz` files can be loaded using NumPy:

```python
import numpy as np

# Load data
data = np.load('ground_state_energies.npz')

# Access arrays
system_sizes = data['L']
energies = data['E']
```

## Notes

- All energies are in units of the Rabi frequency Ω
- Distances are measured in lattice sites
- The constraint parameter is implemented via the PXP projector
- For detailed parameter definitions, see the paper

## Data Provenance

- Generated: 2024-XX-XX
- Simulation code: Custom Julia/Python implementation
- Computing resources: [Institution HPC Cluster]
- Total compute time: ~500 CPU hours
