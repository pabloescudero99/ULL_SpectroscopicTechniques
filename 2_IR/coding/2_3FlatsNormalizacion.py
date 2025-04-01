# -*- coding: utf-8 -*-
"""

Normalización del flat

"""
from pyraf import iraf
import os

dir_work = os.getcwd()+'\\..\\data'
os.chdir(dir_work)

iraf.imdelete("Nflat_lrzj_sn", verify="no")
# Interactivamente
#iraf.response.eParam()
# Con la línea de comandos
# el uso de la función spline3 con órdenes muy altos es habitual para aplanar las variaciones espectrales
# utilice la keyword "k" para comprobar la relación entre el espectro observado y el modelo. Se encuentra una buena solución
# cuando la relación no muestra tendencias claras a lo largo del eje de longitudes de onda y la mayoría de los valores de la relación están dentro del 1%
iraf.response("flat_lrzj_sn", "flat_lrzj_sn", "Nflat_lrzj_sn", interactive="yes", sample="*",\
     naver=1, function="spline3", order=45, low_rej=0, high_rej=0, niter=3)
# Sale una ventana con cielo vs ajuste. Le damos a la k para ver el ratio señal/ajuste y vamos aumentando 
#el orden hasta q mejore. Me he quedado en ¿100?. ¿EL rms da igual?