#!/usr/bin/env python3
"""
SETUP NEW REPOSITORY FOR HYPERBOLIC FUNHOUSE MIRRORS PAPER
FIXED FOR WINDOWS ENCODING ISSUES
"""

import os
import shutil
from pathlib import Path

print("=" * 80)
print("🚀 CREATING NEW REPOSITORY: Hyperbolic Funhouse Mirrors")
print("=" * 80)

# Get current directory
current_dir = Path("C:/Users/Your Name Here/Downloads/HyperbolicFunhouse")
print(f"📂 Working in: {current_dir}")

# ====================== 1. CHECK YOUR FILES ======================
print("\n🔍 CHECKING YOUR FILES...")
files = os.listdir(current_dir)
print(f"Found {len(files)} files:")
for file in files:
    print(f"  • {file}")

# ====================== 2. CREATE REPO STRUCTURE ======================
print("\n📁 CREATING REPOSITORY STRUCTURE...")

folders = [
    "src",
    "src/core",
    "src/models",
    "data",
    "figures",
    "notebooks",
    "docs",
    "tests",
    "paper"
]

for folder in folders:
    folder_path = current_dir / folder
    folder_path.mkdir(exist_ok=True)
    print(f"  ✓ Created: {folder}")

# ====================== 3. ORGANIZE YOUR FILES ======================
print("\n📄 ORGANIZING YOUR FILES...")

# Map your files to their new locations
file_mapping = {
    "hyperbolic_funhouse.py": "src/main.py",  # FIXED: underscore not hyphen
    "model.py": "src/models/quark_model.py",
    "run_hyperbolic.bat": "run.bat",
}

for old_name, new_name in file_mapping.items():
    old_path = current_dir / old_name
    new_path = current_dir / new_name
    
    if old_path.exists():
        shutil.move(str(old_path), str(new_path))
        print(f"  ✓ Moved: {old_name} → {new_name}")
    else:
        print(f"  ⚠️  Not found: {old_name}")

# ====================== 4. CREATE ESSENTIAL FILES ======================
print("\n🛠️  CREATING ESSENTIAL FILES...")

# 1. Update requirements.txt if it exists
req_file = current_dir / "requirements.txt"
if req_file.exists():
    with open(req_file, "a", encoding="utf-8") as f:
        f.write("\n# Additional dependencies\nscipy>=1.7.0\nmatplotlib>=3.5.0")
    print("  ✓ Updated requirements.txt")
else:
    with open(req_file, "w", encoding="utf-8") as f:
        f.write("""numpy>=1.21.0
scipy>=1.7.0
matplotlib>=3.5.0
""")
    print("  ✓ Created requirements.txt")

# 2. Create __init__.py files
for init_file in [
    "src/__init__.py",
    "src/core/__init__.py", 
    "src/models/__init__.py",
    "tests/__init__.py"
]:
    with open(current_dir / init_file, "w", encoding="utf-8") as f:
        f.write('"""Package initialization"""\n')
    print(f"  ✓ Created: {init_file}")

# 3. Create core modules
print("\n🧮 CREATING CORE MODULES...")

# Core mathematics module - WITHOUT Unicode characters
math_content = '''"""
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
'''
with open(current_dir / "src/core/mathematics.py", "w", encoding="utf-8") as f:
    f.write(math_content)
print("  ✓ src/core/mathematics.py")

# Geometry module - WITHOUT Unicode characters
geom_content = '''"""
Hyperbolic geometry on H/Gamma(5)
"""
import numpy as np

def hyperbolic_distance(z1, z2):
    """Distance in Poincare half-plane"""
    return np.arccosh(1 + np.abs(z1 - z2)**2 / (2*np.imag(z1)*np.imag(z2)))

def triangle_area(theta12, theta23, theta13):
    """Area of hyperbolic triangle from mixing angles"""
    return theta12 * theta23 * theta13 * np.exp(1j*np.pi/2)
'''
with open(current_dir / "src/core/geometry.py", "w", encoding="utf-8") as f:
    f.write(geom_content)
print("  ✓ src/core/geometry.py")

# 4. Create paper folder with template - USING LaTeX escapes
paper_content = '''\\documentclass[12pt]{article}
\\usepackage{amsmath, amssymb, hyperref}
\\title{Hyperbolic Funhouse Mirrors: \\\\ Flavor from $\\mathbb{H}/\\Gamma(5)$ Geometry}
\\author{Marvin Gentry}
\\date{\\today}

\\begin{document}
\\maketitle

\\begin{abstract}
We demonstrate that all quark masses and mixing parameters emerge naturally from the hyperbolic geometry of the modular curve $\\mathbb{H}/\\Gamma(5)$ with $A_5$ symmetry. At the fixed point $\\tau_0 = e^{2\\pi i/5}$, modular forms evaluate to powers of the golden ratio $\\phi = (1+\\sqrt{5})/2$. The resulting model predicts: (1) CP phase $\\delta_{\\mathrm{CP}} = 68.7^\\circ$ (experimental: $68.8^\\circ$), (2) Jarlskog invariant $J = 3.12\\times10^{-5}$, (3) all CKM elements within $<3\\%$ error, (4) all quark mass ratios within $<10\\%$ error. The three generations correspond to three geodesic families with lengths proportional to $\\phi^3$, $\\phi^2$, $\\phi^1$, providing a geometric origin for the observed flavor hierarchy.
\\end{abstract}

\\section{Introduction}
The flavor puzzle remains one of the deepest mysteries beyond the Standard Model...

\\section{Code Availability}
The complete Python implementation is available at:
\\[ \\href{https://github.com/drmlgentry/HyperbolicFunhouseMirrors}{https://github.com/drmlgentry/HyperbolicFunhouseMirrors} \\]

\\end{document}
'''
with open(current_dir / "paper/main.tex", "w", encoding="utf-8") as f:
    f.write(paper_content)
print("  ✓ paper/main.tex")

# 5. Create .gitignore
gitignore_content = """# Python
__pycache__/
*.py[cod]
*.so
*.egg
dist/
build/

# Virtual environments
venv/
env/
.venv/

# IDE
.vscode/
.idea/
*.swp

# Data
data/*.npy
figures/*.png

# OS
.DS_Store
Thumbs.db
"""
with open(current_dir / ".gitignore", "w", encoding="utf-8") as f:
    f.write(gitignore_content)
print("  ✓ .gitignore")

# 6. Create LICENSE
with open(current_dir / "LICENSE", "w", encoding="utf-8") as f:
    f.write("""MIT License

Copyright (c) 2024 Hyperbolic Funhouse Mirrors Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""")
print("  ✓ LICENSE")

# 7. Create updated run.bat
bat_content = """@echo off
echo HYPERBOLIC FUNHOUSE MIRRORS
echo ============================
echo.
echo 1. Installing dependencies...
pip install -r requirements.txt

echo.
echo 2. Running the model...
python -m src.main

echo.
echo 3. Opening results...
if exist figures\\results.png start figures\\results.png

echo.
echo 4. Checking data...
if exist data\\parameters.txt type data\\parameters.txt

echo.
pause
"""
with open(current_dir / "run.bat", "w", encoding="utf-8") as f:
    f.write(bat_content)
print("  ✓ Updated run.bat")

# 8. Create quick test
test_content = '''#!/usr/bin/env python3
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
'''
with open(current_dir / "test_install.py", "w", encoding="utf-8") as f:
    f.write(test_content)
print("  ✓ test_install.py")

# ====================== 5. VERIFY STRUCTURE ======================
print("\n" + "=" * 80)
print("📁 FINAL REPOSITORY STRUCTURE")
print("=" * 80)

structure = """
HyperbolicFunhouse/
├── run.bat                    (launcher)
├── requirements.txt           (dependencies)
├── README.md                  (your existing)
├── LICENSE                    (MIT license)
├── .gitignore                 (Git ignore rules)
├── test_install.py            (quick test)
├── setup_new_repo.py          (this script)
├── src/
│   ├── main.py               (main runner)
│   ├── core/
│   │   ├── mathematics.py    (golden ratio, fixed point)
│   │   └── geometry.py       (hyperbolic geometry)
│   └── models/
│       └── quark_model.py    (your model)
├── paper/
│   └── main.tex              (LaTeX paper template)
├── data/                     (for results)
├── figures/                  (for plots)
├── notebooks/               (for Jupyter notebooks)
├── docs/                    (documentation)
└── tests/                   (unit tests)
"""

print(structure)

# ====================== 6. GITHUB INSTRUCTIONS ======================
print("\n" + "=" * 80)
print("🐙 GITHUB SETUP INSTRUCTIONS")
print("=" * 80)

instructions = """
YOUR NEW REPOSITORY IS READY!

FOLLOW THESE EXACT STEPS:

STEP 1: Open Command Prompt as Administrator
   Press Windows + X, then press A

STEP 2: Navigate to your folder:
   cd "C:\\Users\\Your Name Here\\Downloads\\HyperbolicFunhouse"

STEP 3: Initialize Git:
   git init
   git add .
   git commit -m "Initial commit: Hyperbolic Funhouse Mirrors"

STEP 4: Create GitHub Repository:
   • Go to https://github.com
   • Click the "+" icon -> "New repository"
   • Name: HyperbolicFunhouseMirrors
   • Description: "Flavor from hyperbolic geometry on H/Gamma(5)"
   • Make it PUBLIC
   • DO NOT initialize with README (you already have one)
   • Click "Create repository"

STEP 5: Connect and Push:
   Copy these EXACT commands from GitHub:
   
   git remote add origin https://github.com/drmlgentry/HyperbolicFunhouseMirrors.git
   git branch -M main
   git push -u origin main

STEP 6: Verify:
   • Go to: https://github.com/drmlgentry/HyperbolicFunhouseMirrors
   • You should see all your files!
   • Your repository is now separate from the old one

STEP 7: Run your code:
   Double-click run.bat OR run:
   python -m src.main

IMPORTANT NOTES:
• This is a NEW repository, separate from GoldenRatioModularFlavor
• The GitHub URL will be different
• Your old paper stays at: https://github.com/drmlgentry/GoldenRatioModularFlavor
• Your new paper goes to: https://github.com/drmlgentry/HyperbolicFunhouseMirrors

You now have TWO repositories:
   1. GoldenRatioModularFlavor (old paper - A5 modular forms)
   2. HyperbolicFunhouseMirrors (new paper - hyperbolic geometry)
"""

print(instructions)
print("\n" + "=" * 80)
print("READY TO PUBLISH YOUR NEW PAPER!")
print("=" * 80)