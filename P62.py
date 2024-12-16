from turtle import *
parsa = Turtle()
def user1(poyan):
    user2 = input("<.>")
    if user2 == "circle" :
        parsa.circle(radius=60)
    elif user2 == "rectangle" :
        for i in range(2):
            parsa.fd(230)
            parsa.lt(90)
            parsa.fd(130)
            parsa.lt(90)
    elif user2 == "sqaure":
        for i in range(4):
            parsa.fd(poyan)
            parsa.lt(90)
    if user2 == "end":
        Screen().bye()
for i in range(5,110,50):
    user1(poyan=i)
done()