# Contributing to This Repository

Thank you for your interest in contributing to this data repository! We welcome contributions that improve documentation, add analysis tools, or enhance data accessibility.

## How to Contribute

### Reporting Issues

If you find errors in the data or documentation:

1. Check if the issue has already been reported
2. Open a new issue with:
   - Clear description of the problem
   - Steps to reproduce (if applicable)
   - Expected vs. actual behavior
   - Your environment (Python version, OS, etc.)

### Suggesting Enhancements

We welcome suggestions for:
- Additional data formats
- New analysis scripts
- Improved documentation
- Better visualization tools

Please open an issue to discuss your ideas before implementing them.

### Code Contributions

1. **Fork the repository**
   ```bash
   git clone https://github.com/UynajGI/Quantum-criticality-and-factorization-in-a-constrained-Rydberg-spin-chain.git
   cd Quantum-criticality-and-factorization-in-a-constrained-Rydberg-spin-chain
   ```

2. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow existing code style
   - Add docstrings to functions
   - Include comments for complex logic
   - Update documentation as needed

4. **Test your changes**
   ```bash
   python -m pytest tests/
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Brief description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   - Provide a clear description of changes
   - Reference any related issues
   - Wait for review and address feedback

## Code Style Guidelines

### Python

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use meaningful variable names
- Maximum line length: 100 characters
- Use type hints where appropriate

Example:
```python
import numpy as np
from typing import Tuple

def calculate_critical_exponent(
    sizes: np.ndarray,
    values: np.ndarray
) -> Tuple[float, float]:
    """Calculate critical exponent from finite-size scaling.
    
    Parameters
    ----------
    sizes : np.ndarray
        System sizes
    values : np.ndarray
        Observable values
        
    Returns
    -------
    exponent : float
        Critical exponent
    error : float
        Uncertainty estimate
    """
    # Implementation here
    pass
```

### Documentation

- Use Markdown for documentation files
- Include code examples where helpful
- Keep language clear and concise
- Use proper scientific notation and units

## Data Contributions

### Adding New Datasets

If you have related data to contribute:

1. Ensure data is well-documented
2. Include metadata (parameters, methods, etc.)
3. Use standard formats (NPY, CSV, JSON)
4. Add a README describing the data
5. Open an issue to discuss inclusion

### Data Format Requirements

- **NumPy arrays**: Use `.npy` or `.npz` format
- **Tabular data**: Use CSV with clear column headers
- **Metadata**: Use JSON format
- **Include units** in documentation
- **Document uncertainties** where applicable

## Analysis Scripts

When contributing analysis code:

1. **Include docstrings**
   - Describe what the script does
   - List input/output files
   - Document parameters

2. **Add command-line interface**
   ```python
   import argparse
   
   parser = argparse.ArgumentParser(description='Script description')
   parser.add_argument('--input', help='Input file path')
   parser.add_argument('--output', help='Output file path')
   ```

3. **Handle errors gracefully**
   ```python
   try:
       data = np.load(filename)
   except FileNotFoundError:
       print(f"Error: File {filename} not found")
       sys.exit(1)
   ```

4. **Include example usage**
   - In docstring
   - In README
   - In comments

## Testing

### Writing Tests

- Place tests in `tests/` directory
- Use `pytest` framework
- Test both expected behavior and edge cases
- Include test data in `tests/data/` if needed

Example:
```python
import pytest
import numpy as np
from utils.fitting import power_law_fit

def test_power_law_fit():
    """Test power law fitting function."""
    # Generate test data
    x = np.array([1, 2, 3, 4, 5])
    y = 2 * x**1.5
    
    # Fit
    params, errors = power_law_fit(x, y)
    
    # Assert
    assert np.isclose(params[0], 2.0, rtol=0.01)
    assert np.isclose(params[1], 1.5, rtol=0.01)
```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_fitting.py

# Run with coverage
pytest --cov=code tests/
```

## Documentation

### Updating Documentation

- Keep README files current
- Update CHANGELOG for significant changes
- Document breaking changes prominently
- Include migration guides if needed

### Adding Examples

- Place Jupyter notebooks in `code/examples/`
- Include clear explanations
- Show expected output
- Test notebooks before committing

## Pull Request Process

1. **Before submitting:**
   - Run tests and ensure they pass
   - Update documentation
   - Check code style
   - Rebase on latest main branch

2. **PR description should include:**
   - Summary of changes
   - Motivation and context
   - Type of change (bugfix, feature, docs, etc.)
   - Testing performed
   - Screenshots (if applicable)

3. **Review process:**
   - Maintainers will review your PR
   - Address feedback promptly
   - Be open to suggestions
   - Keep discussion professional and constructive

4. **After approval:**
   - PR will be merged by maintainer
   - Your contribution will be acknowledged
   - Consider joining ongoing discussions

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discriminatory language
- Personal attacks or trolling
- Publishing others' private information
- Other unprofessional conduct

## Questions?

- Open an issue for general questions
- Email maintainers for sensitive matters
- Join discussions in existing issues/PRs

## Recognition

Contributors will be acknowledged in:
- README.md contributors section
- Release notes
- Academic papers (for substantial contributions)

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (CC BY 4.0 for data, MIT for code).

---

Thank you for contributing to open science! 🎉
