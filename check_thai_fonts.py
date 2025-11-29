#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check available fonts that support Thai characters in matplotlib
"""

import sys
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

# Fix Windows console encoding
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 80)
print("Checking fonts that support Thai characters...")
print("=" * 80)

# Common fonts that support Thai
thai_fonts = [
    'Tahoma',
    'Arial Unicode MS',
    'Thonburi',
    'Leelawadee UI',
    'Angsana New',
    'Browallia New',
    'Cordia New',
    'DilleniaUPC',
    'FreeSans',
    'DejaVu Sans',
]

# Get all available fonts
available_fonts = [f.name for f in fm.fontManager.ttflist]

print("\n✓ Thai-compatible fonts found on your system:\n")
found_fonts = []
for font in thai_fonts:
    if font in available_fonts:
        print(f"  • {font}")
        found_fonts.append(font)

if not found_fonts:
    print("  ⚠ No Thai fonts found in the predefined list")
    print("\n  All available fonts on your system:")
    for i, font in enumerate(sorted(set(available_fonts))[:20], 1):
        print(f"  {i}. {font}")
    print(f"  ... and {len(set(available_fonts)) - 20} more fonts")
else:
    print(f"\n✓ Recommended font to use: {found_fonts[0]}")

# Test Thai rendering
print("\n" + "=" * 80)
print("Testing Thai text rendering...")
print("=" * 80)

if found_fonts:
    plt.rcParams['font.family'] = found_fonts[0]

    fig, ax = plt.subplots(figsize=(10, 2))
    ax.text(0.5, 0.5, 'ทดสอบภาษาไทย - Thai Text Test',
            ha='center', va='center', fontsize=20)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('thai_font_test.png', dpi=100, bbox_inches='tight')
    print(f"\n✓ Test image saved as 'thai_font_test.png' using font: {found_fonts[0]}")
    print("  Check if Thai characters display correctly in the image.")
else:
    print("\n⚠ No Thai-compatible fonts found. Thai text may not display correctly.")
    print("\nTo fix this on Windows:")
    print("  1. The font 'Tahoma' or 'Leelawadee UI' should already be installed")
    print("  2. Try restarting your Python kernel/notebook")
    print("\nTo fix this on Linux:")
    print("  sudo apt-get install fonts-thai-tlwg")
    print("\nTo fix this on macOS:")
    print("  Install 'Thonburi' font (usually pre-installed)")

print("\n" + "=" * 80)
