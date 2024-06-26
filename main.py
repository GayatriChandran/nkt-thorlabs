#!/usr/bin/env python
"""
Sweep NKT VARIA through a range of wavelengths. Measure output 
using a Thorlabs PM100D power meter and S130C sensor. 

Gayatri 6/24
"""

from nkt_tools.varia import Varia
import time
import numpy as np
import pyvisa
from ThorlabsPM100 import ThorlabsPM100
import matplotlib.pyplot as plt

rm = pyvisa.ResourceManager()
inst = rm.open_resource('USB0::0x1313::0x8078::P0004558::INSTR')

power_meter = ThorlabsPM100(inst=inst)                          # Thorlabs power meter object intialized

varia = Varia()                                                 # NKT VARIA object intialized

if __name__ == "__main__":

    meta = 'dose_240'                                           # Which metasurface is being measured. 
    start_wavelength = 500                                      # Input start wavelength (nm) for sweep
    end_wavelength = 650                                        # Input end wavelength (nm)

    spectrum = np.arange(start_wavelength,end_wavelength)
    readings = np.zeros((np.size(spectrum),), dtype=float)

    print("Set range auto and wait 500ms    ...")
    power_meter.sense.power.dc.range.auto = "ON"
    power_meter.sense.average.count = 200
    varia.long_setpoint = spectrum[0]+0.5
    varia.short_setpoint = spectrum[0]-0.5                              # Set VARIA wavelength
    

    time.sleep(5)                                              # Enough time to get into position.
    

    for i in range(np.size(spectrum)):        
 
        power_meter.sense.correction.wavelength = float(spectrum[i])        # Set power-meter wavelength         
        print("Wavelength :", power_meter.sense.correction.wavelength)
        varia.long_setpoint = spectrum[i]+0.5
        varia.short_setpoint = spectrum[i]-0.5                              # Set VARIA wavelength and bandwidth
        

        time.sleep(.5)                                                       # Wait to settle

        readings[i] = power_meter.read
        time.sleep(.5)                                                      # Ended one measurement !

    
    file_name = str(start_wavelength) + '_' + str(end_wavelength) + '_NKT70' + '_meta_' + meta + '.csv'
    np.savetxt(file_name, np.column_stack((spectrum, readings)), delimiter=',', header="wavelength,power")

    # Before signing out, go back to the default 10nm bandwidth in the red region.
    varia.short_setpoint = 630
    varia.long_setpoint = 640

    inst.close()                                                            # Close this instance of the power-meter object
    
