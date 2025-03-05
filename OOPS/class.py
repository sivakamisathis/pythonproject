# class student:
#     def __init__(self):
#         self.name=""
#         self.age=0

#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)

# std=student()
# std.name="Siva"
# std.age=20

# std.display()


# class student:
#     school_name='skv school'

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def show(self):
#         print(self.name,self.age,student.school_name)

#     @classmethod
#     def change_school(cls,name):
#         cls.school_name=name

#     @staticmethod
#     def find_notes(subject_name):
#         return ["chapter1","chapter2","chapter3"]

# std1=student("siva",25)
# std1.show()

# student.change_school('skv school')

# std1.change_school('RMS school')
# std1.show()

# student.find_notes("Maths")


# std1.find_notes("Maths")


# class fruit:
#     def __init__(self,color):
#         self.color=color

#     def display(self):
#         print("The color is:",fs.color)

# fs=fruit("red")
# fs.display()

# class teacher:
#     def __init__(self,name,regno):
#         self.name=name
#         self.regno=regno

#     def display(self):
#         print("The name is:",self.name)
#         print("The Register no is:",self.regno)

# t1=teacher("mala",30)
# t2=teacher("Kavitha",35)

# t1.display()
# print("\n")
# t2.display()

class calculator:
    def __init__(self,num1,num2):
        self.num1="" 
        self.num2=num2
    def add(self):
        print("The Addition:",self.num1+self.num2)
       