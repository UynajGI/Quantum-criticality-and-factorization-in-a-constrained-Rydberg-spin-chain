# Analysis and Visualization Code

This directory contains Python scripts for analyzing the data and reproducing the figures in the paper.

## Directory Structure

```
code/
├── analysis/           # Data analysis scripts
├── visualization/      # Plotting scripts
├── utils/             # Utility functions
└── examples/          # Example notebooks
```

## Requirements

See `../requirements.txt` for Python dependencies.

Core requirements:
- Python ≥ 3.8
- NumPy ≥ 1.20
- SciPy ≥ 1.7
- Matplotlib ≥ 3.4
- pandas ≥ 1.3

Optional:
- Jupyter for running example notebooks
- seaborn for enhanced visualizations

## Analysis Scripts

### `analysis/extract_critical_exponents.py`

Extracts critical exponents from finite-size scaling analysis.

**Usage:**
```bash
python analysis/extract_critical_exponents.py --input ../data/raw_data/ --output ../data/processed_data/
```

**Parameters:**
- `--input`: Path to raw data directory
- `--output`: Path for processed data output
- `--method`: Fitting method ('chi2' or 'mle')
- `--bootstrap`: Number of bootstrap samples for error estimation

### `analysis/finite_size_scaling.py`

Performs finite-size scaling collapse of the data.

**Usage:**
```bash
python analysis/finite_size_scaling.py --data ../data/raw_data/order_parameters.npz
```

### `analysis/phase_diagram.py`

Constructs the phase diagram from raw data.

**Usage:**
```bash
python analysis/phase_diagram.py --output ../data/processed_data/phase_diagram.csv
```

## Visualization Scripts

### `visualization/plot_phase_diagram.py`

Creates the phase diagram figure (Figure 1 in paper).

**Usage:**
```bash
python visualization/plot_phase_diagram.py --output ../figures/phase_diagram.pdf
```

### `visualization/plot_scaling_collapse.py`

Creates finite-size scaling collapse plots (Figure 2 in paper).

**Usage:**
```bash
python visualization/plot_scaling_collapse.py --data ../data/processed_data/fss_data.npz
```

### `visualization/plot_entanglement.py`

Creates entanglement entropy plots (Figure 3 in paper).

**Usage:**
```bash
python visualization/plot_entanglement.py
```

## Utility Functions

### `utils/data_loader.py`

Helper functions for loading and preprocessing data.

```python
from utils.data_loader import load_raw_data, load_processed_data

# Load all raw data
raw_data = load_raw_data('../data/raw_data/')

# Load specific processed dataset
phase_data = load_processed_data('../data/processed_data/phase_diagram.csv')
```

### `utils/fitting.py`

Functions for curve fitting and error estimation.

```python
from utils.fitting import power_law_fit, bootstrap_error

# Fit power law
params, errors = power_law_fit(x, y, yerr)

# Estimate errors via bootstrap
error = bootstrap_error(x, y, fit_function, n_bootstrap=1000)
```

### `utils/scaling.py`

Finite-size scaling utilities.

```python
from utils.scaling import collapse_data, extract_exponent

# Collapse data
x_scaled, y_scaled = collapse_data(L, g, order_param, nu, beta, g_c)

# Extract critical exponent
nu, nu_err = extract_exponent(L, g, susceptibility)
```

## Example Notebooks

### `examples/01_data_loading.ipynb`

Introduction to loading and exploring the datasets.

### `examples/02_phase_diagram.ipynb`

Interactive exploration of the phase diagram.

### `examples/03_scaling_analysis.ipynb`

Step-by-step finite-size scaling analysis.

### `examples/04_reproduce_figures.ipynb`

Reproducing all figures from the paper.

## Running the Analysis Pipeline

To reproduce all processed data and figures from scratch:

```bash
# 1. Extract critical exponents
python analysis/extract_critical_exponents.py

# 2. Perform finite-size scaling
python analysis/finite_size_scaling.py

# 3. Generate phase diagram
python analysis/phase_diagram.py

# 4. Create all figures
python visualization/plot_phase_diagram.py
python visualization/plot_scaling_collapse.py
python visualization/plot_entanglement.py
```

Or use the convenience script:
```bash
./run_full_analysis.sh
```

## Testing

Run unit tests:
```bash
pytest tests/
```

## Code Style

This code follows PEP 8 style guidelines. Format code using:
```bash
black .
flake8 .
```

## Contributing

See `../CONTRIBUTING.md` for guidelines on contributing to this codebase.

## License

The code in this directory is licensed under the MIT License. See `../LICENSE` for details.
