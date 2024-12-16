from os import system
system("cls")
for parsa in range(5):
    print(parsa)
value1=float(input("enter your number school class  ?:"))
print("value1",value1)
value2=int(input("enter your number english class ?:"))
print("value2",value2)
value3=input("enter weather name or number ?:")
print("value3",value3)
if value3 == ('hot'):
    print("weather is hot!")
elif value3 == ('cold'):
    print("weather is cold!")
elif value1<value2:
    result1=value1*value2+2
    print("result1",result1)
    print("youre number class school and english good ")
elif value1>value2:
    result2=value1/value2-2
    print("result2",result2)
else:
    print("youre number class school and english bad ! ")