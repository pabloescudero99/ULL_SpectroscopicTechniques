# -*- coding: utf-8 -*-
"""

Telluric

"""
# sn05kl + BD402534
from pyraf import iraf
import os
import numpy as np

dir_work = os.getcwd()+'\\..\\data'
os.chdir(dir_work)

#iraf.delete('BD402534_tel', verify='no')
#iraf.sarith('BD402534.0001.fits','/','BD402534_cont','BD402534_tel')
#
## Hacemos splot para ver espectro y eliminar las bandas de absorcion de la estrella problema (lambdas en el campus)
##y nos quedamos solo con absorcion. En cada linea que queremos eliminar hacemos 'k k' en cada lado para un ajuste 
##gaussiano y luego '- -' en cada lado para borrarla. Cuando hallamos borrado todas, guardamos con la 'i'
## En principio con la 'i' le das a enter y sobreescribe BD402534_tel, pero nosotros lo hemos guardado en un archivo 
##aparte llamado abs_BD402534_tel
#
#iraf.splot('BD402534_tel')

check = input('\nEsto es un test? (Yes/No)\n')
if check == 'Yes':
    iraf.delete('sn05kl_telcorr_test*', verify='no')
    iraf.telluric("sn05kl_cal", "sn05kl_telcorr_test", "abs_BD402534_tel", ignorea="yes",\
              xcorr="yes", tweakrm="no", interactive="yes", sample="11116:11609",\
              threshold=0., lag=10.0, shift=0, scale=1, dshift=0.1, dscale=0.1,\
              offset=0.5, smooth=1)
elif check == 'No':
    iraf.delete('sn05kl_telcorr*', verify='no')
    iraf.telluric("sn05kl_cal", "sn05kl_telcorr", "abs_BD402534_tel", ignorea="yes",\
              xcorr="yes", tweakrm="no", interactive="yes", sample="11116:11609",\
              threshold=0., lag=10.0, shift=0, scale=1, dshift=0.1, dscale=0.1,\
              offset=0.5, smooth=1)
else:
    print('\nEscribe Yes o No\n')




#iraf.delete('sn05kl_telcorr*', verify='no')
#
#iraf.telluric("sn05kl_cal", "sn05kl_telcorr", "abs_BD402534_tel", ignorea="yes",\
#              xcorr="yes", tweakrm="no", interactive="yes", sample="11116:11609",\
#              threshold=0., lag=10.0, shift=0, scale=1, dshift=0.1, dscale=0.1,\
#              offset=0.5, smooth=1)
# useful key commands:
# :shift VALUE - set an offset between wavelength scale of spectrum to be corrected and the telluric spectrum.
# :dshift VALUE - set an offset increment between wavelength scale of spectrum to be corrected and the telluric spectrum.
# :scale VALUE - set a scale factor between wavelength scale of spectrum to be corrected and the telluric spectrum.
# :dscale VALUE - set a scale increment to be add/subtract to scale
# :offset VALUE - add an offset in flux to show the spectra
# x - shows the corrected spectra with the offset applied plus above and below those with +/- dshift.
# y - shows the corrected spectra with the scale applied plus  above and below those with +/- dscale
#  Note that when using "x" or "y" any of the 3 spectra (top, central or bottom) can be set as reference (the central one)
#by clicking on it
# q - to quit and save the corrected spectrum

# Hay que centrarse en una zona central con lineas teluricas (no tomar los extremos generalmente). Nuestro objetivo 
#es conseguir un espectro plano es esa zona (eliminar absorcion telurica)

# Hay que corregir de shift y dshift (desplazamiento) para hacer corregir la calibracion en lambda. Para ello, le damos
#a x (correccion lambda, eje X) y jugamos con los valores de shift y dshift. El espectro de arriba es el shift+dshift,
#el de en medio shift y el de abajo shift-dshift. Si tocando el espectro de arriba o abajo nos convence mas que el del 
#centro, no ponemos con el cursor encima del espectro y le damos a la tecla del correspondiente eje para colocarlo 
#en el centro

# Despues hay que corregir el scale y el offset, debidos a que las observaciones pueden haberse dado en condiciones
#diferentes (diferentes noche, masa de aire) Para ponernos en esa escala, le damos a la 'y', ya que estamos corrigiendo
#en flujo (eje Y). Mismo concepto que en shift, pero con la tecla y

# Si pulsamos en el espectro del centro con la tecla del eje correspondiente, reduce el +- a un valor mas fino

# Cuando nos convenzca todo el espectro, Q y se guarda es el espectro central