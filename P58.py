user1=(input(">>"))
while True:
    for letter in user1:
        if letter.isupper():
            user1=user1.replace(f"{letter}",f".{letter.lower()}")
    print(f"user1 : {user1}")
    if user1 != "parsa.naderi":
            print("....")
    if user1 == "parsa.naderi":
        break