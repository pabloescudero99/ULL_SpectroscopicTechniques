# -*- coding: utf-8 -*-
"""

Sustracción del cielo

"""
# sn05kl + BD402534
from pyraf import iraf
import os

dir_work = os.getcwd()+'\\..\\data'
os.chdir(dir_work)

# Listas de imágemes de la sn y su estrella de calibración
listA_sn05kl = iraf.hselect("tcr*fits", "$I", \
  '@"CAT-NAME"?="SN05KL" && OBJECT?="A:" && LIRGRNAM="lrzj8"', Stdout=1)
listB_sn05kl = iraf.hselect("tcr*fits", "$I", \
  '@"CAT-NAME"?="SN05KL" && OBJECT?="B:" && LIRGRNAM="lrzj8"', Stdout=1)
listA_BD402534 = iraf.hselect("tcr*fits", "$I",  \
   '@"CAT-NAME"?="*40253*" && OBJECT?="A:"  && LIRGRNAM="lrzj8"', Stdout=1)
listB_BD402534 = iraf.hselect("tcr*fits", "$I",  \
   '@"CAT-NAME"?="*40253*" && OBJECT?="B:"  && LIRGRNAM="lrzj8"', Stdout=1)

# eliminamos la extensión de las listas
listA_sn05kl_noext = [s.split('.fits')[0] for s in listA_sn05kl]
listB_sn05kl_noext = [s.split('.fits')[0] for s in listB_sn05kl]
listA_BD402534_noext = [s.split('.fits')[0] for s in listA_BD402534]
listB_BD402534_noext = [s.split('.fits')[0] for s in listB_BD402534]

# Guardar listas en archivos
iraf.delete('listA_sn05kl.lst', verify='no')
iraf.delete('listB_sn05kl.lst', verify='no')
iraf.delete('listA_BD402534.lst', verify='no')
iraf.delete('listB_BD402534.lst', verify='no')
with open('listA_sn05kl.lst','w') as f:
     for item in listA_sn05kl_noext:
          f.write("{}\n".format(item))
with open('listB_sn05kl.lst','w') as f:
     for item in listB_sn05kl_noext:
          f.write("{}\n".format(item))
with open('listA_BD402534.lst','w') as f:
     for item in listA_BD402534_noext:
          f.write("{}\n".format(item))
with open('listB_BD402534.lst','w') as f:
     for item in listB_BD402534_noext:
          f.write("{}\n".format(item))

# Creación de imágenes A-B y B-A y listas con nombre de imágenes finales
iraf.imdelete('S*.fits', verify='no')
listAB_sn =[]
listBA_sn = []
list_sub_sn = []
for ima,imb in zip(listA_sn05kl_noext,listB_sn05kl_noext):
    print("imA:",ima)
    print("imB:",imb)
    outab = "S"+ima+"_"+imb
    outba = "S"+imb+"_"+ima
    iraf.imarith(ima,'-',imb,outab)
    iraf.imarith(imb,'-',ima,outba)
    listAB_sn.append(outab)
    listBA_sn.append(outba)
    list_sub_sn.append(outab)
    list_sub_sn.append(outba)
#Estrella telurica:
list_sub_star =[]
listAB_star = []
listBA_star = []
for ima,imb in zip(listA_BD402534_noext,listB_BD402534_noext):
    print("imA:",ima)
    print("imB:",imb)
    outab = "S"+ima+"_"+imb
    outba = "S"+imb+"_"+ima
    iraf.imarith(ima,'-',imb,outab)
    iraf.imarith(imb,'-',ima,outba)
    list_sub_star.append(outab)
    list_sub_star.append(outba)
    listAB_star.append(outab)
    listBA_star.append(outba)    
# Guardar listas en archivos
iraf.delete('sub_ABsn05kl.lst', verify='no')
with open('sub_ABsn05kl.lst','w') as f:
     for item in listAB_sn:
          f.write("{}\n".format(item))
iraf.delete('sub_BAsn05kl.lst', verify='No')
with open('sub_BAsn05kl.lst','w') as f:
     for item in listBA_sn:
          f.write("{}\n".format(item))
iraf.delete('sub_sn05kl.lst', verify='No')
with open('sub_sn05kl.lst','w') as f:
     for item in list_sub_sn:
          f.write("{}\n".format(item))
iraf.delete('sub_BD402534.lst', verify='No')
with open('sub_BD402534.lst','w') as f:
     for item in list_sub_star:
          f.write("{}\n".format(item))
iraf.delete('subAB_BD402534.lst', verify='No')
with open('subAB_BD402534.lst','w') as f:
     for item in listAB_star:
          f.write("{}\n".format(item))
iraf.delete('subBA_BD402534.lst', verify='No')
with open('subBA_BD402534.lst','w') as f:
     for item in listBA_star:
          f.write("{}\n".format(item))