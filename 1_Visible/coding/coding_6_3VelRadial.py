#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Corrección de Velocidad radial: rvcorrect

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt
import scipy.constants as ctes

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

# Corrección del movimiento del observador en la dirección del objeto observado:
# Rotación de la tierra sobre su propio eje, el movimiento de la tierra alrededor del 
# baricentro del sistema tierra-luna, y el movimiento de la tierra alrededor del sol
# Podemos además incluir una corrección más, correspondiente al movimiento del sol relativo 
# al sistema local de reposo

# Añadir cabecera de UT (si no la tiene)
iraf.hedit("NGC1068_final_skysub", "UT", "(UTOBS)", add="yes", show="yes", verify="no")

# aplicación de rvcorrect
iraf.astutil()
iraf.rvcorr(images="NGC1068_final_skysub")
# cuidado con que el observatorio sea el correcto. Se puede editar con:
iraf.astutil.observatory="lapalma"