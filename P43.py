from os import system
system("Cls")
def greeting(p):
    for x in range (p):
        name1=input(">>")
        age1=int(input("<<"))
        print(f"{name1} is {age1} years old!")
for x in range(1):
    greeting(p=1)