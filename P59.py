user1=0
while True:
    user2=input(">>")
    if "P" in user2[0]:
        user1 += 5
    elif user2 == "end":
        break
    else :
        continue
print(f"result : {user1}")