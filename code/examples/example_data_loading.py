"""
Example script demonstrating how to load and explore the data.

This script shows basic data loading and visualization techniques.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.data_loader import (
    get_data_summary,
    load_metadata
)


def main():
    """
    Main function demonstrating data loading.
    """
    print("=" * 70)
    print("Quantum Criticality in Constrained Rydberg Spin Chain")
    print("Data Loading Example")
    print("=" * 70)
    print()
    
    # Load and display metadata
    print("Loading metadata...")
    try:
        metadata = load_metadata()
        print(f"Dataset: {metadata['title']}")
        print(f"Version: {metadata['version']}")
        print(f"License: {metadata['license']}")
        print()
        
        # Display summary
        print(get_data_summary())
        print()
        
        # Show numerical methods used
        print("Numerical Methods Used:")
        print("-" * 70)
        for method, params in metadata['numerical_methods'].items():
            print(f"\n{method.replace('_', ' ').upper()}:")
            for key, value in params.items():
                print(f"  {key}: {value}")
        print()
        
    except FileNotFoundError as e:
        print(f"Note: {e}")
        print("\nThis is example code. Actual data files need to be generated")
        print("from your simulations and placed in the data/ directories.")
        print("\nFor now, this demonstrates the expected structure.")
    
    # Example of how to load and plot data (when available)
    print("\nExample Usage:")
    print("-" * 70)
    print("""
# Load ground state energies
from utils.data_loader import load_ground_state_energies

data = load_ground_state_energies()
sizes = data['L']
couplings = data['g']
energies = data['E_per_site']

# Plot energy vs coupling for different system sizes
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
for i, L in enumerate(sizes):
    plt.plot(couplings, energies[:, i], label=f'L={L}', marker='o')

plt.xlabel('Coupling parameter g')
plt.ylabel('Energy per site')
plt.legend()
plt.grid(True, alpha=0.3)
plt.title('Ground State Energy vs Coupling')
plt.tight_layout()
plt.savefig('energy_plot.pdf')
plt.show()
    """)
    
    print("\n" + "=" * 70)
    print("Repository Structure Successfully Created!")
    print("=" * 70)
    print("\nNext Steps:")
    print("1. Add your actual simulation data to data/raw_data/")
    print("2. Run analysis scripts to generate processed data")
    print("3. Generate figures using visualization scripts")
    print("4. Update metadata.json with your specific information")
    print("5. Update CITATION.cff with author information and DOI")
    print("6. Share your repository for open science!")


if __name__ == "__main__":
    main()
