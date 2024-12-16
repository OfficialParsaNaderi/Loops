with open("text1.txt" , "r") as file :
    data = file.readlines()
    for line in data :
        word = line.split()
        print(word)