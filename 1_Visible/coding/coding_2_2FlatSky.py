#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

FLAT SKY, ILLUMINATION

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

# lista nombre espectros corregidos de flatlamp
listsky_ff = iraf.hselect("ff_W*.fits", "$I", "OBJECT='BLANK3'",
              Stdout=1)
for im in listsky_ff:
    iraf.imstat(im+"[20:480,20:1700]", fields="image,mean,stddev",
                format="no")
# crear flat sky medio
iraf.imdelete("skymedio")
iraf.imcombine(",".join(listsky_ff[1:]), "skymedio", combine="average",
      reject="avsigclip", scale="mode", statsec="[20:480,20:1700]")

# visualización
# iraf.display("skymedio", 1)