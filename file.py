# Q.1
# f = open("poem.text")
# content = f.read()
# if("twinkle" in content):
#     print("twinkle is present")

# else:
#     print("twinkle is not present")
# f.close()

# Q.2
# import random

# def game():
#     print("you are playing a game....")
#     score = random.randint(1, 62)
#     with open("hiscore.text") as f:
#         hiscore = f.read()
#         if (hiscore != ""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0

#     print(f"your score {score}")
#     if(score>hiscore):
#         with open ("hiscore.text", "w") as f:
#             f.write(str(score))

#     return score

# game()

# Q.3
# def genratetable(n):
#     table = ""
#     for i in range(1, 11):
#         table += f"{n} X {i} = {n*i}\n"

#     with open (f"tables/tables_{n}.text","w") as f:
#         f.write(table)

    
# for i in range(2, 21):
#     genratetable(i)

# Q.4
# word = "donkey"

# with open("donkey.text", "r") as f:
#     content = f.read()

# contentnew = content.replace(word, "####")

# with open("donkey.text", "w") as f:
#     content = f.write(contentnew)

# Q.5
# words = ["donkey", "lion", "dog"]

# with open("donkey.text", "r") as f:
#     content = f.read()

# for word in words:
#     content = content.replace(word, "#" * len(word))

# with open("donkey.text", "w") as f:
#     content = f.write(content)

# Q.6
# with open ("poem.text") as f:
#     content = f.read()

# if("twinkle" in content):
#     print("yes")

# else:
#     print("no")

# Q.7
# with open ("poem.text") as f:
#     lines = f.readlines()

# lineno = 1
# for line in lines:

#     if("twinkle" in lines):
#         print(f"yes its present in line no:{line}")
#         break
#     lineno += 1

# else:
#     print("no")

# Q.8 
# with open ("poem.text") as f:
#     content = f.read()

# with open ("poem_copy.text", "w") as f:
#     f.write(content)

# Q.9
# with open ("poem.text") as f:
#     content1 = f.read()

# with open ("donkey.text") as f:
#     content2 = f.read()

# if(content1 == content2):
#     print("files are identical")

# else:
#     print("files are not identical")

# Q.10
# with open ("poem_copy.text", "w") as f:
#     f.write("")

# Q.11
# with open ("old.txt") as f:
#     content = f.read()

# with open ("rename.txt", "w") as f:
#     f.write(content)

