from random import random


sen = "I am Stephanie"
print(sen)
sen2 = 'I teach Python'
sen3 = """
I am here to teach
WIll end soon"""
print(sen3)

s="I"
t="am"
u="Stephanie"

print(s+t+u)
print(s*5)
print(t*5)
print(s*-8)

print(ord("a"))
print(chr(97))

print(len(u))
print(u[0])
print(u[len(u)-1])

s="Kim Yongmin"
print(s[0:3])
print(s[:3])
print(s[0:])

print(s[0:4]+s[4:] ==s) #Kim_ 
print(s[4:]) # _Yongmin

Kor_id = "840519-1xxxxxx"
print("sex: " ,Kor_id[7])
print("Year: " +Kor_id[0:2])
print("Month: " ,Kor_id[2:4])
print("Day: "+Kor_id[4:6])

print("Kim's Ko id: "+Kor_id[:7])

s = "Python is Amazing. on on"
print(s.upper()) #All capitalize
print(s.title()) 

print(s.count("on"))
print(s.count("on" ,0,10))

print(s.find("on"))
print(s.find("are"))

print(s.index("on"))
#print(s.index("are"))

print("I am {} years old".format(40))

age = 38
print(" I am {} years old" .format(age))

col = "Blue"
col2 = "Red"

print("My favourite colours are {} and {}." .format(col, col2))
print("My favourite colours are {0} and {1}." .format(col, col2))
print("My favourite colours are {1} and {0}." .format(col, col2))
print("My favourite colours are {col} and {col2}." .format(col="Yellow", col2="Black"))

quantity = 6
item = "banana"
price = 2.5
print(f"{quantity} {item} cost SGD {price}")
print("{} {} cost SGD {}" .format(6, "banana", 2.5))

print("Yongmin\tkim")
print(r"Yongmin\tkim")

# 4.7 Activity
## Passcode generation program by Pythom
url = "http://glasgow.ac.uk"
pass_url = url.replace("http://", "") # req 1
print(pass_url)
pass_url = pass_url[:pass_url.index(".")] #req 2

passcode = pass_url = pass_url[0:3] + str(len(pass_url)) + str(pass_url.count("a")) + "!"
print(passcode)

print("the passcode of {} is {}" .format(url, passcode))


#5.1 Activity -> Python Lists
a = ["yongmin", "Hezhen", "Yating", 1, 2,3.14, True] #strings
print(a)
a[2] = 10
print(a)
a[-1] = 20
print(a)
del a[5]
print(a)

MRT=["kim", "Lee", "Park"]
MRT .append("Andrew")
print(MRT)

MRT .append("Andrew")
print(MRT)

MRT  = MRT + ["John"]
print(MRT)

Loc = {1:"Kim", 2:"Lee", 3:"Park"}
print(Loc.keys())
print(Loc.values())
print(Loc.items())

Java = {"Kim", "Park", "Lee"}
Python = set(["Andy", "john", "Moham"])
print(Java)
print(Python)

Java.add("Son")
Python.add("Son")

print(Java | Python)
print(Java.union(Python))

# 5.6 ACtivity
## Coding competition will be held in Glasgow.
## In otder to promote the competition, luckydraw will take place.
## One participant will wawrd a cupon for KOREAN BBQ.
## # PArticipant will wawrd cupons for STarbuck coffee.

from random import *
part = range(1, 21) #from 1-20
print (part)

part_list = list(part)
print(part_list)

winners = sample(part, 4)
print(winners)

print("Luckydraw winners")
print("Korean bbq: {}".format(winners[0]))
print("starbucks: {}".format(winners[1:]))
print("Congrats")