#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Promedios espectrogalaxia y bias_espectrogalaxia
Created on Thu Feb  1 15:48:49 2024

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

# Gráficos de promedio de filas y columnas de un espectro de la galaxia
iraf.prows("WHT9874.fits", 800, 1200)
iraf.gki.printPlot()
newest = max(glob.iglob('*.eps'), key=os.path.getctime)
os.rename(newest, "espectrodegalaxia_prows.eps")
#
iraf.pcols("WHT9874.fits", 100, 400)
iraf.gki.printPlot()
newest = max(glob.iglob('*.eps'), key=os.path.getctime)
os.rename(newest, "espectrodegalaxia_pcols.eps")

# representación del promedio de columnas del espectro junto con el promedio 
# del bias medio
iraf.prows("WHT9874",800, 1200, wy1=900, wy2=1100)
iraf.prows("Biasmedio", 800, 1200, append="yes")
iraf.gki.printPlot()
newest = max(glob.iglob('*.eps'), key=os.path.getctime)
os.rename(newest, "comparacion_Bias_espectrodegalaxia.eps")
# SE CONFIRMA QUE ES OPORTUNO SUSTRAER EL BIAS 2D