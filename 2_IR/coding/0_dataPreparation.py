# -*- coding: utf-8 -*-
"""

Preparación de los datos

"""

from pyraf import iraf
import os

dir_work = os.getcwd()+'\\..\\data'
os.chdir(dir_work)

# Lista con info de la cabecera
listraw=iraf.hselect("tcr*.fits", "$I,CAT-NAME,OBJECT,RA,DEC,ROTSKYPA,LIRSLNAM,LIRGRNAM,\
  LIRLAMP1,LIRLAMP2,EXPTIME,AIRMASS,DATE-OBS,UTOBS", "yes",Stdout=1)

# Guardar en archivo .log la información de la lista anterior
iraf.delete('observations.log', verify='no')
with open('observations.log','w') as f:
    for item in listraw:
        f.write("%s\n" % item)

# Elaboración de la imagen sin la emisión del objeto, es decir, imagen con 
#el cielo
# Escogemos las imágenes de mayor exposure time
iraf.imdelete('oh_skylines', verify='no')
iraf.imcopy("tcr805624.fits", "oh_skylines")
# Eliminamos de la imagen A la emisión del objeto pegando el cielo de la B
iraf.imcopy("tcr805625[*,270:325]", "oh_skylines[*,270:325]")