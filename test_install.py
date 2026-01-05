#!/usr/bin/env python3
"""
Quick test to verify installation
"""
import sys
try:
    import numpy as np
    from src.core.mathematics import PHI
    print("SUCCESS!")
    print(f"Golden ratio: phi = {PHI:.6f}")
    print(f"Three generations: phi^3={PHI**3:.2f}, phi^2={PHI**2:.2f}, phi={PHI:.2f}")
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(1)
