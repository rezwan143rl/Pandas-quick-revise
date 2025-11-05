import pandas as pd
import numpy as np

employee =pd.read_csv("CSV/employees_1000.csv",parse_dates=["Start Date"],date_format="%m/%d/%Y") 

print(employee.info())
print(employee.nunique())
employee["Gender"]=employee["Gender"].astype("category")
employee["Senior Management"]=employee["Senior Management"].astype("boolean")
employee["Team"]=employee["Team"].astype("category")
# employee["Start Date"]=pd.to_datetime(employee["Start Date"],format="%m/%d/%Y",yearfirst=False) # done automatically in read csv
employee["Last Login Time"]=pd.to_datetime(employee["Last Login Time"],format="%H:%M %p").dt.time

print(employee.info())