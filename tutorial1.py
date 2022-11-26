#1
length = 1.5
width = 0.5 
perimeter = (2*length) + (2*width)
rectangle_area = length*width
print("The rectangle area is", rectangle_area, "m^2.", "The perimeter is ", perimeter, "m.")

#2
city_name = "JB"
distance = 20
mean_speed = 20
time_taken = (distance*1000)/(mean_speed*60)
print("The estimated time taken travel to " +city_name+ " is ", round(time_taken), " minutes.")

#3
s1 = s2 = s3 = 1.5
s = (s1 + s2 + s3)/2
from math import sqrt
area_of_triangle = round(sqrt(s*(s-s1)*(s-s2)*(s-s3)))
print("The area of triangle is", area_of_triangle,".")

#4
person_name = "Harianto Rahardjo"
age = 65
kim_age = 40
age_difference = age - kim_age
print("Hi Prof,", person_name, "is",age_difference,"older than Kim.")

#Solutions
''''''''
#Tutorial 1 - Question 1
length = float(input("Enter the length: ")) #key in the length
width = float(input("Enter the width: "))
area = length*length
perimeter = 2*length + 2*width #calculation of the perimeter
print("THe rectangle area is %f m^2, the perimeter is %f m."%(area,perimeter)) 

#Tutorial 1 - Question 2
city = input("City you're going to: ")
distance = float(input("How far is the city from here? (in km): "))
speed = float(input("The car speed is (in m/s): ")) #average speed
time = (distance*1000)/speed #calculation of time in seconds #make sure that your unit is consistent
ett=int(time/60) #estimated time in mins
print("The estimated travelling time in %s would be in %d minutes" %(city,ett))

#Tutorial 1 - Question 3
#key in the length
l1=float(input("Enter the first length: "))
l2=float(input("Enter the second length: "))
l3=float(input("ENter the third length: "))
# #alternative for inputting the lengths
# l1 = l2 = l3 = 1.5 #approach 1
# l1, l2, l3 = 1, 2, 3 #approach 2
#formula
s=(l1+l2+l3)/2 #calcualte the semi-perimeter
a=(s*(s-l1)*(s-l2)*(s-l3))**(0.5) #calculate the area using ** instead of math module.
print("The area of triangle is %f. " %(a))

#Tutorial 1 - Question 4
Kim_age = 40
name_expert = input("enter the person's name: ")
age_expert = int(input("enter his/her age: "))

if Kim_age > age_expert :
    print("Hi %s, I am %d years older that you."%(name_expert, Kim_age-age_expert))
else :
    print("Hi %s, I am %d years younger than you."%(name_expert, age_expert-Kim_age))