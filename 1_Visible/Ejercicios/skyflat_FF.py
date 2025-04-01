#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ILLUMINATION
@author: pescudero
"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt
dir_work = '/home/pabloescudero99/Escritorio/TdE_Practicar/Ejercicios/' #input('Introduce el directorio de trabajo que se encuentre dentro de /scratch/pescudero/')
os.chdir(dir_work) # '/scratch/pescudero/TOB' + dir_work

# aplicación de illumination
iraf.imdel("ilumin_FF", verify="no")
valorinicial = 2
iraf.illumination("skyflat_FF", "ilumin_FF", interactive="yes", nbins=5, bins="",
 function="legendre", order=valorinicial, low_reje=3, high_rej=3,niter=3,
 interpolator="poly3")
