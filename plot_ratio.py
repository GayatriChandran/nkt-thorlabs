#!/usr/bin/env python
"""
Plot the ratio of two sets of measurements. In this case, 
'input' is the power incident on a metasurface. And 'deflected' is
 the power reflected from the surface.

Gayatri 6/24
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == "__main__":

    input = pd.read_csv('input_test.csv')               # Input files
    deflected = pd.read_csv('deflected_test.csv')

    input.power *=1000                                                  # Unnecessary, since it is a ratio.
    deflected.power *=1000                                              # But just to remind ourselves about the unit.

    result = pd.DataFrame(deflected.power/input.power)                  # Take ratio
    result.insert(0, "wavelength", input.wavelength, True)              # Add wavelength column

    ax=result.plot(x="wavelength", y="power", alpha=0.5, style='.-')    # Plot result
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Deflected power / Input power ")
    ax.set_title('Sample name')

    plt.show()
    
    fig = ax.get_figure()
    fig.savefig('sample_test')                                             # Save figure