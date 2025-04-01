# -*- coding: utf-8 -*-
"""

Continuum

"""
# sn05kl + BD402534
from pyraf import iraf
import os
import numpy as np

dir_work = os.getcwd()+'\\..\\data'
os.chdir(dir_work)

# Ajustamos continuo etselar. Ajuste estrella estandar por polinomio para eliminar absorcion. Hay q evitar 
#absorcion intrinseeca y telurica. Usamos continuum.
# Tomamos segmentos con la s de zonas sin absorcion. Orden bajo (3-4). Tramo alto (?) en la zona final 
#para q no se vuelva loco
#
iraf.imdelete("BD402534_cont", verify='no')
iraf.continuum("BD402534.0001.fits","BD402534_cont", type="fit",function="legendre",order=3,\
               low_reject=2,high_reject=0,niterate=2)