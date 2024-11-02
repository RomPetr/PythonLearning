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
# HW 7.8
sandwich_orders = ['BLT', 'Grilled Cheese', 'Philly Cheesesteak', 'Reuben', 'Club Sandwich']
finished_sandwiches = []
for sandwich in sandwich_orders:
    print(f'I made your "{sandwich}" sandwich')
    finished_sandwiches.append(sandwich)
print(f"I made the following few sandwiches: {', '.join(finished_sandwiches)}")
"""
# --------------------------------------

"""
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(*pets)
while 'cat' in pets:
    pets.remove('cat')
print(' '.join(pets))
"""