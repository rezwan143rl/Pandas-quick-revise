import pandas as pd
import numpy as np
##list to series
# ice_cream= ["vanilla","chocolate","Butter scotch","pistacio"]
# Ice_cream_series=pd.Series(ice_cream)
# print(Ice_cream_series)
# #series combines both list and dictionary. we can
# #give values an identifier just like a dictionary in a list
# # 0          vanilla
# # 1        chocolate
# # 2    Butter scotch
# # 3         pistacio
# #dtype: object (for string it is object type)
# #result is like this . as there is no identifier it automatically assigns a numeric identifier
# lottery_numbers=[1,6,3,2,7,9]
# lottery_numbers_series=pd.Series(lottery_numbers)
# print(lottery_numbers_series)
# #output:
# #1    6
# #2    3
# #3    2
# #4    7
# #5    9
# #dtype: int64
# resistration=[True,False,False,True,False,False,]
# resistration_series=pd.Series(resistration)
# print(resistration_series)
# # output
# # 0     True
# # 1    False
# # 2    False
# # 3     True
# # 4    False
# # 5    False
# # dtype: bool

# dictionary to series

# sushi={
#     "salmon":"orange",
#     "tuna":"red",
#     "coral":"white"
# }
# sushi_series=pd.Series(sushi)

# print(sushi_series)
# # output
# # salmon    orange
# # tuna         red
# # coral      white
# # dtype: object
# # here is no numeric value rather the keys 
# # in this case dictionary is ordered

# # pandas series methods

# prices =pd.Series([250,33,231,650,333])
# print(prices.to_csv())
# print(prices.sum())
# print(prices.divide(3))
# print(prices.add(15))

# #series attributes

# ser= pd.Series(index=["alice","malice","chelish","delish"],data=[2,3,1,4])
# prices =pd.Series([250,33,231,650,333])
# print(ser)
# print(ser.size)
# print(ser.is_unique)
# print(ser.index)
# print(ser.values)
# print(prices.index)
# print(type(ser.values))
# print(type(ser.index))
# print(type(prices.index))
# pd.Series()

# read a csv file and squeeze it to a series. as primarily its a data frame
pokemon=pd.read_csv("pokemon.csv",usecols=["Name"]).squeeze("columns") 
# print(pokemon)
# print(pd.read_csv("pokemon.csv"))
dataset=pd.read_csv("dataset.csv",usecols=["Age"]).squeeze("columns")
# print(dataset)

# #Read a series from head to number of element(0-el-1) /
# #Read a series from tail to -number of element (el to el-n) 

# print(pokemon.head(1)) #default is 5 
# print(dataset.tail(11)) 


#python functions in pandas 
# print(len(pokemon))
# print(type(len(pokemon)))
# print(dict(pokemon))
# print(sorted(pokemon))
# print(list(pokemon))
# print(sorted(dataset))
# print(min(dataset))
# print(max(dataset))
# print(min(pokemon))
# print(max(pokemon))

# # finding if a key or value in the series using default "in" key word in python

# #as in
# print("balbasaor" in pokemon) # this will return false as in keyword looks for index or key if not explicitky said

# print(11 in pokemon) # this will say true 
# print("Ivysaur" in pokemon.values) # this will return true as explicitly said
# print("nokia" in pokemon.values) # this will return false as doesnot exist

# sort_value method 

print([pokemon.sort_value()])




