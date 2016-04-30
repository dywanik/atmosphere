#!/usr/bin/env python
#~ 
#~ Taken from Vallado's "Fundamentals of Astrodynamics and Applications
#~ (2nd Edition)". Page 537.
#~ 
#~ Remigiusz Pospieszynski
#~ MMXVI
#~ 
import math

def press(h_ellp):
	p_SL=1.0133
	H=7.0104
	return p_SL*math.exp(-(h_ellp/H))
