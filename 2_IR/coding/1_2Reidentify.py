# -*- coding: utf-8 -*-
"""

Reidentify

"""
from pyraf import iraf
import os

dir_work = os.getcwd()+'\\..\\data'
os.chdir(dir_work)

# Para ampliar la calibración a toda la extensión espacial de la rendija
# COMPROBAR que los ajustes no pierden calidad. En la terminal, comprobar que
#no se pierden demasiadas lineas ni disminuya la RMS (corregir con fitcoords si
#alguna se va y volver a correr ¿reidentify?)
iraf.reidentify("oh_skylines", "oh_skylines", section="", newaps="yes", \
     coordlist="lirisdr$std/ohlines.dat",interactive="no",overrid="yes", refit="yes", trace="yes", \
     step=20, nsum=20, nlost=3, cradius=5., match=-6.0, maxfeat=50, minsep=2.,verbose="yes")

# 
iraf.fitcoords("oh_skylines", fitname="oh_skylines", interactive="yes", combine="yes",\
     function="legendre", xorder=5, yorder=4)