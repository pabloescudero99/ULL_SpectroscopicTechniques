#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Estimación del rango espectral

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

# buscar keyword de longitudondacentral,dispersion, tamañopixel y binningenYen 
# cualquier cabecera 
iraf.imheader("WHT9874.fits", long="yes")
# obtenemos los valores de dichas keywords
iraf.hselect("W*.fits", "$I, CENWAVE, DISPERSI, \
             CCDYPIXE, CCDYBIN", "yes")
# miramos el número de pixeles en Y de las imágenes corregidas. Se indica junto
# al nombre de la imagen como [NpixX, NpixY]
iraf.imheader("il_WHT9874.fits", long="no")

# CÁLCULOS : Dispersion = "DISPERSI"[A/mm] * ("CCDYBIN" * "CCDYPIXE"[mm/pix]) * NpixY[pix]
# rango espectral = "CENWAVE" +- Dispersion / 2

# 
iraf.pcols("WHT9899.fits", 240, 260)
# Poner en lugar de x1, x2 unos valores adecuado para promediar
# una 20 líneas en la zona central del espectro.
iraf.gki.printPlot()
newest = max(glob.iglob('*.eps'), key=os.path.getctime)
os.rename(newest, "arco.eps")

# Uso de "splot" que es la función análoga a "imexam" para espectros
# seleccionar "along columns"(2) y número pixel medio 250
iraf.splot("WHT9899.fits")