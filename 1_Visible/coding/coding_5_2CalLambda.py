#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

CALIBRACIÓN LONG ONDA

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

lista_il_galax = iraf.hselect("il_W*.fits", "$I", "OBJECT?='NGC'", Stdout=1)
for im in lista_il_galax:
    iraf.imdelete("lamcal"+im[2:10], verify="no")
    iraf.transform(im[:10], "lamcal"+im[2:10], "bs_WHT9899", interptype="poly3",
         flux="yes")
# flux="yes": conservamos el flujo
# interptype=poly3: algoritmo de interpolación.
# Los demás parámetros de dejan con su valor por defecto. Nos saldrá un
# espectro con el mismo numero de píxeles y paso constante en lambda.