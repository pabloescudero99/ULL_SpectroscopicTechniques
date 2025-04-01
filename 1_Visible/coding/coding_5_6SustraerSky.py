#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Sustracción cielo

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

# sustracción de cielo
iraf.imdelete("NGC1068_final_skysub", verify="no")
iraf.background("NGC1068_final", "NGC1068_final_skysub", axis=1,
     interactive="yes", sample="20:80,420:490", naverage=1,
     function="legendre", order=2, low_rej=3.0, high_rej=3.0,
     niterate=3)
# dos intervalos de unos 60-80 píxeles a cada lado del objeto, en la zona donde el nivel del 
# cielo es más o menos plano.
# order=2 significa que ajustamos una recta. Tal vez pueda ser más apropiado order=3. Se ha probado
# con order3 pero sale un patrón de rayas horizontales tras la sustracción 
# (ver NGC1068_final_skysub_order3).
# Con low_rej e high_rej rechazamos los píxeles que desvíen más de tres sigmas del ajuste, y
# lo repetimos niterate veces.
# ajuste es mejor partir de la línea 300 o por allí, ya que las primeras lineas están cerca 
# del borde y pueden tener gradientes espaciales anómalos en en nivel de cielo