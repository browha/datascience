# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 11:38:19 2017
***** IT IS REALLY IMPORTANT TO NOTE THE RANGE OF CONFIGURABLES BELOW *****
@author: me
"""


import os
os.environ['R_HOME']='C:/Progra~1/R/R-3.3.2/'
os.environ['R_USER']='ME'
#os.environ['R_HOME']='C:\\Program Files\\R\\R-3.3.2\\bin\\x64\\'                      
import rpy2.rinterface as ri
try:
    ri.set_initoptions(('rpy2', '--verbose', '--no-save'))
    ri.initr()
except RuntimeError:
    pass
lib_path="'C:/Users/henry.brown/Documents/R/win-library/3.3'"
from rpy2.robjects import pandas2ri
pandas2ri.activate()
import pandas.rpy.common as common #This module will get deprecated at some point.... 
import rpy2.robjects as ro
import numpy as np
import pandas as pd


print ro.r(".libPaths(c(.libPaths(),"+lib_path+"))")
