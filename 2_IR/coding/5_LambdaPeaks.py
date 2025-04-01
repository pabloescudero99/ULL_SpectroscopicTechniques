# -*- coding: utf-8 -*-
"""

Valores de lambda de los picos dado el redshift

"""
import numpy as np
z = 0.00349
lambda_ref = ['HeI10830', 'P_10', 'P_9', 'P_8', 'P_7', 'P_gamma', 'P_betta']
lambda_lab = [10830, 9015, 9229, 9546, 10049, 10938, 12818]
desplaz_lambda = [z*x for x in lambda_lab]

for ind in range(len(lambda_ref)):
    print(f'\n{lambda_ref[ind]}: Desplaz.= {desplaz_lambda[ind]}')