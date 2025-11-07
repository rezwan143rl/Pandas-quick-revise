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
#2. filtering 
print(employee[employee["Gender"] == "Male"]) # this gives all male employes
# print(employee[employee["Team"] == "Finance"]) # this gives all finance team member
on_finance_team=employee["Team"] == "Finance"
print(employee[on_finance_team]) # this do same
# print(employee[employee["Senior Management"]]) # as its already bolean series dont need to compare
print(employee[~employee["Senior Management"]]) # as its already bolean series dont need to compare ' ~ ' this means not or false
print(employee["Salary"].max()) # as its already bolean series dont need to compare ' ~ ' this means not or false
print(employee[(employee["Salary"]>=140000)]) 
print(employee[(employee["Bonus %"]<1.5)]) 
print(employee[(employee["Start Date"]< "1990-01-01")]) 
print(employee[(employee["Last Login Time"]> dt.time(10,30))]) # for time we need the datetime library 
print(employee[(employee["Last Login Time"] == dt.time(12,20))]) # for time we need the datetime library 
