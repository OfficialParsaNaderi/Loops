number1=50
while True:
    user1=input(">>")
    if "p" in user1 or "a" in user1:
        number1 += 10
        print(number1)
    if number1 == 100:
        break
    if number1 != 100:
        print("...")