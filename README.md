# Quantum Criticality and Factorization in a Constrained Rydberg Spin Chain

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## Overview

This repository contains the numerical data, analysis code, and figures associated with the research paper:

**"Quantum Criticality and Factorization in a Constrained Rydberg Spin Chain"**

The data provided here allows for independent verification of our results and enables other researchers to perform their own scaling analysis and extensions of this work.

## Repository Structure

```
.
├── data/
│   ├── raw_data/          # Raw numerical data from simulations
│   └── processed_data/    # Processed data ready for analysis
├── figures/               # Figures from the paper
├── code/                  # Analysis and visualization scripts
├── LICENSE                # License information
├── CITATION.cff           # Citation information
├── metadata.json          # Metadata describing the datasets
└── README.md             # This file
```

## Data Description

### Raw Data (`data/raw_data/`)

Contains the raw output from numerical simulations:
- Ground state energies
- Order parameters
- Correlation functions
- Entanglement measures
- Finite-size scaling data

### Processed Data (`data/processed_data/`)

Contains processed datasets ready for analysis:
- Scaled data for critical analysis
- Extracted critical exponents
- Phase diagram data
- Factorization transition points

See individual README files in each data directory for detailed format specifications.

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/UynajGI/Quantum-criticality-and-factorization-in-a-constrained-Rydberg-spin-chain.git
cd Quantum-criticality-and-factorization-in-a-constrained-Rydberg-spin-chain

# Install required Python packages (optional, for using analysis scripts)
pip install -r requirements.txt
```

### Loading Data

```python
import numpy as np
import json

# Load processed data
data = np.load('data/processed_data/example_dataset.npy')

# Load metadata
with open('metadata.json', 'r') as f:
    metadata = json.load(f)
```

See the `code/` directory for complete examples of data loading and visualization.

## Data Format

All numerical data is stored in standard formats:
- **NumPy arrays** (`.npy`, `.npz`) for multidimensional numerical data
- **CSV files** (`.csv`) for tabular data
- **JSON files** (`.json`) for metadata and parameters

## Citation

If you use this data in your research, please cite:

```bibtex
@article{YourName2024,
  title={Quantum Criticality and Factorization in a Constrained Rydberg Spin Chain},
  author={Author Names},
  journal={Journal Name},
  year={2024},
  doi={10.XXXX/XXXXXX}
}
```

Also see `CITATION.cff` for machine-readable citation information.

## License

This data repository is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to:
- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:
- Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made.

## Contact

For questions or issues regarding this data, please:
- Open an issue on GitHub
- Contact the corresponding author at: [email@institution.edu]

## Acknowledgments

This work was supported by [Funding Agency/Grant Number]. Computational resources were provided by [Computing Facility].

## Version History

- **v1.0.0** (2024-XX-XX): Initial public release