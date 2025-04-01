#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

DISPLAY

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

iraf.display("il_WHT9874", 1, zscale="yes", zran="yes", ztran="log")
iraf.display("il_WHT9876", 2, zscale="yes", zran="yes", ztran="log")
iraf.display("il_WHT9878", 3, zscale="yes", zran="yes", ztran="log")
iraf.display("il_WHT9887", 4, zscale="yes", zran="yes", ztran="log")