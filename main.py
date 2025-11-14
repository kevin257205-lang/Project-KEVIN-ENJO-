print("hello world\n")
if 5>2:
    print("five is greater than 2\n")
if 5>2:
    print("jrhfh")
    
print('hello')

x=4
y=8
print(x+y)
print(x-y)
print(x/y)
print(x*y)
print(x%y)
print(x**y)
print(x//y)
X=23
Y="PIACHE"
print(type(X))
print(type(Y))
z=4.5
print(type(z))

g=' '
print(bool(g))

x='30','40','50'
print(x)
f=['apple','banana','cherry']
x,y,z=f
print(y)
x=y=z=f
print(y)
f=[2,4,7,8,34,50]
print(f)

c="python"
d="is"
e="good"
print(c,d,e)

X="GOOD"

def my_function():
    print("python is "+ X)
my_function()

def my_function():
    global x
    x="good"
my_function()
print("python is "+x)

x=5
print(type(x))
x=5.6
print(type(x))
x=1j
print(type(x))

my_list=["apple","banana"]
print(len(my_list))
#my_list=my_list+[1,3]
#print(len(my_list))
my_list=my_list+["cherry"]
print(my_list[1])
print(my_list[-1])
my_list=my_list+["sjc","bkdcsgkx","vbhsvc"]
print(my_list[-5:-2 ])

my_list[2:5]="abc"
print(my_list)

my_list=[1,2,3,4,5,6]
my_list.insert(2,"apple")
print(my_list)
my_list.append(7)
print(my_list)
my_list.extend([8,9])
print(my_list)
my_list.pop()
print(my_list)
my_list.remove("apple")
print(my_list)
my_list.pop()
print(my_list)
my_list.pop()
print(my_list)


#loops

listz=[1,2,3,4,4,4,5]
for x in listz:
    print(x)

my_list=["apple","banana"]
print(len(my_list))
#my_list=my_list+[1,3]
#print(len(my_list))
my_list=my_list+["cherry"]
print(my_list[1])
print(my_list[-1])
my_list=my_list+["sjc","bkdcsgkx","vbhsvc"]
print(my_list[-5:-2 ])

my_list[2:5]="abc"
print(my_list)

my_list=[1,2,3,4,5,6]
my_list.insert(2,"apple")
print(my_list)
my_list.append(7)
print(my_list)
my_list.extend([8,9])
print(my_list)
my_list.pop()
print(my_list)
my_list.remove("apple")
print(my_list)
my_list.pop()
print(my_list)
my_list.pop()
print(my_list)


#loops

listz=[1,2,3,4,4,4,5]
for x in listz:
    print(x)

#sort
list3=[2,3,5,1,4]
list3.sort()
print(list3)
list3.sort(reverse=True)
print(list3)


#Common string method

l=' HELLO python '

print(l.upper()) #smaller cased gets capitalized
print(l.lower()) #capital letters gets lower cased
print(l.strip()) #removes spaces from start and end
print(l.replace('python','WORLD')) #replace substring with another
print(l.split()) #splits string into a list


#format string

Name="bob"
Age=20
print(f"My name is {Name} and age is {Age}")

x=5
x+=3
x-=4
x*=4
print(x)
x/=7
x%=10
x**=3
x//=5
print(x)


#Comparison operators
print(5==5)
print(5!=5)
print(5>3)
print(5<3)
print(5>=2)
print(5<=6)

#Logical operators

x=5
print(3>x and x<2) # 0 and 1 is 0
print(3>x or x<2) # 0 or 1 is 1
print(not(x>3)) #not 1 is 0


# Identity operators
x=7
y=x
z=9
print(y)
print(x is y)
print(z is not y)

#sets
colors={"red","yellow","blue"}    #creation of set
print(colors)

colors.add("violet") #adding elements
print(colors)

colors.remove("blue")  #removing elements
print(colors)

for I in colors: #iterating through set
    print(I)


#dictionary
student={"name":"dhruv","age":20,"grade":"A"}
print(student)

print(student["name"]) # accessing values
print(student.get("age"))

student["age"]=21    #adding values
student["city"]="Delhi"
print(student)

student.pop("grade")  #removing values
del student["city"]
print(student)

for key,value in student.items():  #iterating values
    print(key,":",value)

#if and else statement

age=20

if age>18:
    print("you are an adult")

elif age==18:
    print("you are a teen")

else:
    print("you are not an adult")

x=int(input())
if x>10:
    print("x is greater than 10")
    if x>20:
        print("x is greater than 20")
    else:
        print("x is not greater than 20")

x=int(input("give a number::"))
if x%2==0:
    print("given number is even")
else:
    print("given number is odd")

#loops
fruits=["apple","banana","cherry"]
for i in fruits:
    print(i)

word='python'
for i in word:
    print(i)
print()
for i in range(1,11):
    print(i)
print()

for i in range(1,10,2):
    print(i)
print()

for i in range(1,4):
    for j in range(1,3):
        print(f"i={i},j={j}")
for i in range(1,6):
    if i==4:
        break
    print(i)


#question 1
for i in range(1,21):
    print(i)

#question 2
for i in range(0,30,2):
    print(i)

#question 3
color=['black','blue','green']
for i in color:
    print(i)

#question 4
for i in range(1,4):
    j=3
    print(f"3x{i}={j}")
    j+=3
      
#function

def greet():
    print("hello python")

def greet(name):
    print(f"hello,{name}")
greet("alice")
greet("bob")

def add(a,b):
    return a+b
result=add(7,4)
print(result)
def sub(a,b):
    return a-b
def product(a,b):
    return a*b
def divide(a,b):
    return a/b
print(sub(5,3))
print(product(5,3))
print(divide(5,3))

def greet(name="student"):
    print(f"hello,{name}!!")
print(greet())

x=10
def my_func():
    y=5
    global x
    print("inside",x,y)
my_func()

#question 1
def greet():
    print("Hello!")

#question 2
def add(a,b):
    print(a+b)

#question 7
x=10
def demo():
    y=4
    print(y,"local")
    print(x,"global")
    print(x+y)

demo()

#class 
class car:
    def __init__(self,brand,color):
        self.brand=brand #attributes
        self.color=color #attributes
    def drive(self): #method
        print(f"{self.color},{self.brand} is driving")

#object
car1=car("BMW","Black")
car2=car("Tesla","White")

car1.drive()
car2.drive()

#Array

import array as ar

#create array of integers

numbers=ar.array('i',[1,2,3,4,5])
print(numbers)

#numpy

from numpy import random

x=random.randint(100)
print(x)

x=random.rand()
print(x)
print(type(x))

s=[54]          #0d array
r=[1,2,3,4,5]   #1d array
t=[[1,2,3],     #2d array
 [3,4,5]]

e=[[[1,2,3]],   #3d array
 [[4,5,6]],
 [[7,8,9]]]

x=random.randint(100,size=(5))
print(x)
x=random.randint(100,size=(3,5))
print(x)
x=random.randint(100,size=(2,3,5))
print(x)
x=random.randint(100,size=(2,2,3,5))
print(x)

x=random.choice([4,5,6],size=(5))
print(x)

#pandas

import pandas as pd
data=[10,20,30,40]
s=pd.Series(data)
print(s)

################################
data={
    "name":['alice',"bob","charlie","david"],
    "age":[24,27,22,32],
    "city":["delhi","mumbai","chennai","kolkata"]
}
df=pd.DataFrame(data)
print(df)


import numpy as np
arr=np.array([1,2,3,4,5])
s=pd.Series(arr)
print(s)


data={"math":90,"science":85,"english":78}
s=pd.Series(data)
print(s)

import pandas as pd
df=pd.read_csv("crocodile_dataset.csv")
print(df.head())

print(df.tail)
