import math
a=int(input())
b=int(input())
C=int(input())   #input the 3 values
d=round(0.5*a*b*math.sin(math.radians(C)),3)     #formula for area of triangle, changing the radian measure to degree
e="{:.3f}".format(d)   #to ensure the number ends with 3 decimal places
print(d)
