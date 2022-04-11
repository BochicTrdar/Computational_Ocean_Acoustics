# Effective sound speed of water with suspended air bubbles, 
# as function of volume fraction
 
from numpy import * 
from matplotlib.pyplot import *

Kw = 2.2e9
Ka = 142e3
rhoa = 1.2
rhow = 1000
phi1 = 1e-6
phi2 = 1e-2
phi = linspace(phi1,phi2,5001)

rhoe = phi*rhoa + ( 1 - phi )*rhow
Ke = 1/( phi/Ka + (1-phi)/Kw ) 
c = sqrt( Ke/rhoe )

figure(1)
semilogx(phi,c)
xlabel(r'Volume fraction')
ylabel('Sound speed (m/s)')
grid(True)

show()

print("done.")
