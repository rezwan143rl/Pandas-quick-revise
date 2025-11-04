import pandas as pd
import numpy as np 

job = pd.read_excel("excel/data_jobs_salary_all.xlsx")
# print(job.nunique())
#data resizing
# print(job.info())

job["job_title_short"]=job["job_title_short"].astype("category")
job["job_schedule_type"]=job["job_schedule_type"].astype("category")
job["job_work_from_home"]=job["job_work_from_home"].astype("category")
job["job_no_degree_mention"]=job["job_no_degree_mention"].astype("category")
job["job_health_insurance"]=job["job_health_insurance"].astype("category")
job["salary_rate"]=job["salary_rate"].astype("category")
print(job.info()) # saved 0.6 mb

