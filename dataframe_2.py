import pandas as pd
import numpy as np
import datetime as dt

employee =pd.read_csv("CSV/employees_1000.csv",parse_dates=["Start Date"],date_format="%m/%d/%Y") 

print(employee.info())
print(employee.nunique())
employee["Gender"]=employee["Gender"].astype("category")
employee["Senior Management"]=employee["Senior Management"].astype("boolean")
employee["Team"]=employee["Team"].astype("category")
# employee["Start Date"]=pd.to_datetime(employee["Start Date"],format="%m/%d/%Y",yearfirst=False) # done automatically in read csv
employee["Last Login Time"]=pd.to_datetime(employee["Last Login Time"],format="%H:%M %p").dt.time
print(employee)


# #2. filtering                     
# print(employee[employee["Gender"] == "Male"])                     # this gives all male employes
# # print(employee[employee["Team"] == "Finance"])                  # this gives all finance team member
# on_finance_team=employee["Team"] == "Finance"
# print(employee[on_finance_team]) # this do same
# # print(employee[employee["Senior Management"]])                  # as its already bolean series dont need to compare
# print(employee[~employee["Senior Management"]])                   # as its already bolean series dont need to compare ' ~ ' this means not or false
# print(employee["Salary"].max())                   # as its already bolean series dont need to compare ' ~ ' this means not or false
# print(employee[(employee["Salary"]>=140000)]) 
# print(employee[(employee["Bonus %"]<1.5)]) 
# print(employee[(employee["Start Date"]< "1990-01-01")]) 
# print(employee[(employee["Last Login Time"]> dt.time(10,30))])                    # for time we need the datetime library 
# print(employee[(employee["Last Login Time"] == dt.time(12,20))])                  # for time we need the datetime library 

# # # 3. and for filtering
# # #female employes who work for marketing
# # is_female=employee["Gender"]=="Female"
# # is_in_marketing=employee["Team"]=="Marketing"
# # print(employee[is_female & is_in_marketing])
# #female employes who work for marketing who earn over 100k a year
# is_female=employee["Gender"]=="Female"
# is_in_marketing=employee["Team"]=="Marketing"
# is_more_than_100k=employee["Salary"]>100000
# print(employee[is_female & is_in_marketing & is_more_than_100k])

# #4. orlogic
# # who are either senior management or started before 1st jan 2000
# # is_before_2000=employee["Start Date"] < "2000-01-01"
# # print(employee[employee["Senior Management"] | is_before_2000])
# is_robert_client= (employee["First Name"]=="Robert") & (employee["Team"] =="Client Services")
# is_after_2016=employee["Start Date"]>"2016-01-01"
# print(employee[is_robert_client | is_after_2016])

# #5. isin method

# print(employee["Team"].isin(["Marketing","Product"]))                 # this gives boolean series
# print(employee[employee["Team"].isin(["Marketing","Product"])]) #

# # 6. isnull / notnull
# team_is_null=employee["Team"].isnull()
# team_is_not_null=employee["Team"].notnull()
# first_name_null = employee["First Name"].isnull()
# print(employee[team_is_null])
# print(employee[team_is_not_null])
# print(employee[first_name_null | team_is_not_null])

# # 7. between method
# sal_between = employee["Salary"].between(90000,120000) 
# print(employee[sal_between])
# date_between =employee["Start Date"].between("2000-01-01","2020-01-01")
# print(employee[date_between])
# time_between=employee["Last Login Time"].between(dt.time(9,30),dt.time(10,30))
# print(employee[time_between])

# # 8. duplicated method
# # print(employee["First Name"].duplicated())                          # returns a boolean series duplicates are true 
# duplicates=employee["First Name"].duplicated()
# duplicates_first=employee["First Name"].duplicated(keep="first")                          # top down default
# duplicates_last=employee["First Name"].duplicated(keep="last")                            # bottom up approach last values will be considered original
# print(employee[duplicates])                           # this returns which are duplicates 
# print(employee[~duplicates])                          # this returns which are not duplicates 
# print(employee[~duplicates_last])                             # this returns which appeared last
# print(employee[employee["First Name"].duplicated(keep=False)])                            # only gives which are uniquese
# print(employee[~employee["First Name"].duplicated(keep=False)])                           # only gives which has no duplicates or unique

# # 9. DROP_DUPLICATES METHOD
# print(employee.drop_duplicates())               # this will check row wise if 2 row is same then it will drop the other occurances , it also has keep argument
# print(employee.drop_duplicates(subset=["Team"]))
# print(employee.drop_duplicates(subset=["Team"],keep="first")) # default
# print(employee.drop_duplicates(subset=["Team"],keep="last")) # bottom up
# print(employee.drop_duplicates(subset=["Team"],keep=False)) # no duplicates or original only unique should be showed if no unique then empty 
# print(employee.drop_duplicates(subset=["First Name"],keep=False)) # no duplicates or original only unique should be showed if no unique then empty 
# print(employee.drop_duplicates(subset=["Senior Management","Team"]).sort_values("Team")) # each time 2 unique of sm and 2 occurances of team . cause checking two
# print(employee.drop_duplicates(subset=["Senior Management","Team"],keep="last").sort_values("Team")) # each time 2 unique of sm and 2 occurances of team . cause checking two

# 10. unique and n unique
#unique method works as catergoric better used in series
print(employee["Gender"].unique()) # this returns number of category as a list
print(employee["Team"].unique()) # this returns number of category as a list
print(employee["Team"].nunique(dropna=True)) # this returns number of unique values by dropping nan(default)
print(employee["Team"].nunique(dropna=False)) # this returns number of unique values by dropping nan
print(employee.unique()) # error as dataframe has no unique method
print(employee.nunique()) # this you know
