# -*- coding: utf-8 -*-
"""

Identify

"""
from pyraf import iraf
import os

dir_work = os.getcwd()+'\\..\\data'
os.chdir(dir_work)

iraf.identify("oh_skylines", section="", coordlist="lirisdr$std/ohlines.dat",
       match=-3., maxfeat=20, zwidth=1500, fwidth=4.0, cradius="5.",
       minsep=2.0, function="legendre", order=4, low_rej=3.0, high_rej=3.0)
# Some useful shortkeys within identify are “w + e + e” - to zoom in, “w + a”
# to zoom out; “z” can be used for zoom a window of size “zwidth”; “m” to mark
# a line; “f” to fit; “:function FUNCTION” to change the function; “:order N” 
# to change the order. After pressing f for fitting the function, the following
# graphical representations can be obtained h for the fit; “j” for the 
# residuals; “k” for the ratio between data and fit; “l” for the non-lineal 
# part of the fit. 

# Eliminar puntos que se desvíen mucho en los residuos, jugar con el orden
#de la función de ajuste
# The GOAL is to achieve a RMS of the order of 10% of the spectral dispersion 
# (:show when running identify) the smaller the RMS, the better, but in many 
# cases a value around 33% could be enough.