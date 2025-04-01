#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

Sensfunc

"""
# sn05kl + BD402534
from pyraf import iraf
import os
import numpy as np

dir_work = os.getcwd()+'\\..\\data'
os.chdir(dir_work)

# Cambiar el orden a 4 para que log flux sea mas recto y para q sensivity residuals sea menor
iraf.unlearn('sensfunc')
iraf.imdelete("sens_cont*", verify='no')
iraf.sensfunc("std_cont", "sens_cont", ignoreap="no", logfile="logfile",\
              newexti="", functio="spline3", order=3, interactive="yes",\
              graphs="slr", marks="plus cross box", colors="2 1 3 4")