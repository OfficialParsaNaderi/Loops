from os import system
system("cls")
start=int(input("enter start number:"))
end=int(input("enter end number:"))
step=int(input("enter step number:"))
for x in range(start,end,step):
    print(x)