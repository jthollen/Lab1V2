# Programmers: John Hollen

# Course: CS151, Prof. Mehri

# Date: 9/22/2021

# Lab Number: 1

# Program Inputs: Volume in mL

# Program Outputs: The equivalent in Table spoons and tea spoons from the given volume in mL

volume_ML = float(input("What is the volume in mL?:"))
tea_Spoon = volume_ML / 5
table_Spoon = 0
if tea_Spoon >= 3:
    table_Spoon = tea_Spoon // 3
    tea_Spoon = tea_Spoon % 3
tea_Spoon = round(tea_Spoon)
print("Table Spoons = ", table_Spoon)
print("Rounded Tea Spoons = ", tea_Spoon)
