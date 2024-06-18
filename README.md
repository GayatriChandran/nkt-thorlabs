# nkt-measure
Code to control a Thorlabs PM100D power meter and NKT VARIA to test spectral properties of a sample. 

Setup : NKT SuperK EXTREME laser source is connected to a SuperK VARIA 
for wavelength and bandwidth selection. Output is measured using a 
Thorlabs PM100D power meter and S130C sesor.

Logic/Steps : 
1. Set a center wavelength and bandwidth (1 nm). 
2. Set wavelength in the power sensor. 
3. Measure with appropriate time delays (since the stage inside the VARIA is pretty slow)
4. Loop through a range of wavelengths.

Notes : 
1. The source is operated at 70% power.
2. The power meter's output is in units of Watts.
3. An environment file (.yml) is included.
## Helper files for quickly checking results 
`plot_single.py` : Plots power (in mW) vs wavelength from one run.  
`plot_ratio.py` : Plots a ratio, for example input power vs deflected power. 
