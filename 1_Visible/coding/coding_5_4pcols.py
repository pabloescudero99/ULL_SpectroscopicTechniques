#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PCOLS

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

x1 = 240
x2 = 260
iraf.pcols("flujcal_WHT9874", x1, x2)
iraf.pcols("flujcal_WHT9876", x1, x2, append="yes")
iraf.pcols("flujcal_WHT9883", x1, x2, append="yes")
iraf.pcols("flujcal_WHT9887", x2, x2, append="yes")
# escoger para x1, x2 los valores adecuados para definir un intervalo
# de unos 20 píxeles alrededor de la posición del pico de continuo de
# la galaxia.
iraf.gki.printPlot()
newest = max(glob.iglob('*.eps'), key=os.path.getctime)
os.rename(newest, "trazas_gal_flujcal.eps")