# -*- coding: utf-8 -*-

from scipy import constants

import math




def psuedorange(Tr,Ts):
	'''P->Pseudorango,the distance from the receiver antenna to the satellite antenna including receiver and satellite clock offsets (and other biases, such as atmospheric delays), Tr->reception time  measured by the receiver cloc,Ts->the signal transmission time measured by the satellite clock'''
	c=constants.c
	P=c(Tr-Ts)
	return P

def psuedorange2(p,Tr,Ts,Ir,Tr,Ep,):
	'''P->Pseudorango,the distance from the receiver antenna to the satellite antenna including receiver and satellite clock offsets (and other biases, such as atmospheric delays), Tr->reception time  measured by the receiver cloc,Ts->the signal transmission time measured by the satellite clock dtr,dts->satellite clock biases, Ir,Er-> the ionospheric and tropospheric delay, Ep-measurement error'''
	c=constants.c
	P=c(Tr-Ts)
	return P



def tropospheric_corrections(p==None,T,h,hrel,Elv):
'''where p is the total pressure (hPa), T is the absolute temperature (K) of the air, h is the geodetic height above MSL (mean sea level), e is the partial pressure (hPa) of water vapor and hrel is the relative humidity. The tropospheric delay s rT is expressed by the Saastamoinen model with p , T and e derived from the standard atmosphere'''
#Elv->Elevation of the satellite with respect to the receptor in radians
	

	if p==None:
		p=1013.25*((1-0.000022557*h)**5.2568)
		
	T=15-0.0065*h+273.15
	
	e=6.108*math.exp((17.15*T-4684)/(T-38.45))*hrel/100
	z=constants.pi-Elv
	Trs=(0.002277/math.cos(z))*(p+( 125/T + 0.05)*math.e-math(z)**2)
	return Trs
	
	
def broadcast_ionosphere_model_corrections(fi,lambda,elev,azimuth,tow,alfa(4),beta(4)):

# Inputs:                                                          *
#   fi            : Geodetic latitude of receiver          (deg)   *
#   lambda        : Geodetic longitude of receiver         (deg)   *
#   elev          : Elevation angle of satellite           (deg)   *
#   azimuth       : Geodetic azimuth of satellite          (deg)   *
#   tow           : Time of Week                           (sec)   *
#   alfa(4)       : The coefficients of a cubic equation           *
#                   representing the amplitude of the vertical     *
#                   dalay (4 coefficients - 8 bits each)           *
#   beta(4)       : The coefficients of a cubic equation           *
#                   representing the period of the model           *
#                   (4 coefficients - 8 bits each)                 *
# Output:                                                          *
#   dIon1         : Ionospheric slant range correction for         *
#                   the L1 frequency                       (metre) *

	c=constants.c				          #speed of light
	a = azimuth                          #asimuth in radians
	e = elev                             #elevation angle in radians
	psi = 0.0137 / (e+0.11) - 0.022      # Earth Centered angle
	lat_i = fi+ psi*cos(a)               # Subionospheric lat
	if (lat_i > 0.416):
		lat_i = 0.416
	elif(lat_i < -0.416):
		lat_i = -0.416

		                                  # % Subionospheric long
	long_i = lambda + (psi*sin(a)/cos(lat_i))
		                                  # % Geomagnetic latitude
	lat_m = lat_i + 0.064*cos((long_i-1.617)*semi2rad)
	t = 4.32e4*long_i + tow
	t = mod(t,86400.)                    #  Seconds of day
	if (t > 86400.):
		t = t - 86400

	else (t < 0.):
		t = t + 86400

	sF = 1. + 16.*(0.53-e)**3             #  Slant factor
		                                  #  Period of model
	PER = beta(1) + beta(2)*lat_m + beta(3)*lat_m^2 +beta(4)*lat_m^3
	if (PER < 72000.):
		PER = 72000
	
	x = 2.*pi*(t-50400.)/PER             # % Phase of the model
		                                  # % (Max at 14.00 =
		                                  # % 50400 sec local time)
		                                  # % Amplitud of the model
	AMP = alfa(1) + alfa(2)*lat_m + alfa(3)*lat_m^2 +alfa(4)*lat_m^3
	if(AMP < 0.)
		AMP = 0.
	end
		                                  # % Ionospheric corr.
	if(abs(x) > 1.57):
		dIon1 = sF * (5.e-9)
	else:
		dIon1 = sF * (5.e-9 + AMP*(1. - x*x/2. + x*x*x*x/24.))

	dIon1 = c*dIon1

	return dIon1




