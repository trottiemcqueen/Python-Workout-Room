greeting = 'hello world!'
print(greeting)

# Variables
name001 = 'Trottie' # name001 is the variable - assisgn a value
_name001 = 'Trot' # can not start variable with numbers
print(name001, _name001)

# Fun
line01 = "********************"
line02 = "*                  *"
line03 = "*     WELCOME!     *"

print('')
print(line01)
print(line02)
print(line03)
print(line01)
print(line01)

# Python Operators
  # Assignment operator '='
  # Arithmatic op '+', '-', '/', '%', '**', '*', '//' plus more we will run into soon
  
multipli = 2 * 2
print(multipli)

subtr = 9 - 5
print(subtr)

divi = 100 / 2
print(divi)

remainderof = 24 % 5
print(remainderof)

anotherdiv = 200 // 3
print(anotherdiv)

tothepower = 2 ** 3
print(tothepower)

  # Assign variables to operators as well
meaning = 99
print(meaning)

meaning += 1
print(meaning)

meaning -= 10
print(meaning)

meaning *= 20
print(meaning)

meaning /= 2
print(meaning)

meaning = round(meaning)
print(meaning)

# Comparison operators and if / else statements
meanings = 42
print('')

if meanings > 10:
  print('Right on!')
else:
  print('Not today')

# Ternary Operator
print('Right on!') if meanings > 10 else print('Not today aye')