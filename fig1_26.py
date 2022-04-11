# Reflection loss at layered fluid bottom with the parameters given in Table 1.5.
# (a) Loss vs. grazing angle.
# (b) Contoured loss vs. frequency and grazing angle. 

from os import *
from numpy import *
from matplotlib.pyplot import *
from scipy.interpolate import interp1d
from wbounceenvfil import *
from readbrc import *

case_title = "Layered fluid bottom"
freq = 25.0
rmaxkm = 10.0
clow  = 1500.0
chigh = 1.00e6
nmedia  = 1
options = "CAW"
parw = array([0.0, 1500.0, 0.0, 1.0, 0.0, 0.0])
parl = array([[2.0,1550.0, 0.0, 1.5, 0.2, 0.0],
              [2.0,1800.0, 0.0, 2.0, 0.5, 0.0]])

print( 'Case (a)...' )

wbounceenvfil("coa",case_title,freq,nmedia,options,parw,parl,clow,chigh,rmaxkm)

system("bounce.exe coa")

thetas1,R = readbrc("coa.brc")

B1 = -10*log10( abs(R)**2 )

freq = 2000.0

wbounceenvfil("coa",case_title,freq,nmedia,options,parw,parl,clow,chigh,rmaxkm)

system("bounce.exe coa")

thetas2,R = readbrc("coa.brc")
B2 = -10*log10( abs(R)**2 )

print( 'Case (b)...' )

nfreqs = 101
freqs = linspace(0,2000,nfreqs)
freqs[0] = 2.0
thetamin =  5.0
thetamax = 85.0
nthetas = 101
thetas = linspace(thetamin,thetamax,nthetas)
B = zeros((nfreqs,nthetas))

for i in range(nfreqs):
    freqi = freqs[i]
    wbounceenvfil("coa",case_title,freqi,nmedia,options,parw,parl,clow,chigh,rmaxkm)
    system("bounce.exe coa")       
    thetasi,R = readbrc("coa.brc")
    Bi = -10*log10( abs(R)**2 )
    interpolator = interp1d(thetasi, Bi)
    B[i,:] = interpolator( thetas )
    
figure(1)
plot(thetas1,B1,thetas2,B2,'--')
xlabel('Grazing angle (deg)')
ylabel('Loss (dB)')
title('(a)')
ylim(0,25)
grid(True)

figure(2)
pcolor(thetas,freqs,B,shading='auto')
colorbar()
xlabel('Grazing angle (deg)')
ylabel('Frequency (Hz)')
title('(b)')
xlim(thetamin,thetamax)
ylim(0,2000)
clim(2,12)

show()

print("done")
