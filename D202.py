import math
a=int(input())
for i in range(1, a+1):     #from 1 to a
    if math.fmod(a,i) ==0:          #if the remainder is 0, then i is a factor of a
        print(i)
