from random import randint
"""
# HW 9.13

class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        self.sides = randint(1, 6)
        print(self.sides)

die = Die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
"""
# -------------------------------------
# HW 9.14
initial = ['2', '4', 'A', '7', 'E', 'F', '9', 'Q', '1', 'J', '12', '45', '76', '5', '8']
win_ticket = []
my_ticket = []
counter = 0
for i in range(4):
    # popped = initial.pop(randint(0, 14))
    win_ticket.append(initial[randint(0, 14)])

str = str(win_ticket)

print(f"A ticket containing this combination {' '.join(win_ticket)} is a winner.")

while True:
    counter += 1
    for i in range(4):
        my_ticket.append(initial[randint(0, 14)])
    if my_ticket == win_ticket:
        print(f"Число попыток = {counter}")
        break
    else :
        my_ticket.clear()
