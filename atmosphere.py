#!/usr/bin/env python3
#~
#~ Exponential Atmospheric Model as described by Vallado in his
#~ "Fundamentals of Astrodynamics and Applications (2nd Edition)"
#~
#~ Remigiusz Pospieszynski
#~ MMXVI
#~

import density_model
import pressure_model
import matplotlib.pyplot as plt
import numpy as np

# Get user input
choice = input("Press [1] to calculate density and pressure on a particular altitude OR press [2] to calculate changes on altitude span: ")

if choice == "1":
    h_ellp = float(input('Enter altitude above Earth: '))
    print(f"Density: {density_model.den(h_ellp):.6e} [kg/m^3]")
    print(f"Pressure: {pressure_model.press(h_ellp):.6e} [N/m^2]")

elif choice == "2":
    start = int(input("Enter the starting altitude: "))
    stop = int(input("Enter the final altitude: "))

    density_data = []
    pressure_data = []

    for alt in range(start, stop + 1):  # Include stop altitude
        den = density_model.den(alt)
        press = pressure_model.press(alt)
        density_data.append((alt, den))
        pressure_data.append((alt, press))

    # Save data using 'with open' for safety
    with open('density.dat', 'w') as density_file:
        for alt, den in density_data:
            density_file.write(f"{alt} {den:.15e}\n")

    with open('pressure.dat', 'w') as pressure_file:
        for alt, press in pressure_data:
            pressure_file.write(f"{alt} {press:.15e}\n")

    # Load data using numpy
    density_arr = np.loadtxt('density.dat')
    pressure_arr = np.loadtxt('pressure.dat')

    # Plot data
    plt.plot(density_arr[:, 0], density_arr[:, 1], label="Density [kg/m³]")
    plt.plot(pressure_arr[:, 0], pressure_arr[:, 1], label="Pressure [N/m²]")

    plt.xlabel('Altitude [km]')
    plt.ylabel('Density / Pressure')
    plt.title('Changes in Atmospheric Pressure and Density')
    plt.legend()
    plt.grid(True)
    plt.show()
