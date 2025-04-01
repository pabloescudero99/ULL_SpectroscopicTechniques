#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

TAREA IDENTIFY

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

valorinicial = 3 # arbitrario. se sugiere 3 o 4
# se recomienda no poner la extensión ".fits" en el nombre
iraf.identify("bs_WHT9899", section="middle col",
     coordlist="linelists$cuar.dat", nsum=20, fwidth=10.0, cradius=6.,
     threshold=200, function="legendre", order=valorinicial,
     database="database", zwidth=400, maxfeatures=100)
# Calibrar señalando los picos, pulsando en "m" e indicando los valores de lambda
# utilizando los espectros de referencia del archivo "ING-Atlas...pdf"
# Clickando en "l" termina de autocalibrar los restantes. Después, hacer click
# en "f" para realizar el ajuste. Se tiene que obtener un RMS<0.1 Si esto no sucede 
# se tiene que aumentar el orden del ajuste a 4 (ya que valorinicial=3) El orden
# se cambia pulsando en ":" y escribiendo "order 4". Se tiene que pulsar de
# nuevo en "f". Se sale pulsando en "q" dos veces y en la terminal indicando "yes"
# para guardar.

# para visualizar la tabla generada emplear:
#iraf.type("linelists$cuar.dat")
#iraf.page("linelists$cuar.dat")