# -*- coding: utf-8 -*-
"""

Calibrate

"""
# sn05kl + BD402534
from pyraf import iraf
import os
import numpy as np

dir_work = os.getcwd()+'\\..\\data'
os.chdir(dir_work)

iraf.delete("BD402534_cal*", verify="no")
iraf.calibrate("BD402534.0001", "BD402534_cal", extinct="no", flux="yes",\
               ignorea="no", sensiti="sens_cont", fnu="no")

iraf.delete("sn05kl_cal*", verify="no")
iraf.calibrate("sn05kl.0001", "sn05kl_cal", extinct="no", flux="yes",\
               ignorea="no", sensiti="sens_cont", fnu="no")