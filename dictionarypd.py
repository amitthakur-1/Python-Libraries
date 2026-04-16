# import pandas as pd
# data={
#     "name":["amiy","vishal","numan","aman","gimini","vihal","xy","ab","sfd","asa"],
#     "age":[12,23,45,23,2,4,3,4,2,23],
#     "salary":[120000,233000,2320044,2,33,44,33,44,22,44],
#     "day":[12,23,1,1,2,4,5,3,6,6],
#     "number":[1,2,3,4,5,6,7,8,9,10]

# }


# df=pd.DataFrame(data)
# print(df)
# print(df.head(2))....print the values upto given index
# print(df.tail())
# print(df.info())  
# print(df.describe()).....avg, max,mean values


# print(df.loc())
# print(df.iloc())
# print(df.drop(2))
# # print(df.fillna())
# print(df.sort_values(1))
# print(df.count())
# df["age"]=df["age"].apply(lambda x:x+1)



import pandas as pd
d=pd.read_csv("D:\Book1.csv")
print(d)
df=pd.DataFrame(d)
print(df)
print(df.head())
print(df.tail())
print(df.info())  
print(df.describe())
print(df.loc())

