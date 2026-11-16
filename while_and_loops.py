# i = 1

# while(i<51):
    # print(i)

    # i += 1

# l = ["jai", "vijay", 5, "jaiho", False]

# i = 0

# while(i<len(l)):
    # print(l[i])
    # i += 1

# l = [5,6,7,8,3,2]

# for i in l:
#     print(i)

# l = [3,5,7,8,4,1]

# for item in l:
#     print(item)

# else:
#     print("done")

# for i in range(100):
#     if(i==34):
#         continue
#     print(i)

# Q.1
# n = int(input("enter a number:"))

# for i in range(1, 11):
#     print(f"{n} X {i} = {n*i}")

# Q.2
# l = ["harry", "soham", "sachin", "rahul"]

# for name in l:
#     if(name.startswith("s")):
#         print(f"hello {name}")

#Q.3
# n = int(input("enter a number:"))

# i = 1
# while(i<11):
#     print(f"{n} X {i} = {n*i}")
#     i += 1

# Q.4
# n = int(input("enter a number:"))

# for i in range(2,n):
#     if(n%i==0):
#         print("not a prime number")
#         break
#     else:
#         print("it is a prime number")
#         break

# Q.5
# n = int(input("enter the number:"))
# i = 1
# sum = 0
# while(i<=n):
#     sum += i
#     i += 1
# print(sum)

# Q.6
# n = int(input("enter the number:"))
# product = 1
# for i in range(1,n+1):
#     product = product * i

# print(f"the factorial of {n} is {product}")

# Q.7
# n = int(input("enter the number:"))
# for i in range(1, n+1):
#     print(" "*(n - i), end = "")
#     print("*"* (2*i - 1),end = "")
#     print("")

# Q.8
# n = int(input("enter the number:"))
# for i in range(1, n+1):
#     print("*"*i,end = "")
#     print("")

# Q.9
# n = int(input("enter the number:"))
# for i in range(1, n+1):
#     if (i==1 or i==n):
#       print("*"*n, end = "")

#     else:
#         print("*", end= "") 
#         print(" "*(n-2), end="")
#         print("*", end= "") 
#     print("")

# Q.10

# n = int(input("enter a number:"))

# for i in range(1, 11):
#     print(f"{n} X {11-i} = {n*(11-i)}")