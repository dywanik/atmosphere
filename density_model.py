#!/usr/bin/env python
#~ 
#~ Values taken from Vallado's "Fundamentals of Astrodynamics 
#~ and Applications (2nd Edition)". Page 537, table 8-4
#~ 
#~ Remigiusz Pospieszynski
#~ MMXVI
#~ 
import math

def den(h_ellp):
	if h_ellp >= 0  and h_ellp < 25 :
		h_0 = 0
		rho_0 = 1.225
		H = 7.249		
	if h_ellp >= 25 and h_ellp < 30 :
		h_0 = 25
		rho_0 = 3.899*10**(-2)
		H = 6.349		
	if h_ellp >= 30 and h_ellp < 40 :
		h_0 = 30
		rho_0 = 1.774*10**(-2)
		H = 6.682
	if h_ellp >= 40 and h_ellp < 50 :
		h_0 = 40
		rho_0 = 3.972*10**(-3)
		H = 7.554
	if h_ellp >= 50 and h_ellp < 60 :
		h_0 = 50
		rho_0 = 1.057*10**(-3)
		H = 8.382
	if h_ellp >= 60 and h_ellp < 70 :
		h_0 = 60
		rho_0 = 3.206*10**(-4)
		H = 7.714
	if h_ellp >= 70 and h_ellp < 80 :
		h_0 = 70
		rho_0 = 8.77*10**(-5)
		H = 6.549
	if h_ellp >= 80 and h_ellp < 90 :
		h_0 = 80
		rho_0 = 1.905*10**(-5)
		H = 5.799
	if h_ellp >= 90 and h_ellp < 100 :
		h_0 = 90
		rho_0 = 3.396*10**(-6)
		H = 5.382
	if h_ellp >= 100 and h_ellp < 110 :
		h_0 = 100
		rho_0 = 5.297*10**(-7)
		H = 5.877
	if h_ellp >= 110 and h_ellp < 120 :
		h_0 = 110
		rho_0 = 9.661*10**(-8)
		H = 7.263
	if h_ellp >= 120 and h_ellp < 130 :
		h_0 = 120
		rho_0 = 2.438*10**(-8)
		H = 9.473												
	if h_ellp >= 130 and h_ellp < 140 :
		h_0 = 130
		rho_0 = 8.484*10**(-9)
		H = 12.636
	if h_ellp >= 140 and h_ellp < 150 :
		h_0 = 140
		rho_0 = 3.845*10**(-9)
		H = 16.149
	if h_ellp >= 150 and h_ellp < 180 :
		h_0 = 150
		rho_0 = 2.070*10**(-9)
		H = 22.523
	if h_ellp >= 180 and h_ellp < 200 :
		h_0 = 180
		rho_0 = 5.464*10**(-10)
		H = 29.74
	if h_ellp >= 200 and h_ellp < 250 :
		h_0 = 200
		rho_0 = 2.789*10**(-10)
		H = 37.105
	if h_ellp >= 250 and h_ellp < 300 :
		h_0 = 250
		rho_0 =7.248*10**(-11)
		H = 45.546
	if h_ellp >= 300 and h_ellp < 350 :
		h_0 = 300
		rho_0 = 2.418*10**(-11)
		H = 53.628
	if h_ellp >= 350 and h_ellp < 400 :
		h_0 = 350
		rho_0 = 9.518*10**(-12)
		H = 53.298
	if h_ellp >= 400 and h_ellp < 450 :
		h_0 = 400
		rho_0 = 3.725*10**(-12)
		H = 58.515
	if h_ellp >= 450 and h_ellp < 500 :
		h_0 = 450
		rho_0 = 1.585*10**(-12)
		H = 60.828
	if h_ellp >= 500 and h_ellp < 600 :
		h_0 = 500
		rho_0 = 6.967*10**(-13)
		H = 63.822
	if h_ellp >= 600 and h_ellp < 700 :
		h_0 = 600
		rho_0 = 1.454*10**(-13)
		H = 71.835
	if h_ellp >= 700 and h_ellp < 800:
		h_0 = 700
		rho_0 = 3.614*10**(-14)
		H = 88.667
	if h_ellp >= 800 and h_ellp < 900 :
		h_0 = 800
		rho_0 = 1.17*10**(-14)
		H = 124.64
	if h_ellp >= 900 and h_ellp < 1000 :
		h_0 = 900
		rho_0 = 5.245*10**(-15)
		H = 181.05
	if h_ellp >= 1000:
		h_0 = 1000
		rho_0 = 3.019*10**(-15)
		H = 268									
	return rho_0*math.exp(-(h_ellp-h_0)/H)
