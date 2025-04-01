#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Espectro Promedio

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

# lista con espectros calibrados de flujo
lista_galax_fl = iraf.hselect("flujcal_W*.fits", "$I", "OBJECT?='NGC'", Stdout=1)

# espectro promedio combinandolos
iraf.delete("NGC1068_final", verify="no")
iraf.imcombine(",".join(lista_galax_fl), "NGC1068_final", combine="average",
     reject="crreject", scale="none", lsigma=3.0, hsigma=2.5,
     rdnoise=5.0, gain=1.20, snoise=0.10, lthreshold=-10,
     rejmask="NGC1068_mask")
# - *rdnoise* y *gain* no los tenemos en la cabecera, asÃ­ que ponemos los
#   que se encuentran en la Web del ING, 
#   http://www.ing.iac.es/Engineering/detectors/ultra_eev12.htm
# - *snoise* es un parÃ¡metro de 'tolerancia' para tener en cuenta posible 
#   pequeÃ±os desplazamientos (en X y Y) entre los diferentes espectros.
# - *lthreshold* excluye los pÃ­xeles con valores inferiores a el.
# - *rejmask* es una imagen de salida con 6 'capas', cada capa contiene los 
#   pÃ­xeles rechazados por el algoritmo para cada imagen en input. Sirve para
#   comprobar que el rechazo no haya sido demasiado agresivo, eliminando
#   pÃ­xeles vÃ¡lidos (a veces sucede, en el cual caso hay que rehacer el
#   imcombine modificando los parÃ¡metros hasta encontrar la combinaciÃ³n
#   mejor).

# comparación con uno de los espectros y se muestra la máscara generada
# iraf.display("NGC1068_final", 1, zsca="no", zran="no", ztra="log",
#      z1=80, z2=3000)
# iraf.display("flujcal_WHT9874", 2, zsca="no", zran="no", ztra="log",
#      z1=80, z2=3000)
# iraf.display("NGC1068_mask", 3, zsca="no", zran="no", ztra="log",
#      z1=80, z2=3000)

# Para ver las capas de la máscara
# iraf.display("NGC1068_mask.pl[*,*,1]", 1, zsca="no", zran="no",
#      ztra="linear", z1=-0.5, z2=1.5)
# iraf.display("NGC1068_mask.pl[*,*,2]", 2, zsca="no", zran="no",
#      ztra="linear", z1=-0.5, z2=1.5)