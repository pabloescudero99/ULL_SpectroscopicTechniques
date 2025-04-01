# -*- coding: utf-8 -*-
"""

Imcombine

"""
from pyraf import iraf
import os
import numpy as np

dir_work = os.getcwd()+'\\..\\data'
os.chdir(dir_work)

# Lista suprimiendo el primer flat ('valores de estadística raros')
lista_flats=iraf.hselect("tcr*.fits", "$I", \
    "IMAGETYP?='flat' && LIRSLNAM='l1' && LIRGRNAM?='lrzj' && $I!='tcr805285.fits'", Stdout=1)

# Combinación de flats
iraf.imdelete("flat_lrzj_sn", verify="no")
iraf.imcombine(",".join(lista_flats), "flat_lrzj_sn", combine="average", \
         scale="median",zero="none",reject="sigclip")