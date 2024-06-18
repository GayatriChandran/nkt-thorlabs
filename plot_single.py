#!/usr/bin/env python
"""
Plot the spectrum from a measurement (.csv file).

Gayatri 6/24
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == "__main__":

    file_name = '500_650_NKT70_meta_240.csv'                    # Input file name

    df = pd.read_csv(file_name)
    df.power *=1000                                                 # Convert units to mW

    ax = df.plot(x="wavelength", y="power", alpha=0.5, style='.-')
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Power (mW)")
    ax.set_title(file_name)                                         # Plot the spectrum

    plt.show()

    fig = ax.get_figure()                                           # Save the picture
    fig_name = file_name.rsplit('.csv')[0]
    fig.savefig(fig_name)

