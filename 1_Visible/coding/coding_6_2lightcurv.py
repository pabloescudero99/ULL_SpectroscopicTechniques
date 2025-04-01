#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

lightcurv

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt
import scipy.constants as ctes

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

# guardamos como variables los datos de las líneas generadas con fitprofs
centro, flujo, gfwhm = np.loadtxt("NGC1068_final.log", unpack=True, usecols=(0,2,5))
# array a partir de x1=165 y con el tamaño de la variable centro
linea = 160+np.arange(0,len(centro))

# Calcula la velocidad radial
velluz = ctes.speed_of_light / 1e3
Hbeta_r = 4861.35
vel = velluz*((centro-Hbeta_r)/Hbeta_r)

plt.clf()
# Como el ajuste falla en varias posiciones y produce números sin sentido,
# conviene poner manualmente el rango en Y. También puede ser conveniente
# dibujar los puntos sin unirlos por linea continua.
# Curva de rotación
y1 = 1255-200 # 0
y2 = 1255+200 # 2000
plt.ylim(y1, y2)
# En y1 e y2 poner unos valores adecuados, Se puede empezar por un intervalo
# relativamente grande (por ejemplo 0 y 2000) y luego ajustarlo.
plt.plot(linea, vel, 'o', markersize=2)
plt.savefig("vel_NGC1068.png")

plt.clf()
# Curva de flujo
ymax = 20000 #100000
plt.ylim(0, ymax)
# Se puede poner en ymax un valor relativamente grande (ej. 100000) y luego
# ajustarlo en función el valor máximo observado del flujo.
plt.plot(linea, flujo, 'o', markersize=2)
plt.savefig("flujo_NGC1068.png")

# Para mejorar la curva de rotación, podemos eliminar aquellos puntos
# que tengan flujo muy pequeño (< 200) o un ajuste dudoso, por ejemplo
# con valores de gfhwm muy altos (digamos mayores de 5 Angstroem).
# Usamos para esto las mascaras de numpy.
# plt.clf()
msk = np.where((flujo > 200.)*(gfwhm < 5.0))
# msk es un array que contiene los índices que corresponden a aquellos
# datos que cumplen con las condiciones definidas arriba (en este caso
# la multiplicación equivale a un AND lógico).
lineaS = linea[msk]
flujoS = flujo[msk]
velS = vel[msk]
plt.ylim(y1, y2)
plt.plot(lineaS, velS, 'o', markersize=2)
# plt.savefig("vel_NGC1068_comp.png")
plt.savefig("velS_NGC1068.png")
plt.clf()
# La curva de velocidad ahora está mucho más "limpia".

# curva de flujo corregida
ymax = 20000 #100000
plt.ylim(0, ymax)
# plt.plot(linea, flujo, 'o', markersize=2)
plt.plot(lineaS, flujoS, 'o', markersize=2)
# plt.savefig("flujoS_NGC1068.png")
plt.savefig("flujo_NGC1068_comp.png")