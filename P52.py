from time import sleep
user1=(0)
while (user1<50):
    user3=int(input(">>"))
    if user3==5 or user3==10:
        user1=int(user3)+user1
        print(f"result : ${user1}")
        sleep(1)
    if user1 == 50:
        break