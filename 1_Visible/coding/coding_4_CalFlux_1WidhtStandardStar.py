#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PROWS/IMEXAMIN

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

# estimamos la anchura del espectro de la estrella
# iraf.display("lamcal_WHT9958", 1, zran="yes", zsca="yes", ztran="log")
# escoger y1, y2 para promediar unas 500 líneas en la zona central
# del espectro
y1 = 611
y2 = 1111
wx_min = 110
wx_max = 390
# Restringimos el intervalo en X (wx_min, wx_max) para
# visualizar mejor la señal de la estrella. Este intervalo debe estar
# centrado en el pico de emisión de la estrella, y un ancho de uno
# 120-140 píxeles.
iraf.prows("lamcal_WHT9958", y1, y2, wx1=wx_min, wx2=wx_max)
iraf.gki.printPlot()
newest = max(glob.iglob('*.eps'), key=os.path.getctime)
os.rename(newest, "estandar_prows.eps")

# ALTERNATIVA con IMEXAMIN
# iraf.display("lamcal_WHT9958", 1, zran="yes", zsca="yes", ztran="log")
# iraf.jimexam.naverage=20     # promediamos 20 líneas
# iraf.jimexam.rplot=16        # plotting radius
# iraf.jimexam.sigma=5         # initial sigma
# iraf.jimexam.width=10        # background width (pixels)
# iraf.imexamin()              # lanzamos imexamin
# ponemos con el cursor aproximadamente sobre el centro de la traza, y 
# clickamos "j" para obtener la FWHM. Determinamos la anchura de la traza de la estrella
# como 2.5 o 3 veces el valor de la FWHM.
