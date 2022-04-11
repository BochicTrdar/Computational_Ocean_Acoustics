# Monostatic backscattering strength at the bottom as a function of bottom type. 
# The APL-UW model at 30 kHz
# Data from APL-UW High-Frequency Ocean Environmental Acoustic Models Handbook (pages 145-147)

from numpy import *
from scipy.io import *
from matplotlib.pyplot import *

datarr  = loadtxt('roughrock.txt')   ; strength_rr  = datarr[ :,4]
datar   = loadtxt('rock.txt')        ; strength_r   = datar[  :,4]
datacs  = loadtxt('coarsesand.txt')  ; strength_cs  = datacs[ :,4]
datavfs = loadtxt('veryfinesand.txt'); strength_vfs = datavfs[:,4] # Last value at 10 kHz is correct?
datas   = loadtxt('siltsigma2a.txt') ; strength_s   = datas[  :,4] # sigma2 = 0.001

thelegend = [r'Lambert$_{-29dB}$', 'Rough rock', 'Rock', 'Gravel', 'Coarse sand', 'Very Fine sand', 'Silt']
istyle = ['k--','b-.','k','g','r-.','k','g--']
ids = [-5,5,5,3,5,-4,0]

thetas =  array([1, 2, 3, 5, 7, 10, 20, 40, 60, 70, 80, 85, 88, 89, 90]) # in degrees
frequencies = array([10.0,15.0,20.0,25.0,30.0,40.0,60.0,80.0,100.0]) # in kHz

#Lambert's Law and -29dB for bottom
strength_lambert = -29 + 10*log10( ( sin(thetas*pi/180.0) )**2 )

figure(1)
plot(thetas,strength_lambert,istyle[0],linewidth=2)
text(thetas[8],strength_lambert[8]+ids[0],thelegend[0],fontsize=18)
plot(thetas,strength_rr,istyle[1],linewidth=2)
text(thetas[5],strength_rr[5]+ids[1],thelegend[1],fontsize=18)
plot(thetas,strength_r,istyle[2],linewidth=2)
text(thetas[5],strength_r[5]+ids[2],thelegend[2],fontsize=18)
plot(thetas,strength_cs,istyle[4],linewidth=2)
text(thetas[7],strength_cs[7]+ids[4],thelegend[4],fontsize=18)
plot(thetas,strength_vfs,istyle[5],linewidth=2)
text(thetas[7],strength_vfs[7]+ids[5],thelegend[5],fontsize=18)
plot(thetas,strength_s,istyle[6],linewidth=2)
text(thetas[9],strength_s[9]+ids[6],thelegend[6],fontsize=18)
xlabel('Grazing Angle (deg)')
ylabel('Scattering Strength (dB)')
title('APL-UW model - 30 kHz')
xlim( 0, 90)
ylim(-60,10)
grid(True)

show()

print( "done." )
