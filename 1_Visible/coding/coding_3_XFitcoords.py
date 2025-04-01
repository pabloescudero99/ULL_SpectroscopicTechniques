#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

FITCOORDS

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

valxorder = 4 #3
valyorder = 5 #3
iraf.fitcoords("bs_WHT9899", interactive="yes", combine="no",
     database="database", function="legendre", xorder=valxorder,
     yorder=valyorder)
# para valxorder valyorder, empezar de un valor pequeño, por ejemplo
# 3, y subirlos si vemos que el ajuste no es bueno.
# fitcoords permite combinar los resultados de varios espectros de
# calibración. En este caso sólo tenemos uno y ponemos combine=no.

# Al terminar la tarea nos imprime los valores de lambda en las 4 esquinas del espectro.
# Es importante comprobar que los valores sean consistentes entre ellos, en particular 
# las lambda correspondientes al mismo valor de Y deben diferir de muy poco (como mucho
# algunas décimas de Amgstrom).