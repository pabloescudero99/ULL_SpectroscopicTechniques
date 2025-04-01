#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

APALL

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

# Nos aseguramos de que estén cargados los paquetes que contienen la
# tarea apall
iraf.twodspec()
iraf.apextract()
#
iraf.apall.format = "multispec"   # genera espectro con sufijo ".ms"
iraf.apall.nsum = 20
iraf.apall.readnoise = 5.0        # valores aproximados sacado de
iraf.apall.gain = 1.16            # http://www.ing.iac.es/Engineering/detectors/ultra_eev12.htm
iraf.apall.background = "fit"
iraf.apall.lower = -12            # ~ 2.5 * fwhm
iraf.apall.upper = 12             # ~ 2.5 * fwhm
iraf.apall.llimit = -12
iraf.apall.ulimit = 12
iraf.apall.width = 8
iraf.apall.ylevel = 0.00
iraf.apall.peak = "yes"
iraf.apall.bkg = "no"             # este no tiene que ver con la resta del background ...
iraf.apall.skybox = 1
iraf.apall.lsigma = 2.5
iraf.apall.usigma = 2.5
iraf.apall.weights = "none"
iraf.apall.interactive = "yes"
# Parámetros sobre la sustracción del cielo (background)
iraf.apall.b_sample = "-55:-25,25:55"   # con respecto al centro de la traza
iraf.apall.b_naverage = -3
iraf.apall.b_niterate = 3
iraf.apall.b_low_reject = 3.
iraf.apall.b_high_rejec = 3.
iraf.apall.b_function = "legendre"
iraf.apall.b_order = 2               # ajustamos una recta al background
# Parámetros sobre seguimiento de la traza (posición del pico en función
# de lambda)
iraf.apall.t_order = 12
iraf.apall.t_nsum = 20
iraf.apall.t_step = 20
iraf.apall.t_function = "legendre"
iraf.apall.t_low_r = 3.0
iraf.apall.t_high = 3.0
iraf.apall.t_niterate = 1

# aplicación de apall
iraf.imdelete("lamcal_WHT9958.ms", verify="no")
iraf.apall("lamcal_WHT9958", extract="yes", extras="no")
# extra = no" significa que no queremos el espectro del cielo,
# ni la sigma (incertidumbre sobre el espectros extraído).

# VENTANA INTERACTIVA:
# - Find apertures? yes
# - Number of apertures to be found automatically: 1
#   (Nota: si ya hemos encontrados alguna apertura y repetimos la operaciÃ³n,
#   es posible que apall no nos vuelva a hacer estas preguntas, ya que la
#   informaciÃ³n sobre las aperturas se queda grabada en un fichero en la
#   carpeta 'database')
# - Recenter? yes
# - Resize? yes
# - Edit aperture? yes 
#   Como ya tenemos la apertura marcada y centrada, no hay que marcar ninguna
#   apertura mÃ¡s, asÃ­ que **NO** utilicen la tecla ``m``.
#   Con esto deberÃ­a aparecernos una ventana grÃ¡fica con la apertura y las
#   dos zonas del cielo ya definidas. Si estamos satisfechos, pulsamos ``q``
#   y contestamos 'yes' a Trace apertures?
# - Fit traced positions? yes
# - Fit curve to aperture? yes 
#   Nos aparece la traza del espectro, o sea la posiciÃ³n del centro (pico de
#   luz) en X a lo largo del eje espectral.
#   Un polinomio de legendre de grado 10-12 deberÃ­a proporcionar un buen
#   ajuste. Notamos que la traza solo se desplaza unas pocas dÃ©cimas de
#   pÃ­xel. Podemos jugar con los parÃ¡metros de ajuste (order, low\_ e 
#   high_reject, niter ...) hasta encontrar el ajuste que nos mÃ¡s convence.
# - Salimos con ``q``
# - Write apertures? yes
# - Extract aperture? yes
# - Review extracted spectra? yes
# - Review extracted spectrum for aperture 1? yes 
#   En la ventana grÃ¡fica nos aparece el espectro, salimos con ``q`` y ya
#   tenemos el espectro extraÃ­do (el fichero con extensiÃ³n .ms.fits)

# También podrímos tener la necesidad de cambiar la ventana de extracciÃ³n
# del espectro y/o las zonas donde se mide el nivel del cielo. Tras 
# contestar yes a las preguntas (hasta 'edit aperture?') nos aparece
# la ventana grÃ¡fica con la apertura y la zonas del cielo. Luego:
# - Nos ponemos con el cursor en la zona de la apertura, a la izquierda,
#   con ``l`` definimos el 'lower limit' de la apertura; luego posicionamos
#   el curso a la derecha y con ``u`` marcamos el 'upper limit' (en la barra
#   de abajo se muestras dichos lÃ­mites en pÃ­xeles).
# - Para ser mas precisos podemos hacer un **zoom**. Ubicamos el cursor en la
#   esquina izquierda/abajo de la zona que queremos visualizar, tecleamos
#   ``w`` y ``e``, luego vamos a la esquina arriba/derecha y tecleamos ``e``.
# - Para cambiar las zonas donde se mide el cielo, tecleamos ``b``, y vemos el 
#   resultado del fit (la linea discontinua). Nos ponemos sobre la dos
#   zonas ya marcadas, y las borramos con ``z``. Las volvemos a definir con
#   ``s`` (marcando cuantas zonas queremos: pulsar ``s`` en el extremo izquierdo
#   y luego en el derecho de la zona deseada; repetir para aÃ±adir mÃ¡s zonas); 
#   tecleamos ``f`` para rehacer el ajuste. 
# - Si estamos contentos salimos con ``q``. Luego otro ``q`` para salir 
#   del ajuste del background, y seguimos con 'Trace aperture?'