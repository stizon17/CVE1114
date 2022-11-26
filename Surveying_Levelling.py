from curses.ascii import isblank
from re import T
import pandas as pd
import os

#for importing of excel initially created to include data we collected as a group
df = pd.read_excel('/Users/stephtizon/Downloads/Levelling.xlsx', sheet_name= "Sheet1",  engine='openpyxl')
print(df)

import numpy as np


Rise_and_Fall_method_details  = {
    "Backsight": [1.478, 1.316, 1.715, 1.276], 
    "Foresight": [0.000, 1.445, 1.230, 1.2326, 1.875],
    "Rise": [0.000, 0.033, 0.086, 0.479, 0.000],
    "Fall": [0.000, 0.000, 0.000, 0.000, 0.599]
}

import math

Backsight = [1.478, 1.316, 1.715, 1.276]
Foresight = [1.445, 1.230, 1.2326, 1.875]
Rise = [0.033, 0.086, 0.479]
Fall = [0.599]

#If we were to put the numbers calculated as "floats":

print(float(sum(Backsight)))
print(float(sum(Foresight)))

Arithmetic_Check_1 = float(sum(Backsight)) - float(sum(Foresight))
Arithmetic_Check_2 = float(sum(Rise)) - float(sum(Fall))

#To check if Total BS- Total FL = Total Rise - Total Fall ; setting it to integers

if Arithmetic_Check_1 == Arithmetic_Check_2:
    print("Results acceptable")
else:
    print("Results unacceptable")

print(Arithmetic_Check_1)
print(Arithmetic_Check_2)

#However, if we were to put the numbers as "integers"

print(int(sum(Backsight)))
print(int(sum(Foresight)))

Arithmetic_Check_3 = int(sum(Backsight)) - int(sum(Foresight))
Arithmetic_Check_4 = int(sum(Rise)) - int(sum(Fall))

#To check if Total BS - Total FS = Total Rise - Total Fall ; setting it to float types.

if Arithmetic_Check_3 == Arithmetic_Check_4:
    print("Results acceptable")
else:
    print("Results unacceptable")

print(Arithmetic_Check_3)
print(Arithmetic_Check_4)

Reduced_Level = np.array([10.000, 10.033, 10.119, 10.598, 9.999])
print(Reduced_Level[0], Reduced_Level[-1])

RL_Arithmetic_Check = Reduced_Level[0] - Reduced_Level[-1]

if RL_Arithmetic_Check == Arithmetic_Check_1:
    print("OK")
else:
    print("NOT OK")

print(RL_Arithmetic_Check)


from openpyxl import workbook
from datetime  import datetime
import xlsxwriter
import datetime

# For exporting the final RL to a new excel sheet, containing the final values

workbook = xlsxwriter.Workbook("/Users/stephtizon/Downloads/Final_RL.xlsx")
worksheet  = workbook.add_worksheet('Sheet_1')

#exporting of final data onto an excel sheet (as per isntructed)

Final_Backsight = [1.478, 1.316, 1.715, 1.276]
for row_num, data in enumerate(Final_Backsight):
    worksheet.write(row_num+1, 0, data)

Final_Foresight = [ " ", 1.445, 1.230, 1.2326, 1.875]
for row_num, data in enumerate(Final_Foresight):
    worksheet.write(row_num+1, 1, data)

Final_Rise = [ "  ", 0.033, 0.086, 0.479, "  "]
for row_num, data in enumerate(Final_Rise):
    worksheet.write(row_num+1, 2, data)

Final_Fall = [" " , " ", " ", " ", 0.599]
for row_num, data in enumerate(Final_Fall):
    worksheet.write(row_num+1, 3, data)

Final_RL = [10.000, 10.033, 10.119, 10.598, 9.999]
for row_num, data in enumerate(Final_RL):
    worksheet.write(row_num+1, 4, data)


my_list = ["Backsight (m)", "Foresight (m)", "Rise (m)", "Fall (m)", "Reduced Level (RL)", "Remarks"]
for col_num, data in enumerate(my_list):
    worksheet.write(0, col_num, data)

Points = ["801-NL", "802-NL", "1000-NL", "1002-ML", "801-NL"]
for row_num, data in enumerate(Points):
    worksheet.write(row_num+1, 5, data)

worksheet.write(7,0,"Arithmetic Check:")
worksheet.write(8,0, "Backsight - Foresight")
worksheet.write(8,2, "Rise - Fall")


Final_BS_FS_data = sum(Backsight) - sum(Foresight)
worksheet.write(8, 1, Final_BS_FS_data)

Final_RS_FS_data = sum(Rise) - sum(Fall)
worksheet.write(8, 3,Final_RS_FS_data)

worksheet.write(8, 5, RL_Arithmetic_Check)

worksheet.write(8,4, "Last RL - First RL")

workbook.close()