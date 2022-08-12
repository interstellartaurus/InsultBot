ls /etc/from random import choice


insults = open("insults.txt", "r")


line = choice(insults.readlines())
mozza_string = (f"Yousa know what?! {line}")
print(mozza_string)
    
insults.close()


