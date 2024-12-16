user=(input(">>"))
for letter in user:
    if letter.isupper():
        user=user.replace(f"{letter}",f"_{letter.lower()}")
print(f"user : {user}")