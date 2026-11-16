# def greet(name, caste):
#     print("jai ram ji ki " + name)
#     print(caste)

# greet("modi", "OBC")
# greet("rahul gandhi", "SC")
# greet("yogiji", "GEN")

# def greet(name, caste):
#     print("jai ram ji ki, " + name)
#     print(caste)
#     return"jai ho"

# a = greet("modiji", "OBC")
# print(a)

# Recursion
# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n*factorial(n-1)

# n = int(input("enter the number: "))
# print(f"the fact. of this number is:{factorial(n)}")

# Q.1
# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#         return c

# a=1
# b=9
# c=8
# print(greatest(a,b,c))

# Q.2
# def farenite_to_celsius(f):
#     return 5*(f-32)/9

# f = int(input("enter the temperature:"))
# print (farenite_to_celsius(f))

# Q.4
# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n

# print (sum(4))

# Q.5
# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)

# pattern(3)

# Q.6
# def inches_to_cms(i):
#      return i * 2.54

# i = int(input("enter the inches:"))
# print (inches_to_cms(i))

# Q.7
# part->1
# def rem(l, word):
#     for item in l:
#         l.remove(word)
#         return l

# l = ["rohan", "sohan", "vinay", "an"]
# print(rem(l, "an"))

# part->2
# def rem(l, word):
#     n = []
#     for item in l:
#         if not(item==word):
#             n.append(item.strip(word))
#     return n

# l = ["rohan", "sohan", "vinay", "an"]
# print(rem(l, "an"))

# Q.8
