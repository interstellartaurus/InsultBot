from random import choice

# Open and read from file
insults = open("insults.txt", "r")

# create variable and randomly pick a string from insults.text
line = choice(insults.readlines())

# print the string
biggie_string = (f"Yousa know what?! {line}")
print(biggie_string)
    
insults.close()


