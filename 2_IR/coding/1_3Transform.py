# -*- coding: utf-8 -*-
"""

Transform

"""
from pyraf import iraf
import os

dir_work = os.getcwd()+'\\..\\data'
os.chdir(dir_work)

# COMPROBAR calibración de la longitud de onda aplicándola a la imagen de solo
#cielo. 'dx' debe estar en torno a 6 A/pix
iraf.imdelete("oh_skylines_cal", verify="no")
iraf.transform("oh_skylines", "oh_skylines_cal", interpt="spline3", xlog="no",\
            ylog="no", flux="yes", database="database",fitname="oh_skylines")