def parsa():
    p=float(input(">>").replace("🎈",""))
    print(f"parsa: {p}")
parsa()
def poyan():
    n=int(input("<<"))
    print(f"poyan: {n}")
parsa()
from turtle import fd,lt,done
def shape(parsa):
    for x in range(3):
        fd(parsa)
        lt(120)
for x in range(170,300,20):
    shape(parsa=x)
done()