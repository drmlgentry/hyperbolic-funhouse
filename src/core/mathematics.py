"""
Core mathematical foundations
Golden ratio phi = (1+sqrt(5))/2 from A5 symmetry
"""

import numpy as np

PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
TAU0 = np.exp(2j * np.pi / 5)  # Fixed point on H/Gamma(5)

def print_golden_ratio():
    """Display golden ratio properties"""
    print(f"phi = {PHI:.10f}")
    print(f"phi^2 = phi + 1 = {PHI**2:.6f}")
    print(f"1/phi = phi - 1 = {1/PHI:.6f}")
    return PHI
