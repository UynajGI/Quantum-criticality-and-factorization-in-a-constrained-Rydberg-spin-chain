# Processed Data

This directory contains processed and analyzed data ready for plotting and further analysis.

## Data Files

### Phase Diagram

- **`phase_diagram.csv`**: Critical points and phase boundaries
  - Columns:
    - `g_c`: Critical coupling values
    - `phase_left`: Phase label on the left side
    - `phase_right`: Phase label on the right side
    - `transition_type`: Type of phase transition (first-order, second-order, crossover)

### Finite-Size Scaling

- **`fss_data.npz`**: Data collapsed using finite-size scaling
  - Keys:
    - `L`: System sizes
    - `g_scaled`: Scaled coupling parameter (g - g_c) * L^(1/ν)
    - `order_param_scaled`: Scaled order parameter
    - `susceptibility_scaled`: Scaled susceptibility
    - `nu`: Correlation length exponent
    - `beta`: Order parameter exponent
    - `gamma`: Susceptibility exponent

### Critical Exponents

- **`critical_exponents.json`**: Extracted critical exponents with uncertainties
  - Structure:
    ```json
    {
      "transition_1": {
        "g_c": [value, uncertainty],
        "nu": [value, uncertainty],
        "beta": [value, uncertainty],
        "gamma": [value, uncertainty],
        "delta": [value, uncertainty]
      }
    }
    ```

### Factorization Points

- **`factorization.csv`**: Factorization transition data
  - Columns:
    - `L`: System size
    - `g_f`: Factorization point
    - `concurrence`: Entanglement concurrence
    - `Q_measure`: Quantum discord

### Scaling Functions

- **`scaling_functions.npz`**: Universal scaling functions
  - Keys:
    - `x`: Scaled variable
    - `f_order`: Scaling function for order parameter
    - `f_susceptibility`: Scaling function for susceptibility
    - `f_entropy`: Scaling function for entanglement entropy

## Analysis Methods

### Finite-Size Scaling

Critical exponents were extracted by collapsing data from different system sizes:
- **Correlation length exponent (ν)**: From scaling of the correlation length
- **Order parameter exponent (β)**: From scaling of the order parameter
- **Susceptibility exponent (γ)**: From scaling of the susceptibility peak

### Error Estimation

Uncertainties were estimated using:
- Jackknife resampling for statistical errors
- Systematic errors from extrapolation fits
- Combined quadratically for total uncertainty

## Usage Examples

### Load phase diagram

```python
import pandas as pd

phase_data = pd.read_csv('phase_diagram.csv')
print(phase_data)
```

### Load critical exponents

```python
import json

with open('critical_exponents.json', 'r') as f:
    exponents = json.load(f)
    
nu_value, nu_error = exponents['transition_1']['nu']
print(f"ν = {nu_value} ± {nu_error}")
```

### Load finite-size scaling data

```python
import numpy as np

fss = np.load('fss_data.npz')
g_scaled = fss['g_scaled']
order_scaled = fss['order_param_scaled']

# Plot collapsed data
import matplotlib.pyplot as plt
plt.plot(g_scaled, order_scaled)
plt.xlabel('$(g - g_c) L^{1/\\nu}$')
plt.ylabel('Scaled order parameter')
plt.show()
```

## Quality Control

- All scaling collapses were visually inspected
- χ² analysis performed for goodness of fit
- Consistency checks between different observables
- Comparison with analytical predictions where available

## Reproducibility

To reproduce this processed data from raw data:
1. Use scripts in `code/analysis/` directory
2. Run `python code/analysis/extract_critical_exponents.py`
3. Run `python code/analysis/finite_size_scaling.py`

See `code/README.md` for detailed instructions.
