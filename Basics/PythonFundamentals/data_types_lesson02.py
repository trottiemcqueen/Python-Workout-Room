# String data type

# literal assignment
first = "Trottie"
last = "McQueen"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# Constructor funciton
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like the music from the " + decade + "s."

# Multiple lines
multiline = '''
Hey, how are you?                                       
                                  
I was just checking in.
                                  
                                           All good?
'''
print(multiline)
print(multiline.replace("good", "ok"))
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
print(" ")

# Build a Menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$7".rjust(4))
print("Muffin".ljust(16, ".") + "$3".rjust(4))
print("Cheesecake".ljust(16, ".") + "$10".rjust(4))
print("BLT Sandwhich".ljust(16, ".") + "$5".rjust(4))
print("Pizza Slice".ljust(16, ".") + "$5".rjust(4))

print(" ")

# String index values
print(first[2])
print(first[-1])
print(first[0:])

