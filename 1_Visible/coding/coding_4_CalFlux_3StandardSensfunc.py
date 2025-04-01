#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

STANDARD, SENSFUNC

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

airmass = iraf.hselect("WHT9958", "AIRMASS", "yes", Stdout=1)
exptime = iraf.hselect("WHT9958", "EXPTIME", "yes", Stdout=1)
# aquí también reemplazamos espectroestandar por el nombre de fichero
# que contiene el espectro de la estrella estándar.
# En principio la masa de aire debería ser la de a mediado de la exposición, mientras la cabecera nos da la masa de aire al comienzo. Hay tareas de IRAF que permiten calcular la masa de aire efectiva (una especie de media pesada a lo largo de la exposición), pero para tiempos de exposición cortos las diferencias son generalmente despreciables.

print('\nObservatorio: lapalma\n')
iraf.standard.extinction = "EXTINCTION/wlext.dat"
# EXTINCTION y STANDARDS son dos subcarpetas dentro de la carpeta con
# los datos
iraf.standard.observa = "lapalma"
# directorio y nombre del fichero (sin extensión) con el flujo tabulado.
iraf.standard.caldir = "STANDARDS/"
iraf.standard.star_name = "hd935"
# aunque la estrella se llame HD93521, el fichero con el flujo
# tabulado se llama hd935
iraf.standard.exptime = float(exptime[0])
iraf.standard.airmass = float(airmass[0])
#
iraf.sensfunc.extinct = "EXTINCTION/wlext.dat"
iraf.sensfunc.observa = "lapalma"
iraf.sensfunc.function = "legendre"

# aplicación de STANDARD
iraf.delete("std_hd93521", verify="no")
iraf.standard("lamcal_WHT9958.ms", "std_hd93521")
# nombre de la estrella en el catalogo, por ejemplo hd93521.
# Contestamos "no" al editar los "bandpasses"

# aplicación SENSFUNC
iraf.imdelete("sens_hd93521", verify="no")
valorinicial = 6
iraf.sensfunc("std_hd93521", "sens_hd93521", order=valorinicial)
# Como valorinicial del order podemos partir en un número pequeño, por
# ejemplo 6, y subirlo hasta encontrar un ajuste satisfactorio.

# vamos borrando los puntos que desvíen mucho del ajuste, por ejemplo los que 
# se encuentran en las bandas de absorción. Para eso, nos ponemos con el cursor
# sobre el punto a borrar, tecleamos d y luego contestamos p. Las otras 
# posibles respuestas son s para borrar una estrella (es posible ajustar los 
# datos de varia estrellas simultáneamente), o w (borra todos los demás puntos 
# a la misma longitud de onda).
# Un “order” de 10 o 12 puede estar bien: estamos realizando un ajuste “suave” 
# a la relación cuentas-flujo, así que no tiene sentido aumentar el grado del 
# polinomio para que este siga todos los pequeños picos y valles que aparecen 
# en los datos a ajustar).
