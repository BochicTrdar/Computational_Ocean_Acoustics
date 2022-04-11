# Convergence-zone propagation in the eastern North Atlantic
# (a) Typical double-duct profile and associated ray diagram 
# showing that the deepcycling paths refocus near the surface 
# every 65 km
# (b) Computed transmission loss at a frequency of 200 Hz

from os import *
import sys
from numpy import * 
from matplotlib.pyplot import *
from scipy.interpolate import *
from wbellhopenvfil import *
from wkrakenenvfil import *
from plotray import *
from readshd import *

print('Convergence-zone propagation') 

#################### Bellhop ##############################

print( "Running Bellhop for the calculation of rays..." )

Dmax = 5000.0
z0 = array([0.0,300.0,1200.0,2000.0,Dmax])
c0 = array([1522.0,1501.0,1514.0,1496.0,1545.0])

nz = 101
z1 = linspace(0,Dmax,21)
z  = linspace(0,Dmax,nz)
lineari = interp1d(z0,c0)
c1 = lineari( z1 )
splinei = splrep(z1,c1,s=0)
c = splev(z,splinei,der=0)

case_title = 'Bellhop convergence-zone propagation'

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
zs   = array([20.0])
rs   = array([ 0.0])
zbox = 5001.0 
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

rmaxkm = 250.0
rarray = linspace(0,rmaxkm*1000,501)
zarray = array([50.0])
rarray[0] = 1.0
rarraykm = rarray/1000.0
nza = zarray.size
nra = rarray.size

tlsph = 20*log10( rarray )

options = {"options1":options1,"options2":options2,"options3":options3,"options4":options4,"rarray":rarraykm,"zarray":zarray}

wbellhopenvfil('coa',case_title,source_data,surface_data,ssp_data,bottom_data,options)

system("bellhop.exe coa")

#################### KRAKEN ##############################

print( "Running KRAKEN for the calculation of TL..." )

#==================================================================
#  
#  Source data
#  
#==================================================================

source_data = {"zs":zs, "f":freq}

#==================================================================
#  
#  Surface data
#  
#==================================================================

bc = 'V'
properties = [] # Not required (vacuum over surface)
reflection = [] # Not required for this case

surface_data = {"bc":bc,"properties":properties,"reflection":reflection}

#==================================================================
#  
#  Scatter data
#  
#==================================================================

# Scatter is not required for this case: 
bumden = [] # Bump density in ridges/km 
eta    = [] # Principal radius 1 of bump 
xi     = [] # Principal radius 2 of bump 

scatter_data= {"bumden":bumden,"eta":eta,"xi":xi}

#==================================================================
#  
#  Sound speed data
#  
#==================================================================

cs = zeros(nz)
rho = ones(nz)
apt = cs
ast = cs
type  = 'H'
itype = 'N'
# Number of mesh points to use initially, should be about 10 per vertical wavelenght:
nmesh = 10001
sigma = 0.0 # RMS roughness at the surface 
clow  = 0.0
chigh = 1.0e4

cdata = array([z,c,cs,rho,apt,ast])

ssp_data = {"cdata":cdata,"type":type,"itype":itype,"nmesh":nmesh,"sigma":sigma,"clow":clow,"chigh":chigh,"zbottom":Dmax}

#==================================================================
#  
#  Bottom data
#  
#==================================================================

layerp     = array([0, 0, Dmax])
layert     = 'R'
properties = array([Dmax,2000.0,0.0,2.0,0.5,0.0])
bdata      = [];
units      = 'W';
bc	   = 'A';
sigma      = 0.0 # Interfacial roughness

bottom_data = {"n":1,"layerp":layerp,"layert":layert,"properties":properties,"bdata":bdata,"units":units,"bc":bc,"sigma":sigma}

#==================================================================
#  
#  Field data
#  
#==================================================================

rp    =   0 
np    =   1
m     =   120
rmodes = 'A'
stype  = 'R'
thorpe = ' '
finder = ' '
dr     = zeros( nra )

field_data = {"rmax":rmaxkm,"nrr":nra,"rr":rarraykm,"rp":rp,"np":np,"m":m,"rmodes":rmodes,"stype":stype,"thorpe":thorpe,"finder":finder,"rd":zarray,"dr":dr,"nrd":nza}

wkrakenenvfil('coa',case_title,source_data,surface_data,scatter_data,ssp_data, bottom_data,field_data);

system("kraken.exe coa")
system("cp field.flp coa.flp")
system("field.exe coa < coa.flp")

print( "Reading output data..." )

filename = 'coa.shd'
xs = nan
ys = nan
pressure,geometry = readshd(filename,xs,ys)

p = squeeze( pressure )
tl = -20*log10( abs( p ) )

figure(1)
plot(c0,-z0,'o',c,-z)
xlabel('Sound Speed (m/s)')
ylabel('Depth (m)')
grid(True)

figure(2)
plotray('coa.ray')
grid(True)

figure(3)
plot(rarraykm,tlsph,'--',rarraykm,tl)
xlabel('Range (km)')
ylabel('Loss (dB)')
ylim(140,60)
grid(True)

show()

print("done.")
