"""
Data loading utilities for the Rydberg spin chain dataset.

This module provides convenient functions for loading raw and processed data.
"""

import numpy as np
import pandas as pd
import json
from pathlib import Path
from typing import Dict, Any, Optional, Tuple


def load_metadata(metadata_path: str = "metadata.json") -> Dict[str, Any]:
    """
    Load metadata describing the datasets.
    
    Parameters
    ----------
    metadata_path : str
        Path to metadata.json file
        
    Returns
    -------
    metadata : dict
        Metadata dictionary
    """
    with open(metadata_path, 'r') as f:
        metadata = json.load(f)
    return metadata


def load_ground_state_energies(
    data_dir: str = "data/raw_data"
) -> Dict[str, np.ndarray]:
    """
    Load ground state energy data.
    
    Parameters
    ----------
    data_dir : str
        Directory containing raw data files
        
    Returns
    -------
    data : dict
        Dictionary with keys: 'L', 'g', 'E', 'E_per_site'
        
    Examples
    --------
    >>> data = load_ground_state_energies()
    >>> sizes = data['L']
    >>> energies = data['E']
    """
    filepath = Path(data_dir) / "ground_state_energies.npz"
    
    if not filepath.exists():
        raise FileNotFoundError(
            f"Ground state energy file not found: {filepath}\n"
            "This is placeholder code. Actual data files need to be generated."
        )
    
    with np.load(filepath) as data:
        return {key: data[key] for key in data.keys()}


def load_order_parameters(
    data_dir: str = "data/raw_data"
) -> Dict[str, np.ndarray]:
    """
    Load order parameter data.
    
    Parameters
    ----------
    data_dir : str
        Directory containing raw data files
        
    Returns
    -------
    data : dict
        Dictionary with keys: 'L', 'g', 'magnetization', 
        'staggered_magnetization', 'density'
    """
    filepath = Path(data_dir) / "order_parameters.npz"
    
    if not filepath.exists():
        raise FileNotFoundError(
            f"Order parameter file not found: {filepath}\n"
            "This is placeholder code. Actual data files need to be generated."
        )
    
    with np.load(filepath) as data:
        return {key: data[key] for key in data.keys()}


def load_correlation_functions(
    data_dir: str = "data/raw_data"
) -> Dict[str, np.ndarray]:
    """
    Load correlation function data.
    
    Parameters
    ----------
    data_dir : str
        Directory containing raw data files
        
    Returns
    -------
    data : dict
        Dictionary with keys: 'L', 'g', 'r', 'Czz', 'Cnn'
    """
    filepath = Path(data_dir) / "correlation_functions.npz"
    
    if not filepath.exists():
        raise FileNotFoundError(
            f"Correlation function file not found: {filepath}\n"
            "This is placeholder code. Actual data files need to be generated."
        )
    
    with np.load(filepath) as data:
        return {key: data[key] for key in data.keys()}


def load_entanglement(
    data_dir: str = "data/raw_data"
) -> Dict[str, np.ndarray]:
    """
    Load entanglement entropy data.
    
    Parameters
    ----------
    data_dir : str
        Directory containing raw data files
        
    Returns
    -------
    data : dict
        Dictionary with keys: 'L', 'g', 'S_vN', 'S_renyi', 'schmidt_gap'
    """
    filepath = Path(data_dir) / "entanglement.npz"
    
    if not filepath.exists():
        raise FileNotFoundError(
            f"Entanglement file not found: {filepath}\n"
            "This is placeholder code. Actual data files need to be generated."
        )
    
    with np.load(filepath) as data:
        return {key: data[key] for key in data.keys()}


def load_phase_diagram(
    data_dir: str = "data/processed_data"
) -> pd.DataFrame:
    """
    Load phase diagram data.
    
    Parameters
    ----------
    data_dir : str
        Directory containing processed data files
        
    Returns
    -------
    phase_data : pd.DataFrame
        DataFrame with columns: 'g_c', 'phase_left', 'phase_right', 
        'transition_type'
    """
    filepath = Path(data_dir) / "phase_diagram.csv"
    
    if not filepath.exists():
        raise FileNotFoundError(
            f"Phase diagram file not found: {filepath}\n"
            "This is placeholder code. Actual data files need to be generated."
        )
    
    return pd.read_csv(filepath)


def load_critical_exponents(
    data_dir: str = "data/processed_data"
) -> Dict[str, Any]:
    """
    Load critical exponents with uncertainties.
    
    Parameters
    ----------
    data_dir : str
        Directory containing processed data files
        
    Returns
    -------
    exponents : dict
        Dictionary of critical exponents for each transition
    """
    filepath = Path(data_dir) / "critical_exponents.json"
    
    if not filepath.exists():
        raise FileNotFoundError(
            f"Critical exponents file not found: {filepath}\n"
            "This is placeholder code. Actual data files need to be generated."
        )
    
    with open(filepath, 'r') as f:
        exponents = json.load(f)
    
    return exponents


def load_fss_data(
    data_dir: str = "data/processed_data"
) -> Dict[str, np.ndarray]:
    """
    Load finite-size scaling data.
    
    Parameters
    ----------
    data_dir : str
        Directory containing processed data files
        
    Returns
    -------
    data : dict
        Dictionary with scaled data and exponents
    """
    filepath = Path(data_dir) / "fss_data.npz"
    
    if not filepath.exists():
        raise FileNotFoundError(
            f"FSS data file not found: {filepath}\n"
            "This is placeholder code. Actual data files need to be generated."
        )
    
    with np.load(filepath) as data:
        return {key: data[key] for key in data.keys()}


def get_data_summary() -> str:
    """
    Get a summary of available datasets.
    
    Returns
    -------
    summary : str
        Summary of available data files
    """
    try:
        metadata = load_metadata()
        summary = f"Dataset: {metadata['title']}\n"
        summary += f"Version: {metadata['version']}\n"
        summary += f"License: {metadata['license']}\n\n"
        summary += "Available datasets:\n"
        
        for category, datasets in metadata['datasets'].items():
            summary += f"\n{category.replace('_', ' ').title()}:\n"
            for name, info in datasets.items():
                summary += f"  - {name}: {info['description']}\n"
        
        return summary
    except FileNotFoundError:
        return "Metadata file not found. Please ensure metadata.json exists."


if __name__ == "__main__":
    # Example usage
    print("Data Loading Utilities")
    print("=" * 50)
    print(get_data_summary())
