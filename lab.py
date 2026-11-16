# create a list of having the marks of 10 students which are 40,50,65,70,75,80,85,90,95,45 different student in the python program
# marks = [40,50,65,70,75,80,85,90,95,45]

# print("marks of ten students are : ", marks)

# print(type(marks))

# print the marks of 2nd student in the given list

# print("marks of 2nd student is : ", marks[1])

# print the mrarks of 7th student

# print("marks of 2nd student is : ", marks[6])

# print the marks of 7th student by negative indexing

# print("marks of 2nd student is : ", marks[-4])

# print the marks of student no. 2,3,4,5

# print("marks of student no. 2,3,4,5 are : ", marks[2:6])

# print the marks of the student no. 1,3,5,7,9

# print("marks of student no. 1,3,5,7,9 are : ", marks[0::2])

# print all the marks in reverse order using negative indexing

# print("marks of student in reverse order are: ", marks[-10:-1])

# create a list L1 with integer number 11,12,13 and a list L2 with integer number 5,6,7 then perform L1+L2

# L1 = [11, 12, 13]
# L2 = [5, 6, 7]

# print(L1 + L2)

# write programm in python to check wheather the given number is divisible by 5 or 10 or both
# if number is divisible by 5 and 10 both then print the statement accordingly. if number is either divisible by 5 and 10 then print the statement. else print number is niether divisible by 5 nor 10.


# num = int(input("enter the number: "))

# if (num % 5 == 0 and num % 10 == 0):
    # print("Number is divisible by both 5 and 10")
# elif (num % 5 == 0 or num % 10 == 0):
    # print("Number is divisible by either 5 or 10")
# else:
    # print("Number is neither divisible by 5 nor 10")


# write a prog to read 3 numbers from a user and check wheather the first number is greater than 2nd and 3rd both.

# n1 = int(input("enter 1st number:"))
# n2 = int(input("enter 2nd number:"))
# n3 = int(input("enter 3rd number:"))


# if(n1>n2):
    # print("1st number is greater then 2nd ")

# elif(n1>n3):
    # print("1st is greater than 3rd")

# elif(n1>n2 and n1>n3):
    # print("1st is greater than both 2nd and 3rd")

# else:
    # print("1st number is not greater")

# write a prog. in python take the numbers scored by the student in 5 diff. subjects out of 100 and providea result based on the given below cond. 
# marks >= 90% grade A, marks>= 80% and < 90 grade B, marks>= 70% and < 80% grade c, otherwise fail

# m1 = float(input("enter your marks(1):"))
# m2 = float(input("enter your marks(2):"))
# m3 = float(input("enter your marks(3):"))
# m4 = float(input("enter your marks(4):"))
# m5 = float(input("enter your marks(5):"))

# total_percentage = ((100)*(m1 + m2 + m3 + m4 +m5))/500

# if(total_percentage >= 90):
    # print("you scored grade A")

# elif(total_percentage >= 80 and total_percentage < 90):
    # print("you scored grade B")

# elif(total_percentage >= 70 and total_percentage < 80):
    # print("you scored grade C")

# else:
    # print("fail")

# exp 5
# Demonstrate iterative control statements with suitable examples and applications: i) while loop il) for loop.
# total = 0
# i = 1

# while i <= 5:
#     total += i
#     i += 1

# print("Sum:", total)  

# total = 0
# for i in range(-1,):
#     total += i
# print(total)

# phone_book ={"ram":"123","shyam":"456","mohan":"789"}
# print(phone_book)
# print(phone_book["ram"])
# phone_book["rohan"]="110"
# print(phone_book)
# phone_book["ram"]="136"
# print(phone_book)

s1 = {1,2,3,4,5,6,7,8,9,10}