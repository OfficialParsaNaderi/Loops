user1 = input(">>")
user2 = input("<<")
user3 = input("<.>")
def parsa():
    while 50<100:
        if "end" in user1 or " end" in user2  : break
        if user1 != "parsa" : print(user1[1:4])
        if ":)" in user2 : print(user2.replace(":)","..."))
        word,number1,number2=user3.split()
        if word == "hello" :
            print(f"result : give you ${int(number1) * int(number2)} !")
        if word != "hello" :
            print(f"result : sorry ! I give you ${int(number1) / int(number2)}")
        if user3 == 50 :
            break
        if user3 == "end" :
            break