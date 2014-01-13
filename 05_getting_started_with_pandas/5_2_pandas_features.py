# -*- coding: utf-8 -*-
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

####################
# 5.2.1. reindexing
####################
print ">>> obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])"
obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])

print ">>> obj"
print obj

####################################
# create "obj2" by reindexing Series
####################################
print ">>> obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])"
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])

print ">>> obj2"
print obj2

#############################################
# create by reindexing Series with fill_value
#############################################
print ">>> obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)"
print obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)

###############################################
# create "obj3" by reindexing Series with ffill
###############################################
print ">>> obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])"
obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])

print ">>> obj3.reindex(range(6), method='ffill')"
print obj3.reindex(range(6), method='ffill')


#########################################
# create "frame2" by reindexing DataFrame
#########################################
print """>>> frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],
                  columns=['Ohio', 'Texas', 'California'])"""
frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],
                  columns=['Ohio', 'Texas', 'California'])
print ">>> frame"
print frame

print ">>> frame2 = frame.reindex(['a', 'b', 'c', 'd'])"
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print ">>> frame2"
print frame2

#########################################
# reindex columns with columns= parameter
#########################################
print ">>> states = ['Texas', 'Utah', 'California']"
states = ['Texas', 'Utah', 'California']

print ">>> frame.reindex(columns=states)"
print frame.reindex(columns=states)

#################################
# reindex columns and rows
# Note: ffill works only for rows
#################################
print """>>> frame.reindex(index=['a', 'b', 'c', 'd'], method='ffill',
              columns=states)"""
print frame.reindex(index=['a', 'b', 'c', 'd'], method='ffill',
              columns=states)

############################
# reindexing with 'ix' field
############################
print ">>> frame.ix(['a', 'b', 'c', 'd'], states)"
print frame.ix[['a', 'b', 'c', 'd'], states]


#############################################
# 5.2.2. remove elements from rows or columns
#############################################


###########################################
# 5.2.3. index reference, select, filtering
###########################################

########################################
# 5.2.4. arithmetics and data formatting
########################################

####################################################
# 5.2.4.1. arithmetic methods and value substitution
####################################################


#############################################
# 5.2.4.2. operations on DataFrame and Series
#############################################


#########################################
# 5.2.5. function application and mapping
#########################################


############################
# 5.2.6. sorting and ranking
############################

############################################################
# 5.2.7. indexing on columns or rows having duplicate values
############################################################




