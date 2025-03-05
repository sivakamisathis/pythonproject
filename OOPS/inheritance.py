#single inheritance:
# class dad:
#     def phone(self):
#         print("Dad's phone")
# class son(dad):
#     def laptop(self):
#         print("Son's laptop")

# s1=son()
# s1.phone()
# s1.laptop()

#Multiple Inheritance;
# class dad:
#     def phone(self):
#         print("Dad's phone")
# class mom:
#     def sweet(self):
#         print("Moms sweet")
# class son(dad,mom):
#     def laptop(dad):
#         print("Son's laptop")

# s1=son()
# s1.phone()
# s1.sweet()
# s1.laptop()

#Multilevel Inheritance:
# class grandpa():
#     def phone(self): 
#         print("grandpa phone")
# class dad(grandpa):
#     def money(self):
#         print("Dads Money")
# class son(dad):
#     def laptop(self):
#         print("Sons laptop")

# s1=son()
# s1.laptop()
# s1.money()

# s2=dad()
# s2.phone()

#Hierarchal Inheritance
# class dad():
#     def money(self):
#         print("Dad Money")
# class son1(dad):
#     def phone(self):
#         print("Need phone")
# class son2(dad):
#     def book(self):
#         print("Need book")
# class son3(dad):
#     def bag(self):
#         print("Need bag")

# s2=son2()
# s2.money()
# s2.book()

#Hybrid Inheritance
# class student:
#     def get_details(self):
#         self.name=input("Enter the Name:")
#         self.age=int(input("Enter the age:"))
# class addition(student):
#     def add(self):
#         self.get_details()
#         self.mark1=int(input("Enter the mark1:"))
#         self.mark2=int(input("Enter the mark2:"))
#         c=self.mark1+self.mark2
#         print("Addition of marks:",c)

# class subtraction(student):
#     def sub(self):
#         self.get_details()
#         self.mark1=int(input("Enter the mark1:"))
#         self.mark2=int(input("Enter the mark2:"))
#         c=self.mark1-self.mark2
#         print("Subtraction of marks:",c)

# class operations(addition,subtraction):
#     def oper(self):
#         self.add()
#         self.sub()

# s1=operations()
# s1.oper()

#sample program for single inheritance:
# class person:
#     def display(self):
#         self.name=input("Enter the name:")
#         self.age=int(input("Enter the age:"))
        
# class student(person):
#     def show_details(self):
#         #self.display()
#         mark=int(input("Enter the marks:"))
#         print("The student details are:")
#         print("The name is:",self.name)
#         print("The age is:",self.age)
#         print("The mark is:",mark)

# s1=student()
# s1.display()
# s1.show_details()

#sample program for Multiple inheritance:
# class Mathteacher():
#     def teach(self):
#         print("The Math teaching is good")

# class scienceteacher():
#     def teach1(self):
#         print("The Science teaching is excellent")

# class school_teacher(Mathteacher,scienceteacher):
#     def teach2(self):
#         print("Both are school teacher")

# s1=school_teacher()
# s1.teach()
# s1.teach1()
# s1.teach2()

#Multilevel inheritance:
# class Animal():
#     def sound(self):
#         print("The animal sound is nice")

# class Mammal(Animal):
#     def walk(self):
#         print("The mammal is walk")

# class Dog(Mammal):
#     def walk1(self):
#         print("The dog is barking")

# d=Dog()
# d.walk1()
# d.walk()

# a=Animal()
# a.sound()


#Hierarchal inheritance:
# class shape():
#     def area(self):
#         print("The shapes are circle or Rectangle:")

# class Rectangle(shape):
#     def area1(self):
#         print("The shape is rectangle")
    
# class circle(shape):
#     def area2(self):
#         print("The shape is circle")

# s=circle()
# s.area()
# s.area2()


#Hybrid Method:
class Employee():
    def display(self):
        self.name=input("Enter the name:")
        self.salary=int(input("Enter the salary:"))

class Manager(Employee):
    def rules(self):
        self.display()
        print("Managing the works")

class Engineer(Employee):
    def build(self):
        self.display()
        print("Construct the building")

class team(Manager,Engineer):
    def result(self):
        self.rules()
        self.build()

s=team()
s.result()

