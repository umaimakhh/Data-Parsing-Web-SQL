'''
Assigment No:0801 -  
Name: Umaima Khurshid Ahmad
Date: 02/23/2021
'''
import pandas as pd
filePath = 'E:/DPU/Employee.txt'
paramnames =['fNam','LName','MName','phone','DOB','address','gender','salary','SSN','hours']
readFile = pd.read_csv(filePath,names=paramnames)

#a.	Find all male employees
df=pd.DataFrame(readFile)
# print(df)
is_Male =  df['gender']=='M'
intialValue=df[is_Male]
print("/nFind all male employees /n")
print(intialValue)


# Q1 b -- lowest salary by female
is_Female = df['gender']=='F'
dept_gender_salary =  df.groupby([is_Female]).salary.min()
print("/n /n Lowest Salary of female is against True")
print(dept_gender_salary)


#c #aggreation
print("/n /n Out salary groups by middle initial")
intialValue=df['salary'].groupby(df['LName'])
for groupVal,groupname  in intialValue:
    print(groupVal)
    print(groupname)

#composition
# valurCom=df['salary'].groupby(df['salary','LName'])
# intialValue=df['salary'].groupby(df['LName'])
# for groupVal,groupname  in valurCom:
#     print(groupVal)
#     print(groupname)
