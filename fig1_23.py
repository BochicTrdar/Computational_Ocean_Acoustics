# Bottom loss curves

from numpy import * 
from matplotlib.pyplot import *
from bdryr import *

print('Bottom loss curves...') 

theta = linspace(90,0,181)
thetar = theta*pi/180.0
grazing_angle = 90 - theta
cw = 1500.0
cp = 1550.0
cs = 0.0
alphap = 0.5
alphas = 0.0
rhow = 1000.0
rhob = 2000.0

R = bdryr(rhow,rhob,cw,cp,cs,alphap,alphas,thetar)
B1 = -10*log10( abs(R)*abs(R) )

cp = 1600.0

R = bdryr(rhow,rhob,cw,cp,cs,alphap,alphas,thetar)
B2 = -10*log10( abs(R)*abs(R) )

cp = 1800.0

R = bdryr(rhow,rhob,cw,cp,cs,alphap,alphas,thetar)
B3 = -10*log10( abs(R)*abs(R) )

cp = 1600.0

alphap = 0.0

R = bdryr(rhow,rhob,cw,cp,cs,alphap,alphas,thetar)
B4 = -10*log10( abs(R)*abs(R) )

alphap = 0.5

R = bdryr(rhow,rhob,cw,cp,cs,alphap,alphas,thetar)
B5 = -10*log10( abs(R)*abs(R) )

alphap = 1.0

R = bdryr(rhow,rhob,cw,cp,cs,alphap,alphas,thetar)
B6 = -10*log10( abs(R)*abs(R) )

alphap = 0.5 

rhob = 1500.0

R = bdryr(rhow,rhob,cw,cp,cs,alphap,alphas,thetar)
B7 = -10*log10( abs(R)*abs(R) )

rhob = 2000.0

R = bdryr(rhow,rhob,cw,cp,cs,alphap,alphas,thetar)
B8 = -10*log10( abs(R)*abs(R) )

rhob = 2500.0

R = bdryr(rhow,rhob,cw,cp,cs,alphap,alphas,thetar)
B9 = -10*log10( abs(R)*abs(R) )

cp = 1600.0
alphap = 0.0
alphas = 0.0
rhob = 2000.0

cs = 0.0

R = bdryr(rhow,rhob,cw,cp,cs,alphap,alphas,thetar)
B10 = -10*log10( abs(R)*abs(R) )

cs = 200.0

R = bdryr(rhow,rhob,cw,cp,cs,alphap,alphas,thetar)
B11 = -10*log10( abs(R)*abs(R) )

cs = 400.0

R = bdryr(rhow,rhob,cw,cp,cs,alphap,alphas,thetar)
B12 = -10*log10( abs(R)*abs(R) )

cs = 600.0

R = bdryr(rhow,rhob,cw,cp,cs,alphap,alphas,thetar)
B13 = -10*log10( abs(R)*abs(R) )

figure(1)
plot(grazing_angle,B1,grazing_angle,B2,'--',grazing_angle,B3,'.')
grid(True)
xlabel('Grazing angle (degrees)')
ylabel('Loss (dB)')

figure(2)
plot(grazing_angle,B4,grazing_angle,B5,'--',grazing_angle,B6,'.')
grid(True)
xlabel('Grazing angle (degrees)')
ylabel('Loss (dB)')

figure(3)
plot(grazing_angle,B7,grazing_angle,B8,'--',grazing_angle,B9,'.')
grid(True)
xlabel('Grazing angle (degrees)')
ylabel('Loss (dB)')

figure(4)
plot(grazing_angle,B10,grazing_angle,B11,'--',
grazing_angle,B12,'.',grazing_angle,B13,'r')
grid(True)
xlabel('Grazing angle (degrees)')
ylabel('Loss (dB)')

show()

print("done.")
