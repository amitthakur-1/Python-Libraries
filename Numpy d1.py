# 1 applying various numpy operations on the arrays sets
# import numpy as np
# arr_1d=np.array([1,2,3,4])
# print(arr_1d)
# print(type(arr_1d))
# print(arr_1d.ndim)....check arr type
# print(arr_1d.size)....size
# 2.
# Arr_2d=np.array([[1,2,3],[5,6,7]])
# print(Arr_2d)
# print(Arr_2d.ndim)
# print(Arr_2d.size)
# print(Arr_2d.shape)
# print(type(Arr_2d))

# 3
# import numpy as np
# mx_1s = np.array([[[1,1,1],[1,1,1],[1,1,1]]])
# print(mx_1s)
# print(np.ones(5))
# print(mx_1s.dtype)
# print(np.ones((3,4), dtype=int))
# mx_1s = np.zeros((4,6), dtype=bool)
# print(mx_1s)
# 4
# operations on numpy
# em_mx=np.empty
# import numpy as np
# c=np.array([1,2,3,4])
# print(c+2)
# print(c-2)
# print(c*2)
# print(c/2)
# print(c%2)
# print(c**2)
# # print(np.sqrt(c))
# print(np.sum(c))
# print(np.mean(c))
# # print(np.max(c))
# # print(np.min(c))


# BASIC SLICING TECHNIQUES:
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9,10])
# print("basic Slicing",arr[2:7])
# print("step slicing",arr[2:7:2])
# print("negative indexing",arr[-4])


# 2d array 
# SPECIFIC ELEMENT
# print(arr[1,2])
# arr=np.array([[1,2,3],[9,7,6],[21,22,34]])
# print("entire row",arr[0:,1])


# SORTING
# unsorted=np.array([3,1,4,6,4,7,9,6,5,4])
# a=np.array([[3,1,7],[3,0,4],[5,1,6]])
# print(np.sort(a,axis=1))
 # print(a)
# print(np.sort(unsorted))...basic

# 2d arr sorting
# arr_2du=np.array([[5,2,6],[8,5,9]])


# FILTER
 
# number=np.array([1,2,3,4,5,6,7,8])
# odd_numbers=number[number%2!=0]
# print(odd_numbers)
# even=number[number%2==0]
# print(even)

# filter with mask
# number=np.array([1,2,3,4,5,6,7,8,9,10])
# mask=number>5
# print(number[mask])

# fancy indexing vs np.where

# indices=np.array([1,2,3,4,5])
# b=[0,2,3]
# print(indices[b])

# # WHERE
# indices=np.array([0,2,77,5,6,22,7,4])
# where_result=np.where(indices>5)
# print(indices [where_result])


#question1 indexing
# arr = np.array([10,20,30,40,50])
# indexing=arr[1:4]
# print(indexing)

# fancy indexing
# arr = np.array([5,10,15,20,25,30])
# fancy_indexing=[0,2,4]
# print(arr[fancy_indexing])

# WHERE :
# a=np.array([12,23,34,55,88,99])
# where_condition=np.where(a>12,a*2,a)
# print(where_condition)

#  adding and remove the data
# arr1=np.array([1,2,3,4])
# arr2=np.array([4,3,5])
# combined=arr1+arr2
# print(combined)

# a=np.array(["amit","python","copy","notebooks"])
# print(a)
# e=np.char.upper(a)
# print(e)


# b=np.array(["AMIT","NOTEBOOK"])
# print(b)
# c=np.char.lower(b)
# print(c)

# a=np.array(["amit","python","copy","notebooks"])
# print(a)
# x=np.char.title(a)
# print(x)


# lenght
# import numpy as np
# a=np.array(["amit","python","copy","notebooks"])
# print(len(a))

# a=np.array(["amit"])
# b=np.arrray(["thakur"])
# print(np.array(a+b) )


# # replace method
# a=np.array(["hello world","hi world"])

# print(np.char.split(a))

# split and strip method:
# a=np.array(["hello world ","hi world    "])
# print(np.char.strip(a))

# equal meethod
# a=np.array(["name","ml"])
# b=np.array(["name","lm"])
# print(np.char.equal(a,b))


# Create a NumPy array with numbers 1 to 10 and find:  Sum  Mean  Maximum Minimum
# import numpy as np
# a=([1,2,3,4,5,6,7,8,9,10])
# b=([1,2,3,4,5,6,7,8,9,11])
# print(np.sum(a))
# print(np.mean(a))
# print(np.max(a))
# print(np.min(a))
# print(np.minimum(a,b))
# print(np.maximum(a,b))
# print(np.add(a,b))
# print(np.subtract(a,b))
# print(np.multiply(a,b))
# print(np.divide(a,b))

# find even numbers form 1 to 20
# arr=np.arange(1,21)
# x=arr[arr%2==0]
# print(x)

# 3*3 array
# arr=np.array([[1,23,233],[22,233,44],[434,41,55]])
# v=(np.sum(arr,axis=0))
# v=(np.sum(arr,axis=1))
# print(v)

# import random
# a=np.random.randint(1,11,10)
# b=np.sum(a)
# print(np.std(b))
# print(np.var(b))

# a=np.array([1,2,3,4,5])
# print(np.square(a))
  
# arr=np.arange(1,13)
# print(arr.reshape(3,4))


# A=np.array([1,2,3])
# B=np.array([4,55,6])
# c=np.dot(A,B)
# print(c)

# S =np.array(["string","amit"])
# print(np.char.upper(S))
# print(np.char.lower(S))

# arr=np.array(["Banana and Mango"])
# print(np.char.count(arr,"a"))


# arr=np.array(["Python"])
# print(np.char.replace(arr,"Python","java"))

# strin=np.array(["Hello123"])
# print(np.char.isalnum(strin))
# print(np.char.isalpha(strin))


# aae=np.array(["artificial intelligence"])
# print(len(aae[0]))
# print(np.char.str_len(aae))


# stri=np.array(["apple,banana,grapes,mango"])
# print(stri.split(","))

# arr=[12,23,34,22,21,66]
# first=max(arr)
# arr.remove(first)
# second=max(arr)
# arr.remove(second)
# result=first+second
# print(result)

# # OR------
# arr2=[1,223,4,3,3,22,2]
# result=(sum(sorted(arr2)[-1:]))
# print(result)

# filter
# numbers=np.array([1,2,3,4,5,6])
# even_numbers=numbers[numbers%2==0]
# print(even_numbers)

# simple making of an array  using numpy 1d array
# import numpy as np
# list1=[10,20,30,40,50]
# array1=np.array(list1)
# print(array1)
# or
# arr=np.array([12,23,12])
# print(arr)

# 2d array

# arra=np.array([[12,13,15,16],[34,45,45],[22,33,45,22,88,45]],dtype=object)
# print(type(arra))
# print(arra.dtype)


# print(np.dtype(np.int16))



# Create a NumPy array of numbers from 1 to 10
# arr=np.arange(1,11)
# print(arr)

# Create a 3×3 matrix filled with zeros
# arr=np.zeros([3,3])
# print(arr)


# Create a 2×4 matrix filled with ones
# ar=np.ones((2,4))
# print(ar)

# Create an array with values from 10 to 50 (step 5
# arr=np.arange(10,51,5)
# print(arr)

# Find:shape,size,datatype of an array
# arr=np.array([[2,3,4,],[3,4,5],[12,34,45],[12,23,34]])
# print(np.shape(arr))
# print(arr.dtype)
# print(arr.size)


# Reshape a 1D array of 12 elements into 3×4
# arr=np.arange(1,13)
# print(arr.reshape(3,4))



# Access:first element,,last element,middle element
# ar=np.arange(1,4)
# print(ar[0])
# print(ar[-1])
# print(ar[-2])

# Slice elements from index 2 to 7

# a=np.arange(1,9)
# print(a[2:7])

# random generation on elements
#  import numpy as np
# A = np.random.randint(1, 10, (1, 3, 4))
# result = A 
# print(result)


# A=np.array([[1,2],[3,4]])
# B=np.array([[4,5],[5,6]])
# print(np.dot(A,B))....dot product of two numbers

# create an array filled with a specific value
# print(np.full((3,3),9))


# print(np.eye(3))

# print(np.random.rand(3,4))
# print(np.random.randn(3,3))
# print(np.random.randint(1,10,(3,3)))

# arr=np.array([1,2,3,4,5,6,7,8])
# print(np.split(arr,4))

# # list and Numpy Array
# list1=[1,2,3,4]
# array1=np.arange(1,5)
# print(list1)
# print(array1)
# print("list addition: ",list1+list1)
# print("array addition",array1+array1)
# list1=[1,2,3,4]
# array1=np.arange(1,5)
# print("multiplication: ",list1*2)
# x=[x*2 for x in list1]
# print(x)
# print("multiplication: ",array1*2)

# brodcasting the numpy
# a=np.array([[1,2,3],[4,5,6]])
# b=np.array([1,2,3])
# c=a+b
# print(c)


# arr=np.array([[1,2],[3,4]],order='C')
# print(arr.flatten(order='C'))
# print(arr.flatten(order='F'))

# a=np.random.rand(30)
# print(a)


# Task 4: NumPy Operations
# Task
# Create array and find: Sum,Mean,Max, Reshap
# ar=np.array([1,2,3,4])
# print(sum(ar))
# print(np.mean(ar))
# print(np.max(ar))
# print(np.reshape(ar,(2,2)))


# Task 5: Filter Data:Filter students,Age > 20Marks > 80
# name=np.array(['A','B','C','D','E'])
# age=np.array([20,21,22,23,19])
# marks=np.array([80,90,89,98,33])

# condition=(age>20) & (marks>80)
# filtered_names=name[condition]
# filtered_age=age[condition]
# filtered_marks=marks[condition]
# print(filtered_age)
# print(filtered_marks)
# print(filtered_names)

# GroupBy Task:Task,Find average salary per department


# Create a dataset of students with marks in 3 subjects. Perform:
# Total marks
# Average marks
# Highest scorer
# Students with average > 75
# import pandas as pd
# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["A", "B", "C"],
#     "Hindi": [45, 78, 88],
#     "English": [56, 82, 91],
#     "Maths": [77, 85, 95]
# })

# df["Total"] = df[["Hindi", "English", "Maths"]].sum(axis=1)

# df["Average"] = df["Total"] / 3

# top_student = df.loc[df["Total"].max()]
# print(top_student)
# result = df[df["Average"] > 75]
# print(result)


# : Sales Data Analysis
# Analyze sales data:
# Total sales
# Monthly average
# Best month
# Month with sales < 2000


# import pandas as pd

# df = pd.DataFrame({
#     "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
#     "Sales": [1500, 2200, 1800, 3000, 2500]
# })

# total_sale=df["Sales"].sum()
# print(total_sale)
# df["total_sale"]=df["sales"].sum()
# print(df)


# full=np.full((2,2),7)
# print(full)

# random=np.random.random((2,3))
# print(random)

# sequence=np.arange(0,11,1)
# print(sequence)


# VECTOR TENSOR AND MATRIX
# vector=np.array([1,2,3,4,5])
# print(vector)


# metrix 2d array

# matrix=np.array([[1,2,3],[3,4,5]])
# print(matrix)


# tensor" means dimensions are multiple
# tensor=np.array([[[1,2],[3,4]],[[12,13],[13,14]],[[21,22],[23,24]]])
# print(tensor)
# print(tensor*2)
# print(tensor.ndim)


# properties of array:

# arr=np.array([[1,2,3],[4,5,6]])
# print(arr.shape)
# print(arr.ndim)
# print(arr.size)
# print(arr.dtype) 

# ARRAY RESHAPING
# arr=np.arange((8))
# print(arr)
# reshaped=arr.reshape((3,4))
# print(reshaped)

# flattened=reshaped.flatten()....prints a copy
# print(flattened)

# ravel method: returns a original
# raveled=reshaped.ravel()
# print('raveled:',raveled)
 
# transpose : row to columns .

# arr=np.array([[1,2,3,4],[2,3,4,5]])
# new=arr.T
# print(new)









