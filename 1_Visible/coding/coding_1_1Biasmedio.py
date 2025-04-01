# -*- coding: utf-8 -*-
"""
BIAS MEDIO

"""
from pyraf import iraf
import numpy as np
import glob, os
import matplotlib.pyplot as plt

dir_work = os.getcwd()+'/../data/'
# print(dir_work)
os.chdir(dir_work)

# lista de bias
listbias = iraf.hselect("WHT*.fits", "$I", "OBJECT='BIAS'", Stdout=1)

# estadística para comprobar q no hay variaciones en num de cuentas entre los bias
# for im in listbias:
#     iraf.imstat(im, fields="image,mean,stddev", format="no")

# Creación del bias medio
iraf.imdelete("Biasmedio", verify="no")
iraf.imcombine(",".join(listbias), "Biasmedio", combine="average",\
               reject="minmax")

# Gráficos de promedio de filas y columnas del bias medio
iraf.prows("Biasmedio", 800, 1200)
iraf.gki.printPlot()
newest = max(glob.iglob('*.eps'), key=os.path.getctime)
os.rename(newest, "Biasmedio_prows.eps")
# 
iraf.pcols("Biasmedio", 100, 400)
iraf.gki.printPlot()
newest = max(glob.iglob('*.eps'), key=os.path.getctime)
os.rename(newest, "Biasmedio_pcols.eps")
# Los ficheros postscript se pueden visualizar con el comando: gv nombrefichero.eps
# Si no se genera el fichero .eps, o está vacío o da error al visualizarlo, es posible que esté mal definida 
# la variable stdplot (por ejemplo todavía apuntando a la impresora), comprobarlo en el fichero loginuser.cl.
# También a veces falla si tenemos los datos en el home en lugar del disco scratch del ordenador

# Estadística del bias medio
iraf.imstat("Biasmedio", fields="image,mean,stddev", format="no")
iraf.imstat("Biasmedio[100:400,800:1200]", fields="image,mean,stddev",
            format="no")
