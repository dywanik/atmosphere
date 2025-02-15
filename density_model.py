#!/usr/bin/env python3
#~ 
#~ Values taken from Vallado's "Fundamentals of Astrodynamics 
#~ and Applications (2nd Edition)". Page 537, table 8-4
#~ 
#~ Remigiusz Pospieszynski
#~ MMXVI
#~ 

#!/usr/bin/env python3
import math

# Define density values as tuples (h_min, h_max, h_0, rho_0, H)
DENSITY_TABLE = [
    (0, 25, 0, 1.225, 7.249),
    (25, 30, 25, 3.899e-2, 6.349),
    (30, 40, 30, 1.774e-2, 6.682),
    (40, 50, 40, 3.972e-3, 7.554),
    (50, 60, 50, 1.057e-3, 8.382),
    (60, 70, 60, 3.206e-4, 7.714),
    (70, 80, 70, 8.77e-5, 6.549),
    (80, 90, 80, 1.905e-5, 5.799),
    (90, 100, 90, 3.396e-6, 5.382),
    (100, 110, 100, 5.297e-7, 5.877),
    (110, 120, 110, 9.661e-8, 7.263),
    (120, 130, 120, 2.438e-8, 9.473),
    (130, 140, 130, 8.484e-9, 12.636),
    (140, 150, 140, 3.845e-9, 16.149),
    (150, 180, 150, 2.070e-9, 22.523),
    (180, 200, 180, 5.464e-10, 29.74),
    (200, 250, 200, 2.789e-10, 37.105),
    (250, 300, 250, 7.248e-11, 45.546),
    (300, 350, 300, 2.418e-11, 53.628),
    (350, 400, 350, 9.518e-12, 53.298),
    (400, 450, 400, 3.725e-12, 58.515),
    (450, 500, 450, 1.585e-12, 60.828),
    (500, 600, 500, 6.967e-13, 63.822),
    (600, 700, 600, 1.454e-13, 71.835),
    (700, 800, 700, 3.614e-14, 88.667),
    (800, 900, 800, 1.17e-14, 124.64),
    (900, 1000, 900, 5.245e-15, 181.05),
    (1000, float("inf"), 1000, 3.019e-15, 268)
]

def den(h_ellp):
    """Calculate atmospheric density at a given altitude using an exponential model."""
    for h_min, h_max, h_0, rho_0, H in DENSITY_TABLE:
        if h_min <= h_ellp < h_max:
            return rho_0 * math.exp(-(h_ellp - h_0) / H)
    return None 

if __name__ == "__main__":
    test_altitudes = [0, 50, 150, 500, 1000, 1200]
    for alt in test_altitudes:
        print(f"Density: {density_model.den(h_ellp):.6e} kg/m^3")

