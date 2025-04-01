# -*- coding: utf-8 -*-
"""

Extracción del espectro. Apall

"""
# sn05kl + BD402534
from pyraf import iraf
import os
import numpy as np

dir_work = os.getcwd()+'\\..\\data'
os.chdir(dir_work)

# ¡¡¡PUEDE NO CORRER DESDE EL ARCHIVO!!! COPIAR Y PEGAR EN LA TERMINAL

# Paquetes de la tarea apall
iraf.twodspec()
iraf.apextract()
# Se abre apall. Definimos una apertura inicial (si hay una previa borramos con 'd') con 'm' (centro), 'u' 
#(limite derecho) y 'l' (limite izquierdo). Para reducir al 10%, (:ylevel 0.1) y 'z'. Despues vamos al 
#fondo ('b'). Borramos lo q haya con la 't' y hacemos 's'-'s' a cada lado del cielo en ambos lados del pico
#(dos ventanas en cada conitnuo) Seguimos avanzando hasta llegar al fit. Cambiar el orden a 3-4 y 
#eliminar los puntos que se vayan ('d'). Para ver residuos 'j'. Seguimos avanzando y damos enter a todo
# Zoom out with 'w'+'a' y zoom in with 'w'+'e'+'e'

# Estrella
iraf.hedit("BD402534.fits", "DISPAXIS", 1, addonly="yes", verify="no")
iraf.imdelete('BD402534.0001.fits', verify='no')
iraf.apall("BD402534", apertures=1, format="onedspec", interactive="yes",\
    find="yes", recenter="yes", resize="no", edit="yes", trace="yes",\
    fittrac="yes", extract="yes", background="no", extras="no", review="yes",\
    nsum=40, line=450)
    
# SN
iraf.hedit("sn05kl.fits", "DISPAXIS", 1, addonly="yes", verify="no")
iraf.imdelete('sn05kl.0001.fits', verify='no')
iraf.apall("sn05kl", apertures=1, format="onedspec", interactive="yes",\
    find="yes", recenter="yes", resize="no", edit="yes", trace="yes",\
    fittrac="yes", extract="yes", background="no", extras="no", review="yes",\
    nsum=40, line=450)