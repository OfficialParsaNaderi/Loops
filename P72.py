from random import randint,randrange,choice
while True :
    number1 = int(input(">>"))
    number2 = int(input("<<"))
    if number1 <= number2 :
        number3 = randint(number1,number2)
        print(number3)
        break
    else :
        print(" Thaks , that Wrong !")
print(" Finished !")