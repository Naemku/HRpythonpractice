from math import *
length_AB=int(input())
length_BC=int(input())
print("{}°".format(round(atan(length_AB/length_BC)*180/pi)))
