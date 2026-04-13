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
import numpy as np
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


