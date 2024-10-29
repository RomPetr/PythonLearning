
"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see you next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")
# -----------------------------------------------
"""

"""
# преобразование рез-тов range() в список с пом-ю list()
numbers = list(range(1,6))
print(numbers)

# вывод четных чисел
event_numbers = list(range(2,11,2))
print(event_numbers)
#------------------------------------------------

# создание списка квадратов чисел
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
"""

"""
# минимум, максимум и сумма чисел списка
digits = [1,2,3,4,5,6,7,8,9,0]
print(f"минимальное число списка: {min(digits)}")
print(f"Максимальное число списка: {max(digits)}")
print(f"Сумма чисел в списке: {sum(digits)}")
#------------------------------------------------
"""

"""
# генераторы списков
# генератор списка квадратов числа
squares = [value**2 for value in range(1, 11)]
print(f"Квадраты чисел {[n for n in range(1, 11)]} равны {squares}")
"""

'''
# генератор кубических корней с точностью три знака после запятой
nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
nums1 = [round(num ** (1 / 3), 3) for num in nums]
print(nums1)
'''


"""
# сегменты в списках
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
print(players[2:])
print(players[-3:])
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
"""

"""
# копирование списка через сегмент
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
"""


"""
# 4.1
pizzas = ['Margherita', 'Pepperoni', 'Hawaiian', 'BBQ Chicken', 'Four Cheese']

for pizza in pizzas:
    print(f"I like {pizza}")
print("I really love pizza!")
"""

"""
# 4.4 генератор списка из эл-тов от 1 до 1 000 000
nums = [val for val in range(1, 1000001)]
print(nums)
"""

"""
# 4.5 суммирование от 1 до 1000000
nums = [val for val in range(1, 1000001)]
print(min(nums))
print(max(nums))
print(sum(nums))
"""

"""
# 4.6 вывод нечетных чисел от 1 до 20
nums = [val for val in range(1,20,2)]
print(nums)
"""

"""
# 4.7 вывод чисел, кратных 3 в диапазоне от 3 до 30
nums = [val for val in range(3,31,3)]
print(nums)
"""

"""
# 4.9 генератор кубов
cubs = [val**3 for val in range(1, 11)]
print(cubs)
"""