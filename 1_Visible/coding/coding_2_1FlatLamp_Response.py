#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

CORRECCIÓN FLATFIELD

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

# visualizar flat lamp mean
# iraf.display("Flat_lampara_medio", 1, zscale="yes", zrange="yes",
#              ztran="linear", fill="no")

# # RESPONSE
# carga de paquetes necesarios y ejecución de response
iraf.onedspec()
iraf.twodspec()
iraf.longslit()
iraf.imdelete("response", verify="no")
# valorinicial = 8
valorinicial = 40 # ajustado en la ventana con ":" "order 40" y ajustando con "f" y viendo residuos 
# con "j" o "k" (volver a vista inicial con "h")
iraf.response("Flat_lampara_medio", "Flat_lampara_medio[100:400,*]",
     "response", sample="*", function="legendre", order=valorinicial,
     low_rej=3, high_rej=3, niter=5, interactive="yes")

# generación gráficas response promediando en fila o columna
iraf.prows("response", 650, 1050)
iraf.gki.printPlot()
newest = max(glob.iglob('*.eps'), key=os.path.getctime)
os.rename(newest, "response_prows.eps")
iraf.pcols("response", 100, 400)
iraf.gki.printPlot()
newest = max(glob.iglob('*.eps'), key=os.path.getctime)
os.rename(newest, "response_pcols.eps")

# corrección de las imágenes de dividiendo por "response.fits"
listagal = iraf.hselect("bs_WHT*.fits", "$I", "OBJECT='NGC1068'", Stdout=1)
listasky = iraf.hselect("bs_WHT*.fits", "$I", "OBJECT='BLANK3'", Stdout=1)
listaest = iraf.hselect("bs_WHT*.fits", "$I", "OBJECT='hd93521'", Stdout=1)
listaarc = iraf.hselect("bs_WHT*.fits", "$I", "OBJECT='ARC BLUE'", Stdout=1)
# Unimos las listas. (Igualmente hubiéramos podido usar hselect con los
# "or" - las dos barras verticales - para crear una sola lista.)
listaall = listagal + listasky + listaest + listaarc
for im in listaall:
    imout = "ff"+im[2:]
    iraf.imdelete(imout, verify="no")
    iraf.imarith(im, "/", "response", imout)
