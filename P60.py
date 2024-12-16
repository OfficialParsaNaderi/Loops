from turtle import fd,lt,Screen,Turtle,done
parsa = Turtle()
while True :
        user1 = input("<.>").title()
        if "Circle" in user1 : parsa.circle(radius=60)
        elif "Sqaure" in user1 :
                for i in range(4):
                        parsa.fd(100)
                        parsa.lt(90)
        elif "Rectangle" in user1 :
                for i in range(2):
                        parsa.fd(230)
                        parsa.lt(90)
                        parsa.fd(130)
                        parsa.lt(90)
        elif "End"in user1 :
                Screen().bye()
                break
done()