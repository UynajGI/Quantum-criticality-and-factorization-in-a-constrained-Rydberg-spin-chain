# Quantum criticality and factorization in a constrained Rydberg spin chain

This repository contains the numerical data and analysis scripts for the paper:
**"Quantum criticality and factorization in a constrained Rydberg spin chain"**

## Authors
Yuan Jiang, Wen-Long You, Liangsheng Li, and Maoxin Liu

---

## Data Structure (`/dat`)

The data files are organized by the figures presented in the paper. All files are in `.dat` (plain text) format.
The Hamiltonian parameters are defined as:
* **$\lambda$**: Dimensionless Rabi driving strength ($\Omega/J$).
* **$h$**: Dimensionless detuning ($\Delta'/J$).

### [Fig. 2] Global Phase Diagram
* **Location:** `/dat/Fig2/`
* **Description:** Ground-state entanglement entropy $S_{vN}$ map and phase boundaries in the $(h, \lambda)$ plane.
* **Files:**
    * `phase_diagram_svn.dat`: The 2D grid data for the heatmap ($h$, $\lambda$, $S_{vN}$).
    * `ising_critical_line.dat`: Coordinates of the Ising transition boundary (cyan curve).
    * `ll_critical_line.dat`: Coordinates of the Luttinger Liquid to Antiferromagnetic boundary (yellow curve).

### [Fig. 3] Phase Transition & Finite-Size Scaling (FSS)
* **Location:** `/dat/Fig3/`
* **Description:** Analysis of the Ising transition at fixed $h=-0.5$.
* **Files:**
    * `fidelity_susceptibility_DMRG.dat`: Fidelity susceptibility density $\chi_F/L$ vs. $\lambda$ using DMRG for system sizes $L \in \{169, 193, 217, 241\}$.
    * `order_parameter_VUMPS.dat`: Antiferromagnetic order parameter $O_{AFM}$ vs. $\lambda$ using VUMPS for bond dimensions $M \in \{16, 32, 64, 128, 256\}$.
    * `energy_gap_scaling.dat`: Neutral excitation gap $\Delta_E L^z$ data collapse.
    * `peak_scaling_inset.dat`: Power-law scaling of the peak fidelity susceptibility and energy gap with system size $L$.

### [Fig. 4] Entanglement Scaling & Central Charge
* **Location:** `/dat/Fig4/`
* **Description:** Characterization of the Luttinger Liquid (LL) phase and BKT-like transition.
* **Files:**
    * `svn_vs_lambda.dat`: Entanglement entropy $S_{vN}$ vs. $\lambda$ for bond dimensions $M \in \{16, 32, 64, 128, 256\}$.
    * `central_charge.dat`: Effective central charge $c$ extracted via finite-entanglement scaling (shows $c \approx 1$ in the LL phase).
    * `derivative_scaling.dat`: Scaling of the derivative peak maxima $|\partial_\lambda S_{vN}|_m$ vs. $\ln(\ln M)$.

### [Fig. 5] Exact Factorization & Concurrence
* **Location:** `/dat/Fig5/`
* **Description:** Evidence for the factorization line where entanglement vanishes.
* **Files:**
    * `concurrence_heatmap.dat`: 2D intensity map of nearest-neighbor concurrence $\mathcal{C}(\rho)$ in the $(h, \lambda)$ plane.
    * `bloch_vector.dat`: Evolution of the single-site state on the Bloch sphere.
    * `concurrence_ed_cuts.dat`: Concurrence $\mathcal{C}(\rho)$ crossing at the factorization point for ED system sizes $L \in \{12, 14, 16, 24, 28, 30\}$.

### [Fig. 6] Spatial Correlations & Structure Factors
* **Location:** `/dat/Fig6/`
* **Description:** Density-density correlations $C(r)$ and static structure factor $S(k)$.
* **Files:**
    * `correlation_lambda_0.10.dat`: Spatial correlation $C(r)$ in the LL phase ($\lambda=0.10$).
    * `correlation_lambda_0.35.dat`: Spatial correlation $C(r)$ in the AFM phase ($\lambda=0.35$).
    * `structure_factor_heatmap_data.dat`: Full evolution of $S(k)$ vs. $\lambda$.
    * `structure_factor_lambda_0.10.dat` & `...0.35.dat`: Slices of structure factors at specific $\lambda$.

---

## Technical Details
- **Numerical Methods:**
    - **ED**: Exact Diagonalization (up to $L=30$).
    - **DMRG**: Density Matrix Renormalization Group (up to $L=241$).
    - **VUMPS**: Variational Uniform Matrix Product States (infinite size, bond dimension up to $\chi=256$).
- **Model:** Constrained Rydberg spin chain with competing local Rabi driving and nonlocal dipole-dipole exchange.

## Status & Citation
This paper is currently **Submitted**. The citation details will be updated upon publication.

If you wish to refer to this dataset in the meantime, please link to this repository directly.