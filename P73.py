from random import randint,randrange,choice
from string import ascii_letters

user_password1 = []
letters1 = tuple(ascii_letters)
for letter in range (15) :
    user_password1.append(choice(letters1))
for letter in user_password1 :
    print(f"{letter}",end ="")