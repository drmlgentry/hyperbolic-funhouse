"""
Hyperbolic geometry on H/Gamma(5)
"""
import numpy as np

def hyperbolic_distance(z1, z2):
    """Distance in Poincare half-plane"""
    return np.arccosh(1 + np.abs(z1 - z2)**2 / (2*np.imag(z1)*np.imag(z2)))

def triangle_area(theta12, theta23, theta13):
    """Area of hyperbolic triangle from mixing angles"""
    return theta12 * theta23 * theta13 * np.exp(1j*np.pi/2)
