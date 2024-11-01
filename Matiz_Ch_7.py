"""
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")
age = input("How old are you? ")
print(age)
"""

"""
# HW 7.3
num = input("Please, enter some number: ")
num = int(num)
if num % 10 == 0:
    print(f"This number: {num} is a multiple of 10")
else:
    print(f"This number: {num} is not a multiple of 10")
"""
# --------------------------------------
"""
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(*pets)
while 'cat' in pets:
    pets.remove('cat')
print(' '.join(pets))
"""