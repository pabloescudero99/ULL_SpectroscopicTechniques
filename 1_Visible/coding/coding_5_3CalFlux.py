#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

CALIBRACIÓN FLUJO

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

lista_galax = iraf.hselect("lamcal_W*.fits", "$I", "OBJECT?='NGC'", Stdout=1)
# for gal in lista_galax:
#     iraf.setairmass(gal[:14], observatory="lapalma", intype="beginning",
#          outtype="effective", ut="UTOBS", update="yes")
    
# aplicación calibrate
iraf.calibrate.extinction="EXTINCTION/wlext.dat"
iraf.calibrate.observatory="lapalma"
iraf.calibrate.sensitivity="sens_hd93521"
# Sustituimos a nombreestrella el mismo valor que utilizamos en
# la calibración en flujo.
for gal in lista_galax:
    iraf.imdelete("flujcal"+gal[6:14], verify="no")
    iraf.calibrate(gal[:14], "flujcal"+gal[6:14], extinct="yes", flux="yes",
         ignoreaps="yes")
    iraf.imarith("flujcal"+gal[6:14], "*", 1e18, "flujcal"+gal[6:14])
# La tarea automáticamente lee airmass y exptime de la cabecera del
# espectro