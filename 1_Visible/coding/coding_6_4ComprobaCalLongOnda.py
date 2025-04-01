#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Comprobación calibración longitud de onda

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt
import scipy.constants as ctes

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

# 
# iraf.imdelete("lamcal_espectroarco", verify="no")
# iraf.transform("bs_espectroarco", "lamcal_espectroarco", "bs_espectroarco", interptype="poly3",
#                flux="yes")
# iraf.display("lamcal_espectroarco", 1, zsca="yes", zran="yes", ztran="log")

# Escribimos los parámetros iniciales en un fichero
#                lambda   flujo   gaussiana   fwhm
# os.system("echo 'lambdac   flujoc   g         fwhmc'  > 'arco_4880.dat'")
# lambdac, flujoc, fwhmc tienen el mismo significado que en el fitprof
# de la galaxia, excepto que aquí el fwhmc es el valor medido, ya que
# la líneas del arco no se desplazan por efecto doppler.
# Lanzamos el ajuste
# iraf.fitprofs("lamcal_espectroarco", lines="", dispaxis=2, region="r1 r2",
#      positions="arco_4880.dat", fitbackground="yes", profile="gaussian",
#      nerrsample=0, sigma0=5.0, invgain=1.0, verbose="no",
#      nsum=5, output="", option="fit", logfile="fitprofs_arco.log",
#      Stdout="result_arco.dat")
# Aquí, lines="" significa usa todo el rango espacial.

# # Leemos el fichero
# centro, fwhm = numpy.loadtxt("fitprofs_arco.log", unpack=True, usecols=(0,5))
# linea = range(1,len(centro)+1)
# #
# # Pintamos el centro
# plt.clf()
# plt.ylim(y1, y2)
# # Poner para y1 e y2 unos valores adecuados, se puede empezar usando los
# # valores de r1 y r2 utilizados en el ajuste, y luego modificarlos
# # dependiendo del resultado observado.
# plt.plot(linea, centro, 'o', markersize=2)
# #
# # Pintamos una línea horizontal como referencia
# plt.axhline(y=lambdac)
# # sustituir lambdac por el valor medido para este línea del arco.
# plt.title("Longitud de onda en funcion de X")
# plt.savefig("centro_arco.png")
# #
# # Pintamos ahora la fwhm
# plt.clf()
# plt.ylim(0, y2)
# # Para y2 podemos utilizar un valor relativamente grande, por ejemplo
# # 5, y luego ajustarlos.
# plt.plot(linea, fwhm, 'o', markersize=2)
# #
# # Pintamos una línea horizontal como referencia
# plt.axhline(y=0.46)
# plt.title("FWHM (A) en funcion de X")
# plt.savefig("fwhm_arco.png")