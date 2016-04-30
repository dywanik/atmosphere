#!/usr/bin/env python
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

choice = raw_input("Press [1] to calculate density and pressure on particular altitude OR press [2] to calculate changes on altitude span: ")

if choice == "1":
	h_ellp = float(raw_input('Enter altitude above Earth: '))
	print "Density:",density_model.den(h_ellp),"[kg/m^3]"
	print "Pressure:",pressure_model.press(h_ellp),"[N/m^2]"

if choice == "2":
	start = int(raw_input("Enter the starting altitude: "))
	stop = int(raw_input("Enter the final altitude: "))
	density = open('density.dat','w')
	pressure = open('pressure.dat','w')

	for alt in range(start,stop):
		den = density_model.den(alt)
		press = pressure_model.press(alt)
		density.write('%4.lf %.15lf \n' % (alt, den))
		pressure.write('%4.lf %.15lf \n' % (alt, press))
	density.close() 
	pressure.close()

	plt.plotfile('density.dat', delimiter=' ', cols=(0, 1))
	plt.plotfile('pressure.dat', delimiter=' ', cols=(0, 1),newfig=False)
	plt.xlabel('Altitude [km]')
	plt.ylabel('Density/Pressure')
	plt.title('Changes in pressure and density')
	plt.show()
