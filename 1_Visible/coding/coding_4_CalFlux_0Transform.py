#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

TRANSFORM

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

# 
iraf.imdelete("lamcal_WHT9958", verify="no")
iraf.transform("il_WHT9958", "lamcal_WHT9958",
      "bs_WHT9899", interptype="poly3", flux="yes")
# dy =     0.2117

# análogaly para los espectros de las galaxias
lista_il = iraf.hselect("il_W*.fits", "$I", "yes", Stdout=1)
for im in lista_il:
    # print(im[0:2])
    iraf.imdelete("lamcal_"+im[3:10], verify="no")
    iraf.transform(im, "lamcal_"+im[3:10],
          "bs_WHT9899", interptype="poly3", flux="yes")