# Figures

This directory contains high-resolution figures from the paper.

## Figure List

### Main Figures

- **`figure1_phase_diagram.pdf`**: Phase diagram showing different phases and transition lines
  - Also available in: PNG (300 dpi), SVG (vector)
  
- **`figure2_scaling_collapse.pdf`**: Finite-size scaling collapse demonstrating critical behavior
  - Panels: (a) Order parameter, (b) Susceptibility, (c) Correlation length
  - Also available in: PNG (300 dpi), SVG (vector)

- **`figure3_entanglement.pdf`**: Entanglement entropy across phase transitions
  - Shows von Neumann entropy and scaling behavior
  - Also available in: PNG (300 dpi), SVG (vector)

- **`figure4_factorization.pdf`**: Factorization transition and quantum correlations
  - Demonstrates the factorization point and its evolution
  - Also available in: PNG (300 dpi), SVG (vector)

### Supplementary Figures

- **`figureS1_energy_levels.pdf`**: Low-lying energy spectrum
- **`figureS2_correlation_functions.pdf`**: Spatial correlation functions
- **`figureS3_schmidt_spectrum.pdf`**: Schmidt spectrum analysis
- **`figureS4_finite_size_effects.pdf`**: Finite-size effects analysis

## File Formats

- **PDF**: Vector format, recommended for publications
- **PNG**: Raster format at 300 dpi, suitable for presentations
- **SVG**: Scalable vector graphics, editable

## Reproduction

All figures can be reproduced using scripts in the `code/visualization/` directory:

```bash
# Reproduce main figures
python ../code/visualization/plot_phase_diagram.py --output figure1_phase_diagram.pdf
python ../code/visualization/plot_scaling_collapse.py --output figure2_scaling_collapse.pdf
python ../code/visualization/plot_entanglement.py --output figure3_entanglement.pdf
python ../code/visualization/plot_factorization.py --output figure4_factorization.pdf

# Reproduce supplementary figures
python ../code/visualization/plot_energy_spectrum.py --output figureS1_energy_levels.pdf
```

## Figure Styling

All figures use:
- Font: Arial or Helvetica
- Font size: 8-10 pt for labels, 6-8 pt for tick labels
- Line width: 1.5 pt
- Color scheme: Colorblind-friendly palette
- Format: Consistent with journal requirements

## License

Figures are licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

When reusing these figures:
- Provide appropriate citation to the original paper
- Indicate if any modifications were made
- Link to the license
