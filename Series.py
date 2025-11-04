import pandas as pd
# # 1.
# ice_cream=['chocolate','bomb','strawberry']
# print(pd.Series(ice_cream))

# lottery_numbers=[4,9,1,5,1,6,2]
# print(pd.Series(lottery_numbers))
# registrations=[True,False,False,True,True]
# print(pd.Series(registrations))

# # 2.
# mydict={
#     "anisur":"chor",
#     "anna":"dakat",
#     "lenchu":"rapist",
#     "bikrom":"chor",
#     "anis":"chor",
# }
# mydict1=pd.Series(mydict)
# print(mydict1)

# # 3.
# method=pd.Series([3.11,6.22,1.9,2.5])
# print(method.product())
# print(method.mean())
# print(method.std())

# #4.
# attribute=pd.Series(["hot","smart","handsome","brilliant","moga","smart"])
# print(attribute.size)
# print(attribute.values)
# print(attribute.is_unique)
# print(attribute.index)
# print(type(attribute.values))

# #5.
# fruits=["mango","banana","apple","pineapple","peach","kiwi","jackfruit"]
# weekdays=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Satireday"]

# # print(pd.Series(fruits,weekdays))
# # print(pd.Series(data=fruits,index=weekdays))
# print(pd.Series(index=weekdays,data=fruits))
# print(pd.Series(fruits,index=weekdays))
# #all gives same out put but 2,3 and 4 are appropriate

# #6.read_csv
# # pokemon = pd.read_csv("CSV/pokemon.csv",usecols=["Name"]).squeeze("columns").head(10)
pokemon = pd.read_csv("CSV/pokemon.csv",usecols=["Name"]).squeeze("columns")
# pokemon = pd.read_csv("CSV/pokemon.csv",usecols=["Name"]).squeeze("columns").tail(10)
# # print(pokemon.head())

google = pd.read_csv("CSV/GOOGL.csv",usecols=["Open"]).squeeze("columns")
# print(google)

# #8.functions
# print(len(pokemon))
# print(type(pokemon))
# # print(list(pokemon))
# # print(sorted(pokemon))
# # print(sorted(pokemon,reverse=True))
# # print(sorted(google,reverse=True))
# # print(dict(pokemon))
# print(max(google))
# print(min(google))

# #9.in keyword
# print("car"in "racecar")
# # print(pokemon.head())
# print("Bulbasaur"in pokemon) #false
# print("Bulbasaur"in pokemon.values) #true

# #10.sort_values

# print(google.sort_values(ascending=True).head())
# print(google.sort_values(ascending=False).head())

# #11.sort_index
pokemon1 =pd.read_csv("CSV/pokemon.csv",index_col="Name",usecols=["Name","Type 1"]).squeeze(axis="columns")
# print(pokemon1.sort_index(ascending=True).head(15))
# print(pokemon1.sort_index(ascending=False).tail(15))

# # 12.iloc[]
# listi=[]
# for i in range(len(pokemon1)):
#     if(pokemon1.iloc[i]=="Bug"):
#         listi.append(i)
# print(pokemon1.iloc[listi].head(15))       
# #print(pokemon.iloc[1222]) #out of bound
# print(pokemon.iloc[[100,51,622]])
# print(pokemon.iloc[:250])

# #13. loc[]
# print(pokemon1.head(50))
# print(pokemon1.loc["Ivysaur"])
# print(pokemon1.loc[["Ivysaur","Bulbasaur","Vulpix","Pikachu"]])
# try:
#     print(pokemon1.loc[["Ivysaur","Bulbasaur","Vulpix","Pikachu","mollachu"]])
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")

# #14. get method
# print(pokemon1.get("mollachor",default="murgichora nai oita"))
# print(pokemon1.get(["Ivysaur","Bulbasaur","Vulpix","Pikachu",],default="murgichora nai oita")) #default none

# #15. overwrite
# # pokemon.iloc[0]="bullasur"
# # print(pokemon.head())
# # pokemon.iloc[0]="Bulbasaur"
# # print(pokemon.head())
# # pokemon.iloc[[1,3,4]]=["mollachor","olanmelaboro goruchor","murgichor"]
# # print(pokemon.head())
# # pokemon.iloc[[1,3,4]]=["Ivysaur"," VenusaurMega Venusaur","Charmander"]
# # print(pokemon.head())
# # 0                 Bulbasaur
# # 1                  Ivysaur
# # 2                 Venusaur
# # 3    VenusaurMega Venusaur
# # 4               Charmander
# print(pokemon1.head())
# pokemon1.loc[["Bulbasaur","Venusaur","Charmander"]]=["urukku","khura","dengue"]
# print(pokemon1.head())
# pokemon1.loc[["Bulbasaur","Venusaur","Charmander"]]=["Grass","Grass","Fire"]
# print(pokemon1.head())


# #16. copy method
# pokemon_cpy = pokemon.copy()
# print(pokemon.head())
# print(pokemon_cpy.head())
# pokemon_cpy.iloc[1]="mollachor"
# print(pokemon.head())
# print(pokemon_cpy.head())

# #17. math method
# print(google.count())#doesnt count empty
# print(google.size)#counts empty
# print(google.mean())
# print(google.median())
# print(google.mode()) #most frequent
# print(google.min())
# print(google.max())
# print(google.std())
# print(google.sum())
# print(google.product())
# print(google.describe())

# # 18. broadcasting
# print(google.head())
# print(google.head().add(10)) # adds 10 to each
# print(google.head()+10) # adds 10 to each
# print(google.head().sub(20))
# print(google.head()-20)
# print(google.head().mul(2))
# print(google.head() * 2)
# print(google.head().div(12))
# print(google.head() / 12)

# # #19. value_counts method
# # molla={}
# # molla=pokemon1.value_counts().head(1).to_dict()
# # print("the most common power is",list(molla.keys())[0]) #experimenatal
# # print(pokemon1.value_counts(ascending=True,dropna=True))
# print(pokemon1.value_counts(normalize=True)) #gives relative frequency as in mat361 

# #20. apply method takes function as parameter
# # print(pokemon.apply(len))
# def count_a(pokemon):
#     return pokemon.count("a")
# print(pokemon.apply(count_a))

# #21. map method

# # print(pokemon1) 
# # attack_powers={
# #     "Grass": 20,
# #     "Rock": 35
# # }
# attack_powers=pd.Series({
#     "Grass": 20,
#     "Rock": 35
# })

# print(attack_powers)
# print(pokemon1.map(attack_powers))
# # print(pokemon1.map(attack_powers).dropna())
