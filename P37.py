from os import system
system("cls")
for x in range(5):
    number = int(input("enter number :"))
    if  number % 2 == 0:
        print("number is Couple ")
else :
    print("number is Man")