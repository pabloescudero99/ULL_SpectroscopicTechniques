#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Sustracción overscan con ccdproc, Flat Promedio

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

# :a 100, :c 250
# iraf.implot("WHT9911.fits")
# iraf.implot("WHT9899.fits")

# sección del overscan
# iraf.pcols("WHT9911", 100, 400, wx1=1800, wx2=2150)
# iraf.gki.printPlot()
# newest = max(glob.iglob('*.eps'), key=os.path.getctime)
# os.rename(newest, "biassec.eps")
# biassec: 2055 a 2095
# trimsec: 150 a 1870

# creacion lista flats y flats con prefijo bs_
listflat = iraf.hselect("W*.fits", "$I", "OBJECT?='FLAT'", Stdout=1)
listflat_bs = ["bs_"+s for s in listflat]

# aplicación ccdproc para quitar el overscan a los flats de lámpara
iraf.imdelete(",".join(listflat_bs), verify="no")
iraf.ccdproc(",".join(listflat), output=",".join(listflat_bs),
     overscan="yes", zerocor="yes", flatcor="no", readaxis="column",
     trim="yes", darkcor="no", fixpix="no", biassec="[*,2055:2095]",
     trimsec="[*,150:1870]", ccdtype="", function="legendre",
     order=1, zero="Biasmedio")

# comprobación de la estadística de los flats
for im in listflat_bs:
    iraf.imstat(im, fields="image,mean,stddev", format="no")

# cálculo del flat de lámpara promedio
iraf.imdelete("Flat_lampara_medio", verify="no")
iraf.flatcombine(",".join(listflat_bs), output="Flat_lampara_medio",
     combine="average", reject="avsigclip", ccdtype="",
     subsets="no", scale="none", process="no", delete="no")
# Es muy importante poner process=”no”, si no la tarea intenta procesar (restar bias+overscan, recortar 
# etc.) los flats antes de combinarlos, y abortaría con mensajes de error (relacionados con pasos que 
# se realizan en ccdproc).

# Análogaly con los flatsky, espectros, estrellas y arco:
# lista de todos los demás objects
listtodo = iraf.hselect("W*.fits", "$I",
    "OBJECT='BLANK3' ||  OBJECT='NGC1068' || \
     OBJECT='hd93521' ||  \
     OBJECT='ARC BLUE'",  Stdout=1)
# lista con los nombres con el prefijo bs_
listtodo_bs = ["bs_"+s for s in listtodo]
# eliminación del overscan
iraf.imdelete(",".join(listtodo_bs), verify="no")
iraf.ccdproc(",".join(listtodo), output=",".join(listtodo_bs),
     overscan="yes", zerocor="yes", flatcor="no", readaxis="column",
     darkcor="no", fixpix="no", biassec="[*,2055:2095]",
     trimsec="[*,150:1870]", ccdtype="", function="legendre",
     order=1, zero="Biasmedio")

# verificar si ha mejorado el espectro al sustraer el bias 2D
# iraf.prows("WHT9874",800, 1200, wy1=900, wy2=1100)
# iraf.gki.printPlot()
# newest = max(glob.iglob('*.eps'), key=os.path.getctime)
# os.rename(newest, "espectrodegalaxia_prows.eps")
# iraf.prows("bs_WHT9874",800, 1200, wy1=900, wy2=1100)
# iraf.gki.printPlot()
# newest = max(glob.iglob('*.eps'), key=os.path.getctime)
# os.rename(newest, "bs_espectrodegalaxia_prows.eps")
