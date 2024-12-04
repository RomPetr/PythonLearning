"""
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")
age = input("How old are you? ")
print(age)
"""

"""
# HW 7.2
Напишите программу, которая спрашивает у пользователя, на сколько мест он хочет забронировать
стол в ресторане. Если введенное число больше 8, выведите сообщение о том, что пользователю придется
подождать. В противном случае сообщите, что стол готов.

prompt = "How many seats would you like to reserve a table for? \n"
seats = int(input(prompt))
if seats > 8:
    print("Sorry, you'll have to wait a bit")
else:
    print("Okay, your table is reserved.")
"""
# --------------------------------------
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
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
"""
# -------------------------------------
"""
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
"""
# -------------------------------------
"""
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
"""
# -------------------------------------
"""
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
"""
# -------------------------------------
# HW 7.6
prompt = "\nHow old are you?"
prompt += "\nFor ending the program, please enter 'quit' "

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("The movie ticket is free for you.")
    elif age <= 12:
        print("For you, a movie ticket costs $10.")
    else:
        print("For you, a movie ticket costs $15.")

# -------------------------------------
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
# HW 7.9
sandwich_orders = ['BLT', 'Pastrami', 'Grilled Cheese', 'Philly Cheesesteak',
                   'pastrami', 'Reuben', 'Club Sandwich', 'PASTRAMI']
finished_sandwiches = []
print("Sorry, we're out of Pastrami sandwich")
for idx_sandwich in range(len(sandwich_orders)):
    if 'pastrami' in sandwich_orders[idx_sandwich].lower():
        continue
    else:
        print(f'I made your "{sandwich_orders[idx_sandwich]}" sandwich')
        finished_sandwiches.append(sandwich_orders[idx_sandwich])
print(f"I made the following few sandwiches: {', '.join(finished_sandwiches)}")
"""

"""
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(*pets)
while 'cat' in pets:
    pets.remove('cat')
print(' '.join(pets))
"""