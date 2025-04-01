# -*- coding: utf-8 -*-
"""

Imcombine

"""
# sn05kl + BD402534
from pyraf import iraf
import os
import numpy as np

dir_work = os.getcwd()+'\\..\\data'
os.chdir(dir_work)

# MEDIR el centroide del objeto y de la estrella en todas las imagenes. Lo hacemos como el implot de antes: 
#corte central en columnas (:c 400 450) y hacemos p-p a cada lado del objeto para obtener 
#el centroide. Lo hacemos para archivos ya corregidos de flat field y de lambda
# Zoom pulsando con 'e' en la esquina inferior izquierda y superior derecha de la zona que
#se quiere aumentar
# iraf.implot("wf//@sub_sn05kl.lst")
peak_sn = np.array([303.57, 351.27, 303.70, 351.86])
yoff_sn = peak_sn[0] - peak_sn
# iraf.implot("wf//@sub_BD402534.lst")
peaks_est = np.array([304.50, 353.11])
yoff_est = peaks_est[0] - peaks_est

# COMBINACIÓN de los espectros teniendo en cuenta los offsets relativos entre las distintas
#imágenes
# SN
iraf.delete('sn05kl.off', verify='no')
with open('sn05kl.off','w') as f:
    for y in yoff_sn:
        f.write("0 {:.0f}\n".format(y))
iraf.imdelete('sn05kl.fits', verify='no')
iraf.imcombine("wf//@sub_sn05kl.lst", "sn05kl", offsets="sn05kl.off", \
             combine="average",zero="median",\
             reject="sigclip",lsigma=3,hsigma=3,nkeep=5)
# Star
iraf.delete('BD402534.off', verify='no')
with open('BD402534.off','w') as f:
    for y in yoff_est:
        f.write("0 {:.0f}\n".format(y))
iraf.imdelete('BD402534.fits', verify='no')
iraf.imcombine("wf//@sub_BD402534.lst", "BD402534", offsets="BD402534.off", \
             combine="average",zero="median",\
             reject="sigclip",lsigma=3,hsigma=3,nkeep=5)