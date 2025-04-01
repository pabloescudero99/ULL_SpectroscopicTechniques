# -*- coding: utf-8 -*-
"""

Preparación de datos (2)

"""
# sn05kl + BD402534
from pyraf import iraf
import os

dir_work = os.getcwd()+'\\..\\data'
os.chdir(dir_work)

# Corrección de Flatfield
iraf.imdelete('fS*.fits', verify='no')
iraf.imarith("@sub_sn05kl.lst","/","Nflat_lrzj_sn","f//@sub_sn05kl.lst")
iraf.imarith("@sub_BD402534.lst","/","Nflat_lrzj_sn","f//@sub_BD402534.lst")
#iraf.imarith("@sub_ABsn05kl.lst","/","Nflat_lrzj_sn","f//@sub_ABsn05kl.lst")
#iraf.imarith("@subAB_BD402534.lst","/","Nflat_lrzj_sn","f//@subAB_BD402534.lst")
#iraf.imarith("@sub_BAsn05kl.lst","/","Nflat_lrzj_sn","f//@sub_BAsn05kl.lst")
#iraf.imarith("@subBA_BD402534.lst","/","Nflat_lrzj_sn","f//@subBA_BD402534.lst")

# Indicar eje de dispersión en la cabecera
iraf.hedit("fS*fits","DISPAXIS",1,addonly="yes",verify="no")

# Calibración en longitud de onda
# cargar los módulos necesarios
iraf.twodspec()
iraf.longslit()
iraf.imdelete('wf*.fits', verify='No')
iraf.transform("f//@sub_sn05kl.lst","wf//@sub_sn05kl.lst",fitnames="oh_skylines",database="database")
iraf.transform("f//@sub_BD402534.lst","wf//@sub_BD402534.lst",fitnames="oh_skylines",database="database")

# COMPROBAR la calibracion haciendo un splot de una de las imagenes en 300
# Tambien podemos hacerlo con un implot: 
# -1: hacemos un corte en columnas en torno a la zona central del detector (:c 450-550) para ver los objetos
# -2: nos ponemos encima del objeto y damos espacio para ver las coordenadas
# -3: hacemos un promedio en torno a la fila de la coordenada del objeto (linea 304).
#Por ejemplo, si esta en 150 hacemos (:l 149:151)
# -4: para cambiar de pixel a lambda hacemos (:w world)