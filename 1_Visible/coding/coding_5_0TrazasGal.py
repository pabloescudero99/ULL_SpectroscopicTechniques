#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

COMPROBACIÓN GALAXIAS

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

lista_il_galax = iraf.hselect("il_W*.fits", "$I", "OBJECT?='NGC'", Stdout=1)
y1 = 460
y2 = 1060
iraf.prows(lista_il_galax[0], y1, y2, wy1=0, wy2=150)
for ind in np.arange(1,len(lista_il_galax)):
    iraf.prows(lista_il_galax[ind], y1, y2, append="yes")
iraf.gki.printPlot()
newest = max(glob.iglob('*.eps'), key=os.path.getctime)
os.rename(newest, "trazas_galaxia.eps")
# En y1, y2 poner unos valores adecuados para un intervalo de unos
# 300-400 píxeles en la parte central del espectro.