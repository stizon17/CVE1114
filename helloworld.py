print ("hello world")
print ("it works")
print("saved the code")

print (100)
print(123456+12)
print (type(100))

print (4.2)
print (.2)
print (type(0.2))

print ("I am a string")
print (type('I am a string'))

print("hi"*5)

print("this string contains a single quote(')character")

print ('a\
    b\
    c')

a = 5
b= 10
print (a>b)
print (a<b)
print (type(a<b))

print (not 5<10)

n=200
print (n)

a=b=n=200
print (a)
print (b)
print (n)

# a=100
# b=200
# c=300

a,b,c=100,200,300
print (a)
print (b)
print (c)

temp_today = 36.5
print (temp_today)
temp = "my temp is 36.5"
print (temp)

age = 49
Age = 59
AGE = 69
agG = 79
print (age,Age, AGE, agG)

name = "puppy"
age = 10
hobby = "going for a walk"

print ("My dog is " + name)
print (name + " is " +str(age)+ " years old, love to "+ hobby)

# help("keywords")

# this is a comment. Python cannot read this comment.
print("but this works")

stop1 = "Pasir Ris"
stop2 = "Changi Airport"
stop3 = "Tuas Link"

print ("Train to " ,stop1, " is now approaching")
print ("Train to " ,stop2, " is now approaching")
print ("Train to ", stop3, " is now approaching")

a = 10
b = 20
c = a + b # 30
d = c - 5 # 25
print (a,b,c,d)

print (+a) # 10
print (-b) # -20
print (a*b) # 200
print (b/a) # 2.0
print (b%a) # 5
print (type (b/a)) # class, in or float ?
print (a*15+c) #180

# comparison numbers
a = 10
b = 20
print (a==b)
print (a != b)
print (a<=b)
print (a>=b)

x =1.1 +2.2
print (x ==3.3) #True

tol = 1e-5
print (abs(x-3.3)<tol)

a =5
print (a<10 or a <4)
print (type(a<10))

print (20+4*10) #240 or 60?

num  = 20+4*10 #240 o r 60?
print (num)

num = num +2 # num +2
print (num)

num += 2 #64
print (num)

print (round(2.5)) #3
print (round (3.5)) #4

print (round (4.5)) #5

print (pow(2,2))

# from math import *
# print (floor(4.99))
# print (pi)
# print (sqrt(16))

import math
print (math.floor(4.99))
print (math.pi)
print (math.sqrt(16))

from random import *
print (random())
print (random()*10)
print(int(random()*10)+1)

from random import *
date = randint (4,28) #requirement 1 (except for 1st, 2nd, 3rd)
print ("the face to face tutorial is on", str(date), "of every month")