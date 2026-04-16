import pandas as pd
# data=pd.Series([10,20,10],index=["a","b","c"])
# print(data["b"])
# print(data+5)
# 2.
# data={
#     "name":["amit","rahul"]
#     ,"age":[12,23]
# }
# df=pd.DataFrame(data)
# print(df["name"])
# df["marks"]=[52,51]


# df["total"]=df["age"]+df["marks"]
# print(df)


# print(df[df["total"]>65])

# to find the max , mean,sum
# lis=pd.DataFrame([5,10,15,20,25])
# print(lis.sum())
# print(lis.mean())
# print(lis.max())

# s=pd.Series([100,200,300],index=['a','b','c'])
# print(s['b'])

# import pandas as pd
# import numpy as np

# s=pd.Series([10,20,40])
# print(s)... this is single d called series


# by giving own index
# a=pd.Series([1,2,3],index=["a","b",'c'])
# print(a)

# creating a data frame 2d data , data_range
# data=pd.DataFrame({"name":["alice","bob"],"age":[23,34]
# })
# print(data)



# example :
# a= pd.DataFrame({"name":['amit','rahul','abhi','ram','sham','mohan','monty'],"class":[12,33,77,88,23,34,45]})
# print(a)
# print(a.head())....print the heads 5
# print(a.tail())....print the tail 5
# print(a.shape)... to print the number of rows and columns
# print(a.columns)
# print(a.dtypes)
# print(a.loc[2]) to locate the row and columns
# print(a.loc[[2,4]])....return two rows

# addd a list of names in the given rows:
# data=pd.DataFrame( {"calories":[100,200,400],"e.things":['pizza','burger','momo']},index=["day1","day2","day3"])
# data.index.name="S.No."
# data=data.reset_index()
# print(data)

# print a label 
# a=pd.DataFrame({"name":["amit":12,"aman":23,"sub":23})
# print(a)

# Sample DataFrame as a dataset usage
# data = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie','Tork','Gill','Ben','Cork','Tkin','Bin','Champ'],
#         'Age': [25, 30, 35, 20, 17, 23, 25, 27, 43, 32],
#         'City': ['NY', 'LA', 'SF', 'IN', 'DL', 'NZ', 'SA', 'CH', 'HR', 'WI']})
# print(data)


# create a dataset
# data = pd.DataFrame({'Name': ['Alice', 'Bob','Charlie','Tork','Gill','Ben','Cork','Tkin','Bin','Champ'],
#         'Age': [25, 30, 35, 20, 17, 23, 25, 27, 43, 32],
#         'City': ['NY', 'LA', 'SF', 'IN', 'DL', 'NZ', 'SA', 'CH', 'HR', 
# 'WI']})
# print(data)


# data cleaning
# data=pd.DataFrame({"name":["aman",None,"amish","nish"],"class":[12,23,34,None]})
# print(data.isnull())
# print(data.isnull().sum())

# fill missing values with a specific values
# data=pd.DataFrame({"Name":
# ["Ankit","Navdeep","Mohnish","Ankit","Ritesh","Ishika"],
#       "Age":[23,None,19,23,None,18],
#       "Salary":[2000,3000,8000,2000,5000,6000]})
# print(data)
# print("\nage column after filling missing values with 0: ")
# print(data['Age'].fillna(0))
# print("\n filling with mean: ")
# print(data['Age'].fillna(data['Age'].mean()))
# print("\n filling the missing values with median")
# print(data['Age'].fillna(data["Age"].median()))
# print("\n printing the mode into the missing value 0")
# print(data['Age'].fillna(data["Age"].mode()[0]))

# data cleaing
# data=pd.DataFrame({"Name":["Ankit","Navdeep","Mohnish","Ankit","Ritesh","Ishika"],
#       "Age":[23,None,19,23,None,18],
#       "Salary":[2000,3000,8000,2000,5000,6000]})
# #print(data)
# print(data.isnull().sum())

# s=pd.Series([10,20,30,40])
# print(s)

# data={
#     "name":["ramesh","aksas","ryery"],
#     "age":[21,23,34]

# }
# df=pd.DataFrame(data)
# print(df)


# s=pd.Series([12,23,34,4,55,56],index=["AMIT","AMAN","MANISH","ASHISH","KASH","JCD"],dtype=float)
# print(s[0])
# print(s.min())
# print(s.max())


# s=pd.Series(0.5,index=[0,1,2])
# print(s)


# s=pd.Series([12,23,34])

# print("addition")
# print(s+10)
# print("multiplication")
# print(s*2)
# print("subtraction")
# print(s-10)
# print("division")
# print(s/2)

# list with pd
# import pandas as pd
# data=[["amit",31,30000],["nitin",122,23223231],["raman",23435,53534253]]
# df=pd.DataFrame(data)
# print(df)
# print(type(df))

# s=pd.Series([12,23,34])
# d=pd.Series([44,5,21])
# print("addition")
# print(s+d)
# print("subtraction")
# print(s-d)
# print("multiplication")
# print(s*d)
# print("maximum")
# print(s.combine(d,max))
# print("minimum")
# print(s.combine(d,min))
# print("square")
# print(s.combine(d,pow))


