#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

EJE ESPECTRAL

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

# añadir a cabecera el eje espectral, como "DISPAXIS", usando "hedit"
lista_bs = iraf.hselect("bs_W*.fits", "$I", "yes", Stdout=1)
for im in lista_bs:
    iraf.hedit(im, "DISPAXIS", 2, add="yes", show="yes", verify="no")
iraf.hedit("Flat_lampara_medio", "DISPAXIS", 2, add="yes", show="yes",
     verify="no")
# DISPAXIS=2 ya que en eje espectral es el Y (sería DISPAXIS=1 si
# el eje espectral fuera el X).