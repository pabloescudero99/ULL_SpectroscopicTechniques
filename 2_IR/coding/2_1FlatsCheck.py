# -*- coding: utf-8 -*-
"""

Comprobación de flats

"""
from pyraf import iraf
import os

dir_work = os.getcwd()+'\\..\\data'
os.chdir(dir_work)

# Lista con flats para las SNs
# case SNe  (Warning: flat-fields were taken using a different slit than the one used for science frames)
lista_flats=iraf.hselect("tcr*.fits", "$I", \
    "IMAGETYP?='flat' && LIRSLNAM='l1' && LIRGRNAM?='lrzj'", Stdout=1)

# COMPROBAR nivel de iluminación de los flats
# Next step, we check that the illumination level of the images included in the list of flats is homogeneous.
#Expected values are in the range 5000-20000 ADUs, the higher the better. Sometimes it is necessary to discard 
#few of them if the counts are not the same as those of the rest.
for im in lista_flats:
    iraf.imstat(im, fields="image,midpt,mean,stddev", format="no")

check = input('\n¿Todo OK? (Yes/No)\n')
if check == 'Yes':
    print('\nAhí estamossss\n')
    iraf.delete('lista_flats.log', verify='no')
    with open('lista_flats.log','w') as f:
        for item in lista_flats:
            f.write("%s\n" % item)
elif check == 'No':
    print('\nEliminar de la lista alguna de las imágenes flat\n')
else:
    check = input('\nIntroduzca Yes o No!!!\n')