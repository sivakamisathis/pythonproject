#Sample program for map:
# def sample(a):
#     return len(a)

# x=map(sample,("apple","banana","cherry"))
# print("The length of the word is:",list(x))


# def add(a,b):
#     return a+b

# x=map(add, [3,4,5], [6,7,8])
# print("The addition of list is:",list(x))

# #Sample program for Filter
# age=[10, 17, 5, 23, 15, 12, 20]

# def sample(x):
#     if x<18:
#         return False
#     else:
#         return True  
    
# adults=filter(sample, age)

# for x in adults:
#     print("The value of above 18 is:",x)

# #Sample program for Reduce
# import functools
# numbers=[1,2,3,4]
# product=functools.reduce(lambda x,y:x*y,numbers)
# print("The product of list elements:",product)


# from functools import reduce
# list=[4,2,6,10,9]
# num=reduce(lambda x, y:x+y,list)
# print("The addition of number is:",num)

# print("The maximum element of list is:",end="")
# print(reduce(lambda x, y:x if x>y else y, list ))

# from functools import reduce
# list=[2,4,6,8]
# num=reduce(lambda x,y:x*y,list)
# print("The Multiplication of number is:",num)


#Encapsulation:
# class book:
#     #public
#     def open_lib(self):
#         print("door opened")
#         print("The book is available")
#         self._author()

#     #protected
#     def _author(self):
#         print("Only english book")
#         self.__poet()

#     #private
#     def __poet(self):
#         print("The poem is very interesting")
#         print("The poet is also explained very nice")

# b=book()
# b.open_lib()



print(dir(int))