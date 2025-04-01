#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

ILLUMINATION

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

 
iraf.imdel("ilumin", verify="no")
valorinicial = 2
iraf.illumination("skymedio", "ilumin", interactive="yes", nbins=5,
     bins="", function="legendre", order=valorinicial, low_reje=3, high_rej=3,
     niter=3, interpolator="poly3")

# aplicar corrección por iluminación
listagal_ff = iraf.hselect("ff_W*.fits", "$I", "OBJECT='NGC1068'",
                   Stdout=1)
listaest_ff = iraf.hselect("ff_W*.fits", "$I", "OBJECT='hd93521'",
                   Stdout=1)
listaall_ff = listagal_ff + listaest_ff
for im in listaall_ff:
    imout = "il"+im[2:]
    iraf.imdelete(imout, verify="no")
    iraf.imarith(im, "/", "ilumin", imout)
    
# generación gráficas antes y después corrección de "illumination" promediando filas
iraf.prows("bs"+listagal_ff[0][2:], 900, 1100)
# iraf.gki.printPlot()
# newest = max(glob.iglob('*.eps'), key=os.path.getctime)
# os.rename(newest, "espectro_antes_illum.eps")
# iraf.prows("il"+listagal_ff[0][2:], 900, 1100)
# iraf.gki.printPlot()
# newest = max(glob.iglob('*.eps'), key=os.path.getctime)
# os.rename(newest, "espectro_despues_illum.eps")

iraf.prows("il"+listagal_ff[0][2:], 900, 1100, append="yes")
iraf.gki.printPlot()
newest = max(glob.iglob('*.eps'), key=os.path.getctime)
os.rename(newest, "espectro_antesYdespues_illum.eps")