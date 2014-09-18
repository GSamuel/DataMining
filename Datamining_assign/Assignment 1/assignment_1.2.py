"""
Created on Thu Sep 18 09:26:20 2014

@author: Gideon
"""

from xlrd import open_workbook
from pylab import *
import numpy as np

file = 'Data/nanonose.xls'

book = open_workbook(file)
sheet = book.sheet_by_index(0) #select the correct sheet

#print sheet.col_values(1,2)
#print sheet.cell(0,0).value == 'Nanonose'


print '\n\n'

array = np.zeros(shape=(90,8))

for row_index in range(2,sheet.nrows):
    row = np.array(sheet.row_values(row_index,3))
    array[row_index-2] = row

x = array[:,0:1]
y = array[:,1:2]


scatter(x,y)
title('Woopdiedoo')
show()

