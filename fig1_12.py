# Deep-sound-channel propagation in the Norwegian Sea.
# For a source at the channel axis (500 m), the ray diagram
# shows that sound leaving the source within +/- 10 degrees
# aperture propagates to long range without boundary interaction

from os import *
import sys
from numpy import * 
from matplotlib.pyplot import *
from scipy.interpolate import *
from wbellhopenvfil import *
from plotray import *

print('Deep-Sound-Channel Propagation') 

sspdata = loadtxt("norwegian.ssp")

z = sspdata[:,0]; Dmax = max( z )
c = sspdata[:,1]

#################### Bellhop ##############################

print( "Running Bellhop for the calculation of rays..." )

case_title = 'Deep-Sound-Channel Propagation'

freq = 200.0 # frequency in Hz

source_nrays =  41   # number of propagation rays considered #
source_aperture = 10.0 # maximum launching angle (degrees) #
source_ray_step =  5.0 # ray calculation step (meters) #

#==================================================================
#  
#  Source properties 
#  
#==================================================================

nzs  = 1
zs   = array([500.0])
rs   = array([  0.0])
zbox = 4001.0 
rbox = 250.0  # km!!!!!
box  = array([source_ray_step,zbox,rbox])
thetas = array([source_nrays,-source_aperture,source_aperture]) 
p      = zeros(1)
comp   = ''

source_data = {"zs":zs, "box":box, "f":freq, "thetas":thetas, "p":p, "comp":comp}

#==================================================================
#  
#  Surface definition:
#  
#==================================================================

itype = ''
xati  = []  # The *.ati file won't be written  
p     = []  # Surface properties
aunits= ''

surface_data = {"itype":itype,"x":xati,"p":p,"units":aunits}

#==================================================================
#  
#  Sound speed:
#  
#==================================================================

r = []

ssp_data = {"r":r,"z":z,"c":c}

#==================================================================
#  
#  Bottom:
#  
#==================================================================

itype  = ''
bunits = '''W'''
xbty   = [] # Bottom coordinates
p      = array([2000.0,0.0,2.0,0.5,0.0]) # Bottom properties

bottom_data = {"itype":itype,"x":xbty,"p":p,"units":bunits}

#==================================================================
#  
#  Array: 
#  
#==================================================================

options1    = '''CVW''' # No ati file expected  
options2    = '''A '''  # No bty file expected
options3    = '''R''' # Rays 
options4    = []

rarray = array([0.0])
zarray = array([0.0])
rarraykm = rarray/1000.0

options = {"options1":options1,"options2":options2,"options3":options3,"options4":options4,"rarray":rarraykm,"zarray":zarray}

wbellhopenvfil('coa',case_title,source_data,surface_data,ssp_data,bottom_data,options)

system("bellhop.exe coa")

figure(1)
plot(c,-z)
xlabel('Sound Speed (m/s)')
ylabel('Depth (m)')
title('Norwegian Sea - SSP')
grid(True)

figure(2)
plotray('coa.ray')
xlabel('Range (m)')
ylabel('Depth (m)')
ylim(-4000,0)
grid(True)

show()

print("done.")
