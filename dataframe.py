import pandas as pd

nba = pd.read_csv("CSV/NBA.csv")
s=pd.Series([1,4,2,5,1,None])

# 1. same methods from series
# print(nba.head(50))
# print(nba.tail(50))
# print(nba.index)
# print(nba.values)
# print(nba.shape) 
# print(nba.dtypes) # returns a series of data type rather than only one

#not in datafream but in series

# print(s.hasnans)#will return true
# # print(nba.hasnans) # will result in error as not available in dataframe object 
#more

#not in series but in dataframe
# print(nba.columns)
# # print(s.columns) # will error

#different results
# print(s.axes) #only range
# print(nba.axes) # range and column name
# print(s.info())
# print(nba.info())
# print(nba.memory_usage()) # use ful to optimize data

# # 2.
revenue = pd.read_csv("CSV/revenue.csv",index_col="Date")
# print(revenue)
# test =pd.Series([1,4,2,5])
# print(test.sum())
# print(revenue.sum())        # will sum collumwise by default
# print(revenue.sum(axis="columns",skipna=True,numeric_only=True))               # will sum using diff parameters

# # #3.select any column from dataframe
# #  # using attributes as column name
# # print(nba.Team)             # this returns a series of team column
# # print(type(nba.Team))
# # but what if the column name is 2 or more words so now using new full proof method
# print(nba["Team"])             # this is main now
# #not a copy but a view only
# copy_team =nba["Team"].copy()
# print(copy_team)
# copy_team.iloc[0]="kukuron mukuron"
# print(nba["Team"]) 
# print(copy_team)

# # # 4. select multiple column

# # print(nba[["Name","Team"]])      #this is not a view but rather a copy ( inconsistancy)
# # print(type(nba[["Name","Team"]]))        #type dataframe
# col2sel=["Salary","Name","Team"]
# print(nba[col2sel])       #same but developer friendly

# # # #5. adding new columns

# # # # print(nba["Sport"])         #will throw error as column doesnt exist
# # # nba["Sport"]="Basketball"         # this will populate all the rows with basketball and column will be added last
# # # print(nba)
# # # #or much better we can do is use insert method
# # nba.insert(loc=1,column="Shape",value="mota")
# # print(nba)
# # nba["Salary Doubled"]=nba["Salary"].mul(2)
# nba.insert(loc=7,column="Salary_doubled",value=nba["Salary"]*2)
# nba.insert(loc=7,column="Salary_doubled",value=nba["Salary"]-5000000)
# print(nba)

# #6. value counts method redo
# max=nba["Team"].value_counts(normalize=True)*100
# print(max)

# # # 7. dropna method
# nba.loc[[998,1,3,4,996],"Salary"]=None                #### new way of assignment
# # print(nba)
# # # print(nba.dropna())               #default will delete total row with any missing value
# nba=nba.dropna(how="all")                 # this will remove any row with all NaN values
# # print(nba.dropna(subset=["College","Salary"]))              # this will remove any row with missing value in  subset of columns

# # 8. fillna method
# # print(nba.fillna(0))                # this will fill all missing values with zero
# nba["Salary"]=nba["Salary"].fillna(0)                 # copy thats why need to save # this affects only salary column
# nba["Weight KG"]=nba["Weight KG"].fillna(0)               # copy thats why need to save # this affects only salary column


# # 9.astype method

# nba["Salary"]=nba["Salary"].astype("int")
# nba["Weight KG"]=nba["Weight KG"].astype("int")
# print(nba)

# # 10. astype 2 categorytype for space optimization
# #nunique to find number of unique value in both series and dataframe
# print(nba.nunique())
# print(nba.info())
# nba["Team"]=nba["Team"].astype("category")
# print(nba.info())
# nba["Position"]=nba["Position"].astype("category")
# print(nba.info())
# nba["College"]=nba["College"].astype("category")
# print(nba.info())
# nba["Height"]=nba["Height"].astype("category")
# print(nba.info())
# # this helped data size from 62.5 kB to 38.8 KB

# 11. sort values method                

# nba.sort_values()                                                      # will result in error in data frame but works in series
# print(nba.sort_values(by="Name"))                                      # alphabetic default ascending sort (nan position last default)
# print(nba.sort_values(by="Name",ascending= False))                      # alphabetic descending sort (nan position last default)
# print(nba.sort_values(by="Salary"))                  # numeric descending sort (nan position last default)
print(nba.sort_values(by="Salary",ascending= False,na_position="first"))          # numeric descending sort (nan position first)

