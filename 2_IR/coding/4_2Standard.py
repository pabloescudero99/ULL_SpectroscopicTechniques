# -*- coding: utf-8 -*-
"""

Standard

"""
# sn05kl + BD402534
from pyraf import iraf
import os
import numpy as np

dir_work = os.getcwd()+'\\..\\data'
os.chdir(dir_work)

# Usamos programa standard. Asigna unidades de flujo a las cuentas. Ajustamos a un continuio para evitar absorcion. 
#Con sensfunc hacemos algo. Hayq  buscar en simbad cosas de la estrella por coordenadas. Magbnitudes en J para SNE.
# Primero buscamos la estrella en simbad con las coordenadas del imheader 
# Para BD402534: Spectral type G6V. Flux: B-10.98[0.05]; V-10.32[0.04]; G-10.064022[0.002779]; J-8.981[0.018]; H-8.597[0.020]
#K-8.561[0.019]
#https://simbad.cds.unistra.fr/simbad/sim-id?Ident=%401923603&Name=BD%2b40%20%202534&submit=submit

star_name='j'  ## use the name of the band covered by the spectrum (j, h or k)
magband="J"    ## reference band where the standard has calibrated magnitude
mag = 8.981    ## calibrated magnitude in "magband", obtained from SIMBAD-CDS
Teff="G6V"     ## the temperature of the star can be specified as the spectral type
bandwidth=50   ## width of the band where the instrumental magnitude will be computed
bandsep=100     ## separatin of the bands where the instrumental magnitude will be computed
bbdir="onedstds$blackbody/" ## directory where to find the black-body models
iraf.standard.extinct = ""
iraf.unlearn('standard')

iraf.delete('std_cont', verify='no')
iraf.standard("BD402534_cont", "std_cont", samesta="yes", beam_sw="no", \
              star_name=star_name, bandwid=bandwidth, bandsep=bandsep,magband=magband,mag=mag,\
              caldir=bbdir, teff=Teff, interac="yes")