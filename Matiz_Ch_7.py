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
"""
prompt = "How many seats would you like to reserve a table for? \n"
seats = int(input(prompt))
if seats > 8:
    print("Sorry, you'll have to wait a bit")
else:
    print("Okay, your table is reserved.")

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