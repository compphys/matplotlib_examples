#!/usr/bin/env python

import sys
from numpy import *
from pylab import *
from utils.utils import load
from utils.interpolate import spline

au2ev=27.2114
c=137.036

data = load('cu-phthalo.dat')

freqshift=10.4

freq=data[:,0]
alpha_cat=(data[:,1])/3
alpha_rad=(data[:,2])/3
alpha_ani=(data[:,3])/3

sigma_cat=4*pi/c*freq*alpha_cat
sigma_rad=4*pi/c*freq*alpha_rad
sigma_ani=4*pi/c*freq*alpha_ani

freq=freq*au2ev+freqshift
x1=284.2; x2=5.6
y1=0; y2=7.4

figure(1, figsize=(8,12))

#========================================================================
h1=subplot(3,1,1)

setp(h1,xlim=(x1,x1+x2),ylim=(y1,y2),yticks=[0,2,4,6])

xi,yi = spline(freq,sigma_cat,1000)
plot(xi,yi,'b-',freq, sigma_cat, 'ko',linewidth=2.0,markersize=3.0)

peaks=[['A',284.6,2.1],['B',285.3,6.0],['C',285.8,1.4],['D',286.45,4.0],
       ['E',286.9,1.7],['F',287.7,2.1]]
for p in peaks:
    text(p[1],p[2],p[0],size=12)
text(0.04,0.85,'cation',size=12,transform=h1.transAxes)

xlabel('Photon energy [eV]',size=12)
ylabel(r'$\sigma_{zz}(\omega)$ [a.u.]',size=12)

#========================================================================
h2=subplot(3,1,2)
setp(h2,xlim=(x1,x1+x2),ylim=(y1,y2),yticks=[0,2,4,6])

xi,yi = spline(freq,sigma_rad,1000)
plot(xi,yi,'k-',freq, sigma_rad, 'ko',linewidth=2.0,markersize=3.0)

peaks=[['A',284.79,2.45],['B',285.4,6.1],['C',285.9,1.3],\
           ['D',286.25,3.7],['E',286.8,1.2],['F',287.75,1.7]]
for p in peaks:
    text(p[1],p[2],p[0],size=12)
text(0.04,0.85,'radical',size=12,transform=h2.transAxes)

xlabel('Photon energy [eV]',size=12)
ylabel(r'$\sigma_{zz}(\omega)$ [a.u.]',size=12)

#========================================================================
h3=subplot(3,1,3)
setp(h3,xlim=(x1,x1+x2),ylim=(y1,y2),yticks=[0,2,4,6])

xi,yi = spline(freq,sigma_ani,1000)
plot(xi,yi,'r-',freq, sigma_ani, 'ko',linewidth=2.0,markersize=3.0)

peaks=[['A',284.7,2.1],['B1',285.2,5.5],['B2',285.5,5.5],\
           ['D',286.15,3.25],['E',287.0,1.0],['F',287.9,1.4]]
for p in peaks:
    text(p[1],p[2],p[0],size=12)
text(0.04,0.85,'anion',size=12,transform=h3.transAxes)

xlabel('Photon energy [eV]',size=12)
ylabel(r'$\sigma_{zz}(\omega)$ [a.u.]',size=12)

savefig('cu-phthalo.pdf')
