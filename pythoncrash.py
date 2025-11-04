
# #                        input
# name = input("whats your name? ")
# age = 20
# new_patient =True
# print("Hello , "+name)
# birth_year=input("what is your birth year: ")

# #                   type conversions

# age = 2025-int(birth_year)
# print("you age is "+ str(age) +" year")

# first = input("First: ")
# second = input("Second: ")
# sum=float(first)+float(second)
# print("sum "+str(sum))

# #                     str methods

# course = 'Python foR Beggers'
# print(course.upper())
# print(course.lower())
# print(course.find('foR'))
# print(course.replace('foR', '4'))
# print('foR' in course)

# #                    arithmatic

# print(3/5)
# print(3//2)
# print(3*3)
# print(3**3)
# x=0
# x+=3
# print(x)

# #                   comparison operator

# x = 3<2
# y = 3==2
# z = 3>2
# w = 3!=2

# print(3<5 and 1>1)
# print(3>1 or 3<1)
# print(not 3>1)

# tempreture =float(input("tempreture bol : "))

# #                 if elif

# if tempreture>30: 
#     print("it's a sunny day")
#     print("ghuma")
# elif tempreture<20 and tempreture>0:
#     print("mast mausam hein biru")
# else:
#     print(" kallu beta minus tempreture \n tui ki Canada te?")

# weight= float(input("weight bol kallu: ")) #practise
# con_To= input("kg(K), lb(L) : ")
# if con_To.upper() == 'L':
#     weight_lb= weight*2.20462
#     print("weight in LB: "+ str(weight_lb))
# elif con_To.upper() == 'K':
#     weight_kg= weight*0.453592
#     print("weight in KG: "+str(weight_kg))

# #                  while loop
    
# i =0
# j=15
# while i<20:
#     i+=1
#     j-=1
#     print((j*' ')+(i*'*'))


# names = ["akkas","bakkas","lodu","kaku", "leptin","suga"]
# print(names)
# print(names[0])
# names[5]="kukurV"
# print(names)
# print(names[0:4])

number=[1,5,3,2,6,231,121,2] #list

# print(number)
# number.append(66)
# print(number)
# number.insert(1,12)
# print(number)
# number.remove(6)
# print(number)
# number.sort()
# print(number)
# print(number.count(2))
# print(3 in number)
# #number.clear()
# print(number)
# print(3 in number)
# print(len(number)) 
# mylist= ["akkas","olan","doggy"]
# print(mylist)
# mylisa = mylist[:]
# a= [1,2,3,12,21,22,1,5,4]
# print(a)
# b= [i*i for i in a]
# print(b)
# mylisa.append("akkasdas")
# print(mylist[:])
# print(mylisa)
# print(type(a))

#  #                   forloop
 
# for item in number:
#     print(item)
# i=0
# while(i<len(number)):
#     print(number[i])
#     i+=1

# for number in range(5,55,2):
#     print(number)

# #                        tuple

# existu = (1,2,4,3) 
# print(existu)
# print(existu.count(1))

# my_tuple= ("akkas",223 ,"bakkas",223)
# #my_tuple= tuple(["akkas",223 ,"bakkas"]) same
# print(my_tuple[-1])
# for x in my_tuple:
#     print(x)
# if "luka" in my_tuple:
#     print("yessssss")
# else:
#     print("putki")
# print(len(my_tuple))
# print(my_tuple.count(223))
# print()

# import sys
# asa = ["sda",12,"dsadasdfasdf"]
# asaq = ("sda",12,"dsadasdfasdf")

# print(sys.getsizeof(asa),"bytes")
# print(sys.getsizeof(asaq),"bytes")

#                     dictionary 

# mydict= {
#     "name":"akkas",
#     "roll":1,
#     "sec":"b"
#     }
# print(mydict)
# mydict2= dict(name="olan", roll= 2 , sec="b")
# print(mydict2)
# print(mydict2["name"])
# print(mydict["roll"])
# print(mydict2["sec"])
# mydict["email"]= "randironaMatro@putki.edu"
# print(mydict)
# if "name" in mydict:
#     print(mydict["name"])
# try:
#     print(mydict["email"])
# except:
#     print("error")
# for keys in mydict.keys():
#     print(keys)
# for values in mydict.values():
#     print(values)
# masad = dict(mydict)
# #masad = mydict.copy() same
# masad["ID"]=12231
# print(masad)
# print(mydict)
# mydict3 ={2:4,4:16,5:25}
# print(mydict3)
# print(mydict3[2])
# print(mydict3[4])
# mya =("as","dsa")
# myasd = {mya:12}
# print(myasd)

# test={
#     "name":"akkas",
#     "student":{
#         "roll":1,
#         "id":12
#     }
# }
# print(test["student"]["roll"])
# print(test.get("name"))

# #                       set
# #sets are mutable but elements once added cant be replaced or changed meaning element are immutable

# collection ={1,21,12,"das",12,True} #set
# print(collection)
# #print(type(collection))
# #print(len(collection))
# emptySet = set() #the way to create empty set not by sdas= {}. this is of dict

# emptySet.add("dsad")
# emptySet.add(1)
# emptySet.add(2)
# #print(emptySet)
# #emptySet.remove("dsad")
# emptySet.add((1,2,3,4,324,2,1))
# #print(emptySet)
# #print(emptySet.pop())
# print(emptySet)
# bakkas = collection.intersection(emptySet)
# akkas=emptySet.union(collection)
# print(akkas)
# print(bakkas)
# set.clear(akkas)
# print(akkas)

# word_meaning ={
#       "table":["a piece of furniture","list of fact and figuires"],
#       "cat":"a small animal"
# }
# print(word_meaning)
# classroom= {"python","java","c++","python","javascript","java","python","java","c++","c"}
# print("classroom needed: ",len(classroom))

# subjects={}
# english_mark = int(input("english: "))
# subjects.update({"english":english_mark})
# urdu_mark = int(input("urdu: "))
# subjects.update({"urdu":urdu_mark})
# math_mark = int(input("math: "))
# subjects.update({"math":math_mark})
# print(subjects)
# nine_nine= {9,"9.0" }
# print(nine_nine)


# import time
# i=0
# while i<100:
#     i+=1
#     print(i)
# while i>=0:
#     print(i)
#     i-=1
# n = int(input("enter number : "))
# i=1
# while i<=10:
#     print(n,"x",i,"= ",(n*i))
#     i+=1
# lop =[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# i=0
# while i<len(lop):
#     print(lop[i])
#     i+=1
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)



# i=0
# x= int(input('x: '))
# while i<len(tup):
        
#     if(tup[i]==x):
#         print("found and index is ",i)
#         break
#     else:
#         print("finding..")
#     i+=1

# i=0
# y= int(input('y: '))
# while i<len(tup):
        
#     if(tup[i]==y):
#         i+=1
#         continue

#     print(tup[i])
#     i+=1  

# lust =[1,2,3,1,12]
# for el in lust:
#     print(el)
# lop1 =[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# tup1 =(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
# for el in lop1:
#     print(el)
# idx=0
# for el in tup1:
#     if(el==81):
#         print("found in : ",idx)
#         break
#     idx+=1
# else:
#     print("not found")

# for el in range(1,101):
#     print(el)
# for el in range(100,0,-1):
#     print(el)
# n=5
# for el in range(1,11):
#     print(n," x ",el,"= ",(n*el))

# for x in range(100):
#     pass # created a null loop for future use also can be used in if else
# print("akkum")

# sum=0
# fact=1
# n1=5
# i=0
# while i<=n1:
#     sum+=i
#     i+=1
# print(sum)

# for l in range(1,n1+1):
#      fact*=l
# print(fact)

#  #                       Funtion

# def sum(a,b):
#      return a+b
# def hel():
#     print("Hello ,World")
# #as it has to return value if want to save it in another variable it will show "none"
# #eg. ak= hel() will return "none"
# hel()
# print(sum(1,2))
# def avg_3(a,b,c):
#      return (a+b+c)/3.0
# print(avg_3(10,1,2))
# print("sesh","kore dilo",end=" ")#will not create new line as end= is changed from\n to " ".and If we use sep="anything"it will be changedfrom " " to"anything" 
# def lenlist(list):
#     return len(list)
# asd=["das",121,121,3123,131,3123,13123]
# print(lenlist(asd)) 
# def print_list(list):
#     for el in list:
#         print(el,end=" ")
#     print()
# print_list(asd)
# def factorial(n):
#     fact=1
#     for l in range(1,n+1):
#         fact*=l
#     return fact
# print(factorial(5))
# def usd_to_bdt(usd):
#     return usd*124
# print(usd_to_bdt(50))
# def odd_even():
#     n=float(input("what is the n "))    
#     if (n%2==0):
#         print("even number")
#     else:
#         print("odd number")
# odd_even()
# def show(n):
#     if n==0:
#         print()
#         return
#     print(n,end=" ")
#     show(n-1)
# show(5)
# def fac_rec(n):
#     if(n==1):
#         return 1
#     return n+fac_rec(n-1)


# print(fac_rec(5))
# def plist(list ,x):
#     if(x==len(list)):
#         return 
  
#     print(list[x],end=" ")
    
#     plist(list,x+1)
  

# asxd =[1,"dsdc","asa",12,122,12121]

# plist(asxd,1)

# #                          FIlE IO
# f = open("demo.txt","r")
# data = f.read()
# #print(data)
# f.close()
# f = open("demo.txt","a")
# #f.write("\nnew kicu lekha hoilo motherboard")
# f.close()
# f = open("demo.txt","r")
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)
# f.close()
# test = open("test.txt","w")
# test.close()
# #when I try to write/append in nonexisting file . the file is created automatically
# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)
#     #f.close not needed as with automatically closes the file after closing indentation
# import os
# os.remove("test.txt")
# with open("practise.txt","a") as f:
#     f.write("hi everyone\n")
#     f.write("we are leaning file I/O\n")
#     f.write("using java\n")
#     f.write("I like programming in java\n")

# def file_replacer(a,b,c):
#     with open(a,"r+") as f:
#         data = f.read()
#         new_data=data.replace(b,c)
#         f.write(new_data)
# file_replacer("practise.txt","java","python")
# with open("practise.txt","r") as f:
#     data=f.read()
#     check=data.find("learning")
#     if(check!=-1):
#         print("found and index is",check)
#     else:
#         print("not found")
# def search_line():
#     word ="lea"
#     with open("practise.txt","r") as f:
#         data=True
#         word="programming"
#         lineNo=1
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(lineNo)
#                 return
#             lineNo+=1
#     print("-1")
#     return
        
# # search_line()   
# with open("numbers.txt","r") as f:
#     data=f.read()
    
#     even=0
#     # num=""
#     # for el in range(len(data)):
#     #     if(data[el]==","):
#     #         if(int(num)%2==0):
#     #             even+=1
#     #             print(int(num))
#     #             num=""
#     #     else:
#     #         num+=data[el]
#     #not a good option next one better
#     #/
#     Num=data.split(",")
#     print(Num)
#     for x in Num:
#         if(int(x)%2==0):
#             even+=1
            

        
# print(even) 
# #                      OOP
# class Student:
#     name="akkas"
# s1 = Student()
# print(s1.name)
# class Car:
#     color="khoyari"
#     Brand="RFL"
# c1=Car()
# print(c1.color)
# print(c1.Brand)
# class Student:
    
# default constructor (automatically created not needed to write)
#     def __init__(self):
#         pass
#     Uni_name="NSU"
#     def __init__(self,name,marks):
#         self.name= name
#         self.marks=marks
    
#     @staticmethod   #to make a method static/ we dont need to use self
#     def hello():
#         print("Hello")
#     def avg_num(self):
#         mark=0
#         for x in self.marks:
#             mark+=x
#         print("your average mark is:",mark/3)



# s1= Student("alubdi",[99,72,80])
# s1.avg_num()
# s1.hello()
# import time
# class Bank_account:
#     def __init__(self,bal,acc_num):
#         self.bal=bal
#         self.acc_num=acc_num
#     def balance(self):
#         print("balance is:",self.bal)
#     def debit(self, bal):
#         print("your previous balance:",self.bal)
#         print("debiting:",bal,"....",end= "")
#         self.bal+=bal
#         time.sleep(2)
#         print("...")
#         time.sleep(2)
#         print("your new balace is:",self.bal)
#     def credit(self, bal):
#         print("your previous balance:",self.bal)
#         print("crediting:",bal,"....",end= "")
#         self.bal-=bal
#         time.sleep(2)
#         print("...")
#         time.sleep(2)
#         print("your new balace is:",self.bal)
# b1=Bank_account(15000,"1212421241")
# b1.balance()
# b1.debit(550)
# b1.credit(750)
# #                 encapsulation
# class Student:
#     def __init__(self,name,roll):
#         self.__name=name
#         self.__roll=roll
#     def __hello(self):
#         print("hello")
#     def get_name(self):
#         print(self.__name)
#     def get_roll(self):
#         print(self.__roll)

# s1=Student("akkas",99)
# s1.get_name()
# s1.get_roll()
# s1.hola()
# #             inheritance
# #            multi level inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car starting...")
#     @staticmethod
#     def stop():
#         print("car stopping...")
# class Toyota(Car):
#     def __init__(self,brand):
#         self.brand=brand
# class Fortuner(Toyota):
#     def __init__(self,type):
#         self.type= type
# f1=Fortuner("bengu")
# f1.start()
#  ##            multiple inheritance  (mulple parent)     
# class A:
#     varA="olan"
# class B:
#     varB="mulan"
# class C(A,B): # 2 or multple parents
#     varC="mulaniam"

# c1=C()  
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)
# #                 super methods
# class Car:
#     def __init__(self,name):
#         self.name=name
        
#     @staticmethod
#     def start():
#         print("car starting...")
#     @staticmethod
#     def stop():
#         print("car stopping...")
# class Toyota(Car):
#     def __init__(self,brand,name):
#         self.brand=brand
#         super().__init__(name)
# class Fortuner(Toyota):
#     def __init__(self,type,brand,name):
#         self.type= type
#         super().__init__(brand,name)
# f1=Fortuner("bengu","olianki","dasdf")
# f1.start()
# print(f1.name)

# #                   class methods @classmethod decorator
# class testy:
#     name="anonymous"
#     @classmethod
#     def __init__(cls,name):
#         cls.name=name

# ts=testy("olan batore")
# print(ts.name)
# print(testy.name)
# #                 property decorator(makes the function as a property of class)
# class Subject:
#     def __init__(self,phy,chem ,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#     @property
#     def perchantage(self):
#        return str((self.phy+self.chem+self.math)/3)+"%"
# s1=Subject(99,91,98) 
# s1.math=81
# s1.chem=70
# print(s1.perchantage)

# #              polymorphism(operator overloading)
# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def showValue(self):
#         #print(self.real,"+",self.img,"i")
#         print(f"{self.real} + {self.img}i")#chatgpt

#     def __add__(self,b):#dunder function
#         newreal=self.real+b.real
#         newimg=self.img+b.img
#         return Complex(newreal,newimg)
    
#     def __sub__(self,b): #dunder function
#         newreal=self.real-b.real
#         newimg=self.img-b.img
#         return Complex(newreal,newimg)
#     def __mul__(self,b): #dunder function
#         newreal=self.real*b.real
#         newimg=self.img*b.img
#         return Complex(newreal,newimg)
#     def __truediv__(self,b): #dunder function
#         newreal=float(self.real/b.real)
#         newimg=float(self.img/b.img)
#         return Complex(newreal,newimg)
    
# c1=Complex(1,2)
# c2=Complex(2,4)
# c3=c1+c2
# c4=c1-c2
# c5=c2*c1
# c6=c1/c2
# c3.showValue()
# c4.showValue()
# c5.showValue()
# c6.showValue()
# #                 exercise
# 1
# class Circle:
#     def __init__(self,r):
#         self.r=r

#     def area(self):
#         print("area is:",3.14*self.r**2)
#     def perimeter(self):
#         print("perimeter is:",3.14*2*self.r)

# cir1=Circle(5)

# cir1.area()
# cir1.perimeter()

# 2
# class Employee:
#     def __init__(self,role,department,salary):
#         self.role=role
#         self.department=department
#         self.salary=salary
#     def showDetails(self):
#        return f"role is: {self.role}\nDeparment is: {self.department}\nsalary is: {self.salary}$"


# class Engineer(Employee):
#     def __init__(self,name,age,role,department,salary):
#         self.name=name
#         self.age=age
#         super().__init__(role,department,salary)
#     def showDetails(self):
#         return f"name: {self.name}\nage: {self.age}\n"+super().showDetails()

# en=Engineer("alam",35,"sweeper","cleaning",50)
# print(en.role)
# print(en.showDetails())
# #3

# class Order:
#     def __init__(self,item,price):
#         self.item=item
#         self.price=price
#     def __gt__(self, b):
#         return self.price>b.price
         

# it1=Order("mula",5000)       
# it2=Order("bhutta",500 )       
# if(it1>it2):
#     print(f"{it1.item} is costlier than {it2.item}")
# else:
#    print(f"{it2.item} is costlier than {it1.item}") 