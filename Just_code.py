# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

'''
class Vegetable:
    def curliflower(self):
        print("This is curliflower method called", self)

    def patatoes(self):
        print("This is patatoes class called", self)

class House_needs(Vegetable):
    def Car(self):
        print("This is car method called from House_needs", self)

House_needs.patatoes(self)
'''
import datetime
import json
import random

import matplotlib.pyplot as plt
from numpy.distutils.system_info import xft_info

"""class Students:
    def marks(self, name, cnic_no, score):
        print(f'{self} Mr. {name} CNIC No : {cnic_no} has got {score}')


Students.marks('fayaz','42501-9716999-1',"80.81%",'693')
"""

"""class Parents:
    def __init__(self, a, b):
        self.name = a
        self.age = b

obj = Parents(14,12)
print(obj.name)
print(obj.age)

print('Name is : ' , 'age is : ',obj.age )"""

# =============================================================
# Python3 program to
# demonstrate instantiating
# a class


"""class Dog:
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)


# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()
"""

"""class Animals:
    attr1 = "Breed"
    attr2 = "Type"
    attr = "size"
    attr = "age"

    def eat(self, fayaz):
        print("this is attribute in method :" , fayaz)
        print("This is method", self)

newObj = Animals()

# now object can access the elements of a class
# lets access
print(newObj.attr1)
print(newObj.attr2)

# let's call the method
newObj.eat("fayaz malik")"""

# A Sample class with init method
"""class Person:

    # init method or constructor 
    def __init__(self, name):
        self.name = name

    # Sample Method 
    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Nikhil')
p.say_hi()"""


# Python3 program to show that the variables with a value
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.

# Class for Dog
class Dog:
    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed, color):
        # Instance Variable
        self.breed = breed
        self.color = color

    # Objects of Dog class


"""Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)"""

"""
class A:
    def b():
        print("this is method with name b in class A")

A.b()"""
"""
class Test:
    # Constructor - non parameterized
    def __init__(self):
        print("This is non parametrized constructor")

    def show(self, name):
        print("Hello", name)

# creating object of the class
t = Test()         # Output:This is non parametrized constructor

# calling the instance method
t.show("Arthur")   # Output Hello Arthur"""

"""
class Test:
    def __init__(self):
        print('This is is learning of classes and object')

    def person(self, name):
        print("This is", name)

obj1 = Test()

obj1.person('Fayaz Ahmed')"""

# Example 2: Constructor with parameters
"""
class Fruit:
    # parameterized constructor
    def __init__(self, name, color):
        print("This is parametrized constructor")
        self.name = name
        self.color = color

    def show(self):
        print("Fruit is", self.name, "and Color is", self.color)

# creating object of the class
# this will invoke parameterized constructor
obj = Fruit("Apple", "red")   # Output This is parametrized constructor

# calling the instance method using the object
obj.show()                    # Output Fruit is Apple and Color is red"""

"""class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')

# create a new object of Person class
harry = Person()

print(Person.greet)  # Output: <function Person.greet>

print(harry.greet)  # Output: <bound method Person.greet of <__main__.Person object>>

# Calling object's greet() method
harry.greet()  # Output: Hello"""

# Example 2:
# ========================================================================================
"""class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')

# Create a new ComplexNumber object
num1 = ComplexNumber(2, 3)

# Call get_data() method

num1.get_data()   # Output: 2+3j

# Create another ComplexNumber object and create a new attribute 'attr'
num2 = ComplexNumber(5)
num2.attr = 10

print((num2.real, num2.imag, num2.attr))  # Output: (5, 0, 10)

# but c1 object doesn't have attribute 'attr'
print(num1.attr)  # AttributeError: 'ComplexNumber' object has no attribute 'attr'"""

# Example 3:

"""class Student:

# Construct
    def __init__(self, name):
        self.name = name   # Parameter

# Method
    def show(self):
        print('Student name is :', self.name)

# Creating Object
stdName = Student('Fayaz')

# Calling Function
stdName.show()"""
"""
class Student:
    def __init__(self, name , roll_no):
        self.n = name
        self.roll = roll_no

    def call_it(self):
        print('we have pass two parameteers', self.n , 'number is ' , self.roll)

obj1 = Student('Fayaz', 1243)

obj1.call_it()

"""

# Example 3:

# Example 4: Creating Class and Object in Python

"""class MasterStudentClass:
    # class attribute
    species = "students"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
jane = MasterStudentClass("Jane", 18)
bella = MasterStudentClass("Bella", 19)
candy = MasterStudentClass("Candy", 17)
lucia = MasterStudentClass("Lucia", 18)
ran = MasterStudentClass("Ran", 20)

# access the class attributes
print("Jane is a {}".format(jane.__class__.species))         # Jane is a students
print("Bella is also a {}".format(bella.__class__.species))  # Bella is also a students

print('Jane is a {}'.format(jane.__class__.species) )
print('we have printed' .format(lucia.name))
"""

# convert_dictionary_to_python_object

"""class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
# print (counter.__secretCount)  # This wont work
print (counter._JustCounter__secretCount)
"""

# Example 1:

"""class Student:
    'Common base class for all students'
    student_count=0

    def __init__(self, name, id):
        self.name = name
        self.id = id
        Student.student_count += 1

    def printStudentData(self):
        print ("Name : ", self.name, ", Id : ", self.id)

std1=Student("Milan",101)
std2=Student("Vijay",102)
std3=Student("Chirag",103)

print("Total Student : ",Student.student_count)
print ("Student.__doc__:", Student.__doc__)
print ("StudentStudent.__name__:", Student.__name__)
print ("Student.__module__:", Student.__module__)
print ("Student.__bases__:", Student.__bases__)
print ("Student.__dict__:", Student.__dict__)"""

"""# Example 1:

class Employee:
    def __init__(self, id, name):
        # instance variable
        self.id = id
        self.name = name

    # instance method
    def info(self):
        print("Employee ID is ", self.id, "and name is", self.name)

    # instance method
    def department(self):
        print("Employee of IT department")


emp = Employee(19116, "Amy", )
emp.info()  # Output Employee ID is 19116 and name is Amy

emp.department()  # Output Employee of IT department"""

"""class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def creatingStudents(self):
        print('Student Name is :' , self.name , 'and roll number is :' , self.roll_no)

student1 = Student('Qadir',55)
student2 = Student('fayaz',62)
student3 = Student('Rashid',66)
student4 = Student('mansoor',88)

student4.creatingStudents()
print(student3.creatingStudents())
print(student3.name)
student4.creatingStudents()"""

"""class Animal:
    def __init__(self, type , breed):
        self.type = type
        self.breed = breed

    def createAnimalObject(self):
        print(f'This is a :' , self.type , 'is from' , self.breed)

ani1 = Animal('Dog','American')
ani2 = Animal('Cat', 'Australian')
ani3 = Animal('monkey','inida')

ani1.createAnimalObject()
ani2.createAnimalObject()
print(Animal)
print(ani3.breed)"""

import numpy as np

"""class A:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def show(self):
        print(f'Name is ' , self.name, 'age is ' , self.age)

class B(A):
    def __init__(self, work, home):
        self.work = work
        self.home = home

    def show2(self):
        print(f'name is ' , self.name, 'age is', self.age, 'work at', self.work, 'Address is' , self.home)

obj1 = A('fayaz', '32')
obj2 = B('Software House', 'Karai')

# print with objects
print(obj1.age, obj1.name)
print(obj2.work, obj2.home)
print(obj1.name, obj2.home)
print(obj1.name,obj1.age,obj2.work,obj2.home)

# print with methods
obj1.show()
"""

"""class Animal:
    def eat(self):
        print('I can eat')

class Dog(Animal):
    def bark(self):
        print('I can bark')

class Lion(Animal):
    def Roar(self):
        print('I can roar')

# Object from lion and printed Animal main class method eat
objLion = Lion()
objLion.eat()

# Object from dogClass and printed Animal main class methhod eat
objectDog = Dog()
objectDog.eat()"""

"""class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("This is polygon of two sides")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

class Triangle(Polygon):
    def display_info1(self):
        print('A triangle has 3 sides')

class Quadrilateral(Polygon):
    def display_info2(self):
        print('Quadrilateral has four sides')

t1 = Triangle([12,15,35])
perimeter = t1.get_perimeter()
print('The perimeter is :' , perimeter)"""

"""class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("This is polygon of two sides")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

class Triangle(Polygon):
    def display_info(self):
        print('A triangle has 3 sides')
        # Here method will be override by derived class so
        Polygon.display_info(self)

class Quadrilateral(Polygon):
    def display_info(self):
        print('Quadrilateral has four sides')
        # Here method will be override by derived class so
        super().display_info()  # More Elegagnt method

t1 = Triangle([12,15,35])
perimeter = t1.get_perimeter()
print('The perimeter is :' , perimeter)

q1 = Quadrilateral([12,43,23,14])
perimeter = q1.get_perimeter()
print('This perimeter of quadrilater is :', perimeter)

# LETS TRY METHOD OVERRIDING
t1.display_info()
# LETS TRY METHOD OVERRIDING
q1.display_info()"""

"""class Employees:
    def __init__(self, salary):
        self.salary = salary

    def show_salary(self):
        print('This is for employee :' , self.salary)

    def calculate_salary(self):
        calculate_salary = sum(self.salary)
        return calculate_salary

class Admin(Employees):
    def show_salary(self):
        print('This is admin class salary' , self.calculate_salary())


class Maintaineance(Employees):
    def show_salary(self):
        print('This is Maintaineance salary' , self.calculate_salary())

# Lets create Admin Object
admin_emp = Admin([20000,50000, 2000, 10000])
print(admin_emp.calculate_salary())
# Calling Admin method
admin_emp.show_salary()

maint_emp = Maintaineance([40000, 5000, 3000, 1000])
# print the salary of Maintaineance
print(maint_emp.calculate_salary())
# Let's print the method for this class
maint_emp.show_salary()"""

# ======================================================================================
"""class Employees:
    def __init__(self, salary):
        self.salary = salary

    def show_salary(self):
        print('Employee Salary :' , self.salary)

    def calculate_salary(self):
        calculate_salary = sum(self.salary)
        return calculate_salary

class Admin(Employees):
    def show_salary(self):
        print('This is admin class salary' , self.calculate_salary())
        #Employees.show_salary(self)
        super(Admin, self).show_salary() # This will print the main class salary
        super().show_salary() # This will print the main class salary


class Maintaineance(Employees):
    def show_salary(self):
        print('This is Maintaineance salary' , self.calculate_salary())
        super(Maintaineance, self).show_salary()
        super().show_salary()


# Lets create Admin Object
admin_emp = Admin([20000,50000, 2000, 10000])
maint_emp = Maintaineance([40000, 5000, 3000, 1000])

admin_emp.show_salary()
maint_emp.show_salary()"""

""""#===========================================================================================================
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
x = lambda a: a + 10
print((x(5)))
"""

"""def function_learning_lamda(any_no):
    return lambda second_no : second_no * any_no

any_var = function_learning_lamda(4)

print(any_var(5))
"""

"""def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
"""

"""def myfunc(n):
    return lambda  a: a * n
mytripler = myfunc(3)
print(mytripler(11))"""
"""def myfunc(n):
    return lambda a : a * n

mydouler = myfunc(2)
mytripler = myfunc(3)
myfifler = myfunc(5)

print(mydouler(11))
print(mytripler(11))
print(myfifler(11))"""

"""for i in range(10):
    print(i)
    if i == 5:
        break"""

'''iterator vs iterale'''

"""mytyple = ('apple', 'banana', 'mango', 'cherry')

myit = iter(mytyple)

print(myit)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
"""

"""mystr = 'banana'
myit = iter((mystr))

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))"""

"""mytuple = ('apple','banana', 'mango', 'orange')

for x in mytuple:
    print(x)"""

"""class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myClass = MyNumbers()
myiter = iter(myClass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))"""

"""class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myClass = MyNumbers()
myiter = iter(myClass)

for x in myiter:
    print(x)"""

"""def myfunc():
    x = 10

    def function2():
        print(x)
    function2()

myfunc()"""

"""def animal():
    type = 'Dog'

    def dog():
        print('A type of dog')
    dog()

animal()"""

"""x = 300
def myfunc():
    print(x)

myfunc()

print(x)"""

"""x = 300
def myfunc():
    x = 200
    print(x)
myfunc()

print(x)"""

"""def myfunc():
    global x
    x = 300

myfunc()

print(x)"""

"""x = 300

def myfunc():
    global x
    x = 200
myfunc()

print(x)"""

"""def parent():
    var1 = 500
    print()
    print('Parent function')
    print('Printing from Parent ' , x)


    def child():
        global var2
        var2 = 700
        print('Making it global from child' , var2)
        print('Child Function')
        print(var1)
        print('Printing from Child :' , x)
    child()

parent()"""

# ===================================================================================================
# Dates Understanding

"""import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.month)
print(x.day)"""

"""import datetime as dt

x =dt.datetime.now()
print(x)
y = dt.timezone.utc
print(y)"""

"""import datetime
x = datetime.datetime.now()
print(x.strftime("%A"))"""

"""import datetime
x = datetime.datetime(2020,5,17)
print(x)
"""

"""import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))"""
"""
import datetime

x = datetime.datetime.now()

print(x.strftime("%V"))"""

# =========================================================================================

"""x = (5, 6 ,2,67,34,75,34,45,55,3,54,65,6,4,3,4,76,7)
print(x)
print(min(x))
print(max(x))

y = abs(-7.76)
print(y)

z = pow(25, 2)
print(z)

x = pow(4,3)
print(x)
"""
"""
import math

x = math.log(5, 10)
print(x)

x =math.sqrt(36)
print(x)

x = math.ceil(1.5)
y = math.floor(1.5)

print(x)
print(y)"""

"""import math

x = math.pi

print(x)"""

# =====================================================================================
# JavaScript Oject notation
# Json is text format for storing and  transporting data
# Json is "self- describing and easy to understand

"""import json
# some JSON

x = '{"name": "John" , "age" : 30, "city" : "karachi"}'

#parse this x
y = json.loads(x)
print(y)
print(y["age"])
print(y['name'])
"""

"""
import json

# Create python Object dictionaty

x = {
    "name" : "John",
    "age" : 30,
    "city" : "New York"
}

"""

"""
# convert it into jason method
y =json.dumps(x)
# Result in json string
print(y)
"""

# you can work on
'''Dic , list, tuple, string, int , float, true, false, none'''

"""
import json

#print((json.dumps({'name':'fayaz' , 'age': 30}))
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps((["apple" , "banana"])))
print(json.dumps(("apple", "banana")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps((True)))
print(json.dumps(False))
print(json.dumps(None))


# Covert a python object containning all the legal data types

x = {
    "name" : "John",
    "age" : 30,
    "married" : True,
    "divorced" : False,
    "Childeren" : ("Anny", " Billy"),
    "pets" : None,
    "cars" : [
        {"model" : "BMW 230", "mpg" : 27.5} ,
        {"model" : "Ford Edge", "mps" : 24.1}
    ]
}

(json.dumps(x))
print("###########################")
print(json.dumps(x, indent=4))

print("###########################")
print(json.dumps(x, indent=4, separators=(". " , "= ")))

#Sort it alphabetically so chidrens names will be above
print("###########################")
print(json.dumps(x, indent=4, sort_keys=True))
"""

# =================================================================
# Regular Exprerssion
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.


"""import re

txt  = "The rain in spain"
x = re.search("^The.*spain$", txt)  #  ^ keyboard six key has signature carret option

print(x)"""

"""import re
txt = "I am a software Engineer"

x = re.findall("e"
               "", txt)

print(x)
"""

"""import re

txt = "Pakistan is a country with less jobs"""

"""x = re.search("\s" , txt)
print(x)

print("The first white-space character is located in position: " , x.start())

"""
"""x = re.search("Portugal", txt)
print(x)"""

"""x = re.split("\s", txt)
print(x)
"""
"""x = re.split("\s", txt  ,3)
print(x)
"""

"""x = re.sub("\s", "9", txt)
print(x)
"""

"""x = re.sub("\s", "9", txt, 3)
print(x)
"""
# match object

"""x = re.search("le" ,txt)
print(x)"""

"""x = re.search(r"\S\w+" , txt)
print(x)
print(x.span())"""

"""import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())"""

# Try Excecpt
"""try:
    print(x)
except:
    print("An exception accured")"""

"""try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("some thing else went wrong")

"""

"""try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")
"""
"""try:
    print(x)
except:
    print("somethhingg went wrong")
finally:
    print("the try excep is finished")
    """
"""try:
    f = open("demofile.txt")
    try:
        f.write("fayaz malik")
    except:
        print("Something went wrong when writin to the file")
    finally:
        f.close()

except:
    print("Some thing went wrong when opening the file")

    """

"""x = -1
if x <0:
    raise Exception("sorry , no number below zero")
"""

x = "Hello"

"""if not type(x) is int:
    raise TypeError('Only intergers please')"""

'''This is for theme cheking'''

"""def print_method():
    print("This will print our program")

print_method()

class Parent:
    #This is class defined for checking of theme
    def __init__(self, name, age):
        self.name = name
        self.age = age """

# ===================================================================================================

"""class Mobile:
    def __init__(self, company  , model):
        self.company_name = company
        self.Model_no = model

    def company(self):
        print(f'The company name is : {self.company_name} and model is : {self.Model_no}')

class Personal_detail(Mobile):
    def __init__(self, owner , city):
        self.owner = owner
        self.city  = city

    def personal_info(self):
        print(f'The owner ID is : {self.owner} and live at : {self.city}')

samsung = Mobile("Samsung", 343553)
#####################################
print(samsung.company_name)
print(samsung.Model_no)
samsung.company()
# constructor for ChildClass
owner = Personal_detail('Spencer', 'washington DC')
###############################################
print(owner.city)
print(owner.owner)
owner.personal_info()"""
##############################################
'''DO Mix and Match increase the understanding'''

"""try:
    print(x)

except:
    print('X is  not defined')
"""

"""
username = input("Enter user name: ")
print("User name is : " + usename)
"""

"""price = 49
txt = "The price is {} dollars"
print(txt.format(price))
"""

"""quantity  = 3
itemno = 363
price =49

myorder = "I want {} pieces of item number {} for {:.3f} dollars."

print(myorder.format(quantity, itemno, price))"""

"""quantity = 3
itemno =235
price  = 55

myorder = "I want {0} pieces of the item number {1} for {2:.2f} dollars."
print(myorder.format(quantity,itemno,price))"""

"""name = input("Enter you name : " )
age = input("Enter you age : ")
school = input("Enter you school : ")
mydetails = "You have booked {0} his/her age is {1} and study at {2}"

print(mydetails.format(name,age,school))"""

"""name = input("Enter you name : " )
age = input("Enter you age : ")
school = input("Enter you school : ")
mydetails = "You have booked {0} his/her age is {1} and study at {2}." \
            "{0} is young and just  {1} age"

print(mydetails.format(name,age,school))"""

"""carname = input("Enter the car name :")
model   = input("Model is : ")
charges = input("Enter Charges :")
carorder = "You have booked {car} trip with {shape} Model, your trip_fees is :{fees}"
print(carorder.format(car = carname, shape = model, fees = charges))"""

# f = open(r"C:\Users\92334\Desktop\pythonfile.txt", "w")
# print(f.read())
# print(f.read(30))
"""print("##################################")
print(f.readline())
print(f.readline())"""

"""for x in f:
    print(x)"""

"""print(f.readline())
f.close"""

###############################################
# f = open(r"C:\Users\92334\Desktop\pythonfile.txt", "w")
# f.write("Now the file has more content!")
# f.close()

# open and read the file after the appending:
# f = open(r"C:\Users\92334\Desktop\pythonfile.txt", "r")
# print(f.read())

#########################################################
# f = open(r"C:\Users\92334\Desktop\created.txt", "w" )
# f.write("Now the file has content")
# f.close()

# f = open(r"C:\Users\92334\Desktop\created.txt", "r")
# print(f.read())
#######################################################
# Delted files
# import os
# os.remove(r"C:\Users\92334\Desktop\created.txt")

# import os
# if os.path.exists(r"C:\Users\92334\Desktop\created.txt"):
#    os.remove(r"C:\Users\92334\Desktop\created.txt")
# else:
#    print("file is already deleted")

############################################################################
"""Matolotlib Library"""

"""import matplotlib.pyplot as plt
import numpy as np

xpoint = np.array([0,10])
ypoint = np.array([0,25])

plt.plot(xpoint,ypoint)
plt.show()"""
#################################
"""import matplotlib.pyplot as plt
import numpy as np

xpoint = np.array([0,10])
ypoint = np.array([0,25])

plt.plot(xpoint,ypoint, 'x')
plt.show()"""
###################################################

"""import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])

plt.plot(xpoints,ypoints)
plt.show()
print("Code has no error")"""
###################################################
"""import matplotlib.pyplot as plt
import numpy as np

ypoint = np.array([2,21,21,14,6,19])

plt.plot(ypoint ,  marker = '+')
plt.show()"""

###################################################
"""import matplotlib.pyplot as plt
import numpy as np

ypoint = np.array([2,21,21,14,6,19])

plt.plot(ypoint ,  'x:b')
plt.show()"""
#############################################
"""import matplotlib.pyplot as plt
import numpy as np

ypoint = np.array([2,21,21,14,6,19])

plt.plot(ypoint , marker = 'o' , ms = 20, mec ='r', mfc = 'y' )
plt.show()"""

"""import matplotlib.pyplot as plt
import numpy as np

ypoint = np.array([2,21,21,14,6,19])

# plt.plot(ypoint, linestyle = 'dotted' , marker = 'o' , ms = 20, mec ='r', mfc = 'r' )
plt.plot(ypoint, linestyle = 'dashed' , marker = 'x' , ms =15, mec ='b' , mfc ="r" )
plt.show()"""

# String formatting

# price = 49
# txt = "the price is {} dollars"
# print(txt.format(price))
#
#
# prie = 49
# txt = "the price is {:.2f} dollars"
# print(txt.format(prie))
#
# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {} pieces of item number {} for {:.2f} dollars"
# print(myorder.format(quantity,itemno,prie))

# Indexed Number
# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {0} peices of item number {1} for {2:.2f} dollars."
# print(myorder.format(quantity, itemno, price))
#
# age = 36
# name = "fayaz"
# txt = "his name is {1} . {1} is {0} years old"
# print(txt.format(age, name))


# Name index
# myOrder = "I have a {carname}, it is {model}"
# print(myOrder.format(carname = "Cultus", model = "2010"))

# mylist = ["a","b","c","c"]
# mylist = list(dict.fromkeys(mylist))
# print(mylist)

# mylist = ["a","b","c","d","d","e","e","f"]
# mylist = list(dict.fromkeys(mylist))
# print(mylist)

# def my_function(x):
#     return list(dict.fromkeys(x))
#
# mylist = my_function(["a","b","c","d","d","e","e","f"])
#
# print(mylist)

# def my_function(x):
#     return list(dict.fromkeys(x))
#
# my_list = my_function(["a","b","c","d","d","e","e","f"])
# print(my_list)

# How to reverse a string in python

# txt = "My name is fayaz ahmed malik"[::-1]
# print(txt)

# txt = "hello world"[::-1]
# print(txt)

# def my_function(x):
#     return x[::-1]
#
# mytxt = my_function("I am a boy")
# print(mytxt)

# def my_function(x):
#   return x[::-1]
#
# mytxt = my_function("I wonder how this text looks like backwards")
#
# print(mytxt )

# x = 1
# y = 0.1
# z = "fayaz"
# l = 1j
#
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(1j))

# import re
# txt = "the rain in spain"
# x = re.split("\s", txt)
# for i in x:
#     print(i)

# ***********************************************************************#
# dataset = [1,2,3,4,5,6,7,8] # 8 values dataset
#
# # print(list(dataset))
# dataset.append(3.5)
# print(dataset)

# #*
# dataset = [1,2,3,4,5,6,7,8] # 8 values dataset
#
# # print(list(dataset))
# dataset.append(3.5)
# print(dataset)
#
# #*
# dataset = [1,2,3,4,5,6,7,8] # 8 values dataset
#
# #**
# # print(list(dataset))
# dataset.insert(2, 3.5)
# print(dataset)

# import numpy as np
# import matplotlib.pyplot as plt
#
# np.random.seed(2)
# x = np.random.normal(3, 1, 100)
# y = np.random.normal(150, 40, 100)/x
#
# plt.scatter(x,y)
# plt.show()

############################
#
# import numpy as np
# np.random.seed(2)
# x = np.random.randint(1,7, size = 2)
# print(x)

###############################
# Created array and inserted values with for loop
# a = []
# y = 5
# for x in range(y):
#     a.append(random.randint(1,5))
# print(a)

#########################################
# This will take input and store as array.f
# array = []
# x = 5
# for i in range(x):
#     array.append(input("Enter your name, age, passing year, status :"))
#
# print(array)
# # store and only index from 2 and later.
# print(array[2:])

# track from index and store in variables
# a = array[0]
# b = array[1]
# c = array[2]
# d = array[3]
# f = array[4]
# print(f'you age is {a} your passing year is {c}')



