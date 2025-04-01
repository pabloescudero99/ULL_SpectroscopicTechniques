#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

TAREA REIDENTIFY

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

# se recomienda no poner la extensión ".fits" en el nombre
iraf.reidentify("bs_WHT9899", "bs_WHT9899", section="middle col",
     newaps="yes", override="yes", refit="yes", trace="yes", nlost=3,
     coordlist="linelists$cuar.dat", nsum=20, step=20,
     database="database", interactive="no", verbose="yes")