#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

FITPROFS

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt
import scipy.constants as ctes

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

# os.system ejecuta un comando de la shell de Linux, en este caso echo
# imprime los datos dentro de las comillas simples, y el ">" redirige
# la salida al fichero indicado.
#                lambda   flujo    g=gaussiana   ~2*fwhm
os.system("echo '4881.67   3724   g            3.032'  > 'galaxia_hb.dat'")
# medir con splot del espectro final sustraído del cielo. Línea 242. Clickar con 'a' a la izquierda 
# y derecha para hacer zoom en la línea correspondiente. Después, hacer lo mismo clickando en 'k' en
# en ambos lados para realizar un ajuste gaussiano de forma que se indican los parámetros de lambda,
# flujo y FWHM
iraf.delete("NGC1068_final.log", verify="no")
iraf.fitprofs("NGC1068_final_skysub", dispaxis=2, region="4870 4894",
     lines="160-335", positions="galaxia_hb.dat", fitbackground="yes", profile="gaussian",
     nerrsample=0, sigma0=5.0, invgain=1.0, verbose="no", nsum=3,
     output="", option="fit", logfile="NGC1068_final.log",
     Stdout="NGC1068_final.out")
# region es el rango en lambda donde se hace el ajuste. Debe ser lo suficientemente amplio para incluir una buena zona del background en ambos lados de la linea, teniendo en cuenta también su desplazamiento por la rotación de la galaxia, pero no tan grande porque por un lado podrían entrar otras líneas de emisión, por el otro el ajuste lineal dejaría de ser válido. Reemplazar r1, r2 con unos valores unos 12-15 píxeles por cada lado el valor inicial (fwhmc). 
# lines es el intervalo en X (fuera de este rango espacial no hay emisión en Hbeta). Los valores más adecuados para x1 y x2 incluyen toda la emisión visible, pero no deben extenderse más allá.
# nerrsample=0 significa que no queremos calcular los errores del ajuste (si no se complicaría el formato de salida y sería más difícil leerlo con numpy).
# con fitbackground=”yes” ajustamos al mismo tiempo línea y continuum (con fitbackground=”no” igualmente se hace un ajuste del continuum, pero más rápido y menos preciso).
# con nsum=3 se suman 3 cortes espaciales: por ejemplo a X=200 se hace el ajuste de la suma de X=199,200,201; luego a X=201 se ajusta la suma de X=200,201,202 etc,. Así aumentamos un poco la relación señal/ruido a costa de perder algo de resolución espacial.
# Se puede probar con nsum=1, nsum=3, nsum=5 para ver como quedan las curvas de flujo y de rotación.
# output=”” significa que no queremos ninguna imagen de salida (la tarea puede producir una imagen con los ajustes o una con los residuos).
# logfile es el fichero donde se guardan los resultados del ajuste.
# Stdout=”NGC1068_final.out”: recordamos que no es un parámetro de la tarea sino el mecanismo de PyRAF para capturar la salida de la tarea en un fichero; si todo ha ido bien el fichero debería estar vacío.

