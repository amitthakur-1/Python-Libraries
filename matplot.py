
# xpoints=np.array([0,6])
# ypoint=np.array([0,25])
# plt.plot(xpoints,ypoint)
# plt.show()
# x=[1,2,3,4]
# y=[10,20,30,40]
# plt.plot(x,y,
#color='magenta',
#inewidth=7,
#linestyle='-',
#marker='o',
#markersize=9,
#label='sales')
# plt.title("Sales Graph")
# plt.xlabel("Days")
# plt.ylabel(True)
# plt.legend()
# plt.show()


# 1. Student Data Analysis
# Create a DataFrame with student marks
# Calculate:
# Average marks
# Highest marks
# Plot a bar chart of marks
# import matplot as plt
# import matplotlib.pyplot as plt

# import pandas as pd
# df=pd.DataFrame({"Student":['amit','aman','manan','dheeraj'],"marks":[45,56,67,88]})
# print(df)
# avg_marks=df["marks"].mean()
# print("\n the average is  :",avg_marks)
# Highest_marks=df["marks"].max()
# print(" the highest marks are: ",Highest_marks)
# plt.plot(df["Student"],df["marks"],marker='x')
# plt.xlabel("Students")
# plt.ylabel("marks")
# plt.title("student marks")
# plt.show()

# 2. Create monthly sales data using NumPy
# Convert into Pandas DataFrame
# Plot:
# Line chart (sales trend)
# Bar chart (monthly sales)

# import numpy as np
# Month=np.array(["JAN","FEB","MARCH","APRIL","MAY"])
# Sales=np.array([3000,4000,5000,6000,2500])
# df=pd.DataFrame({"Sales":Sales,"Month":Month})
# print(df)
# plt.plot(df["Month"],df["Sales"],marker="o")
# plt.xlabel("Sale")
# plt.ylabel("Month")
# plt.title("Monthly Sales of Shop")
# plt.show()

# 3. Student Performance Analyzer
# Objective:
# Analyze student marks using NumPy, Pandas, and Matplotlib
# Student_name=np.array(["amit","raman","nish","pawan"])
# Student_marks=np.array([54,35,74,56])
# df=pd.DataFrame({"Student_name":Student_name,"Student_marks":Student_marks})
# print(df)
# plt.plot(df["Student_name"],df["Student_marks"],marker='x')
# plt.xlabel("marks")
# plt.ylabel("names")
# plt.show()



# Project: Employee Salary Analyzer 
#  Objective
# Analyze employee salary data to find insights like:
# Average salary
# Highest & lowest salary
# Department-wise analysis
# Visualization of salary distribution
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# Employee_Dept=np.array(["COMPUTERS","SALES","MARKETING","HR"])
# Employee_Salary=np.array([23000,34000,43000,12000])
# df=pd.DataFrame({"emp_dept":Employee_Dept,"emp_salary":Employee_Salary})
# print(df)
# Average_salary=df["emp_salary"].mean()
# Highest_salary=df["emp_salary"].max()
# Lowest_salary=df["emp_salary"].min()
# print("\n Average salaries: ",Average_salary)
# print("Highest salary: ",Highest_salary)
# print("Lowest salary: ",Lowest_salary)

# plt.plot(df["emp_dept"],df["emp_salary"])
# plt.xlabel("DEPARTMENTS")
# plt.ylabel("SALARIES")
# plt.title("DEPARTMENT WISE SALARIES OF EMPLOYEES")
# plt.show()

import pandas as pd
data=("amit0","deepak","ravi","neha")

