# -*- coding: utf-8 -*-
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

######################
# 5.1.1. Series object
######################
#################
# create "obj",
# a Series object
#################
print ">>> obj = Series([4, 7, -5, 3])" # 出力結果だけだと分かりづらかったので、実行コマンドも print してある（以下同じ
obj = Series([4, 7, -5, 3])

# show obj
print ">>> obj"
print obj
# show vaules
print ">>> obj.values"
print obj.values
# show index
print ">>> obj.index"
print obj.index

##################################
# create "obj2",
# a Series object with index names
##################################
print ">>> obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])"
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

# show obj
print ">>> obj2"
print obj2
# show index
print ">>> obj2.index"
print obj2.index

# select by index
print ">>> obj2['a']"
print obj2['a']

print ">>> obj2['d'] = 6"
obj2['d'] = 6

print ">>> obj2[['c', 'a', 'd']]"
print obj2[['c', 'a', 'd']]

# filtering, multiplication, math function application
print ">>> obj2"
print obj2

print ">>> obj2[obj2 > 0]"
print obj2[obj2 > 0]
print ">>> obj2 * 2"
print obj2 * 2
print ">>> np.exp(obj2)"
print np.exp(obj2)

# Series as dict
print ">>> 'b' in obj2"
print 'b' in obj2

print ">>> 'e' in obj2"
print 'e' in obj2

######################################
# create "obj3",
# a Series obj initialized with a dict
######################################
print ">>> sdata = {'Ohio':35000, 'Texas':71000, 'Oregon':16000, 'Utah':5000}"
sdata = {'Ohio':35000, 'Texas':71000, 'Oregon':16000, 'Utah':5000}

print ">>> obj3 = Series(sdata)"
obj3 = Series(sdata)

print ">>> obj3"
print obj3

########################################################
# create "obj4",
# a Series obj initialized with a dict, with index names
########################################################
print ">>> states = ['California', 'Ohio', 'Oregon', 'Texas']"
states = ['California', 'Ohio', 'Oregon', 'Texas']

print ">>> obj4 = Series(sdata, index=states)"
obj4 = Series(sdata, index=states)

print ">>> obj4"
print obj4

# check NaN with isnull, notnull functions
print ">>> pd.isnull(obj4)"
print pd.isnull(obj4)

print ">>> pd.notnull(obj4)"
print pd.notnull(obj4)

print ">>> obj4.isnull()"
print obj4.isnull()

# addition
print ">>> obj3"
print obj3
print ">>> obj4"
print obj4

print ">>> obj3 + obj4"
print obj3 + obj4

# name attributes
print ">>> obj4.name = 'population'"
obj4.name = 'population'
print ">>> obj4.index.name = 'state'"
obj4.index.name = 'state'

print ">>> obj4"
print obj4

# change index after initialization
print ">>> obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']"
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']

print ">>> obj"
print obj


#########################
# 5.1.2. DataFrame object
#########################
#################################################################
# create "frame",
# a DataFrame object initialized with dictionary {'name': a list}
#################################################################
print """>>> data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year':[2000, 2001, 2002, 2001, 2002],
        'pop':[1.5, 1.7, 3.6, 2.4, 2.9]}"""
data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year':[2000, 2001, 2002, 2001, 2002],
        'pop':[1.5, 1.7, 3.6, 2.4, 2.9]}
print ">>> frame = DataFrame(data)"
frame = DataFrame(data)

print ">>> frame"
print frame

# change column order
print ">>> DataFrame(data, columns=['year', 'state', 'pop']"
print DataFrame(data, columns=['year', 'state', 'pop'])

#################################################################
# create "frame2",
# a DataFrame object initialized with dictionary with index names
#################################################################
print """>>> frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                                 index=['one', 'two', 'three', 'four', 'five'])"""
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five'])
print ">>> frame2"
print frame2

# get columns
print ">>> frame2.columns"
print frame2.columns

# extract DataFrame column as Series using dictionary-like reference
print ">>> frame2['state']"
print frame2['state']

print ">>> frame2.year"
print frame2.year

# extract DataFrame row using ix
print ">>> frame2.ix['three']"
print frame2.ix['three']

# assign a scalar to a column
print ">>> frame2['debt'] = 16.5"
frame2['debt'] = 16.5

print ">>> frame2"
print frame2

# assign a numpy array to a column
print ">>> frame2['debt'] = np.arange(5.)"
frame2['debt'] = np.arange(5.)

print ">>> frame2"
print frame2

# assign a Series object to a column
print ">>> val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])"
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])

print ">>> frame2['debt'] = val"
frame2['debt'] = val

print ">>> frame2"
print frame2

# create a new column
print ">>> frame2['eastern'] = frame2.state == 'Ohio'"
frame2['eastern'] = frame2.state == 'Ohio'

print ">>> frame2"
print frame2

# delete a column
print ">>> del frame2['eastern']"
del frame2['eastern']

print ">>> frame2.columns"
print frame2.columns

#########################################################
# create "frame3",
# a DataFrame object initialized with a nested dictionary
#########################################################
print """>>> pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}"""
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
print ">>> frame3 = DataFrame(pop)"
frame3 = DataFrame(pop)

print ">>> frame3"
print frame3

# transpose
print ">>> print frame3.T"
print frame3.T

##########################################
# initialize a DataFrame object
# with a nested dictionary with index name
##########################################
print ">>> DataFrame(pop, index=[2001, 2002, 2003])"
print DataFrame(pop, index=[2001, 2002, 2003])


###########################################
# initialize a DataFrame object
# with a dictionary having Series as values
###########################################
print """>>> pdata = {'Ohio': frame3['Ohio'][:-1],
         'Nevada': frame3['Nevada'][:2]}"""
pdata = {'Ohio': frame3['Ohio'][:-1],
         'Nevada': frame3['Nevada'][:2]}

print ">>> DataFrame(pdate)"
print DataFrame(pdata)

# set name attribute
print ">>> frame3.index.name = 'year'; frame3.columns.name = 'state'"
frame3.index.name = 'year'; frame3.columns.name = 'state'

print ">>> frame3"
print frame3

# get values attribute (returns ndarray)
print ">>> frame3.values"
print frame3.values

print ">>> frame2.values"
print frame2.values

#####################
# 5.1.3. Index object
#####################
###################################################
# create an Index object
# implicitly created as an index of a Series object
###################################################
print ">>> obj = Series(range(3), index=['a', 'b', 'c'])"
obj = Series(range(3), index=['a', 'b', 'c'])

print ">>> index = obj.index"
index = obj.index

print ">>> index"
print index

print ">>> index[1:]"
print index[1:]

# index is immutable
#index[1] = 'd' # throws an Error

########################
# create an Index object
# using pd.Index
########################
print ">>> index = pd.Index(np.arange(3))"
index = pd.Index(np.arange(3))

print ">>> obj2 = Series([1.5, -2.5, 0], index=index)"
obj2 = Series([1.5, -2.5, 0], index=index)

print ">>> obj2.index is index"
print obj2.index is index

# an index object as a set
print ">>> frame3"
print frame3

print ">>> 'Ohio' in frame3.columns"
print 'Ohio' in frame3.columns

print ">>> 2003 in frame3.index"
print 2003 in frame3.index

