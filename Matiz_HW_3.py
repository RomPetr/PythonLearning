"""
motocyles = ['honda', 'java', 'kawasaki', 'harley', 'ducati']
motocyles.append('suzuki') #добавил мотоцикл suzuki в конец списка
print(motocyles)
motocyles.insert(0, 'upiter') #добавил мотоцикл Upiter  начало списка
print(motocyles)
del motocyles[2] #удалил мотоцикл Java
print(motocyles)
message = f"I would like to buy a {motocyles[2].title()} motorcycle"
print(message)
motocyles.insert(5, 'yamaha') #добавил мотоцикл yamaha на 5ю позицию. suzuki сместился по индексу 6
print(motocyles)
popped_motorcycle = motocyles.pop(0) #удалил мотоцикл Upiter
print(motocyles)
print(f"Deleted the {popped_motorcycle.title()}.")
last_owned = motocyles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")
too_expensive = 'ducati'
motocyles.remove(too_expensive) #удалил мотоцикл Ducati
print(motocyles)
print(f"A {too_expensive.title()} is too expensive for me.")
"""

'''
#-----
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
cars.sort() # отсортировано в алфавитном порядке
print(cars)
cars.sort(reverse=True) # отсортировано в обратном алфавитном порядке
print(cars)
print("----")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is sorted list:")
print("------sorted()--------")
print(sorted(cars)) # временная сортировка на момент вывода на экран
print(("---sorted(cars, reverse=True)---"))
print(sorted(cars, reverse=True)) #  временная сортировака в обратном алф. порядке
print("------original list----------")
print(cars)
cars.reverse() # сортировка в обратном порядке
print("------reverse()--------")
print(cars)
print(f"Количество автомобилей в списке: {len(cars)}")
'''

"""
#-----
# 3.1
names = ['alex', 'bob', 'kristina', 'thomas']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(f"My first frend is {names[0].title()}")
"""

"""
# 3.3
motorcycles = ['honda', 'java', 'kawasaki', 'harley', 'ducati', 'triumph']
print(f"I'd like to bye the {motorcycles[3].title()} motorcycle.")
"""

'''
# 3.4
guests = ['alice', 'robert', 'chistian', 'alex'] # формируем список гостей
for i in range(len(guests)): # шлем приглашения гостям в цикле
    print(f"Dear, {guests[i].title()}. I'm waiting for you for dinner on October 12 at 19-00")
print("----")


# 3.5
popped = guests.pop(3) # убрали из списка гостя по имени Алекс
print(f"Guest {popped.title()} is not will come")
guests.append('lucy') #добавили гостя по имени Люси
print(f"Guest {guests[-1].title()} is will come instead {popped.title()}")
for i in range(len(guests)):
    print(f"Dear, {guests[i].title()}. I'm waiting for you for dinner on October 12 at 19-00")
print("----")


# 3.6
guests.insert(0, 'shon') #добавили гостя по имени Шон в начало списка
print(f"Also {guests[0].title()} is will come")
guests.insert(3, 'mark')
print(f"Also {guests[3].title()} is will come too")
for i in range(len(guests)): # шлем приглашения гостям в цикле
    print(f"Dear, {guests[i].title()}. I'm waiting for you for dinner on October 12 at 19-00")
print("----")
'''

"""
# 3.7
for i in range(4):
    deleted = guests.pop()
    print(f"Unfortunately, I cannot host you, {deleted.title()}. I'm sorry")
j = len(guests)
for i in range(j):
    print(f"\nDear, {guests[i].title()}. I'm waiting for you for dinner on October 12 at 19-00")
    print(f"{i}")
del guests[0]
print(guests)
"""

'''
# 3.8
countries = ['Holland', 'Bulgaria', 'Mexico', 'Nicaragua', 'China', 'India']
print("Initial order")
print(countries)
print('---')
print("'sorted()' order")
print(sorted(countries))
print("come back again")
print(countries)
print('---')
print("'sorted(reverse=True)' order")
print(sorted(countries, reverse=True))
print("come back again")
print(countries)
print('---')
countries.reverse()
print("'.reverse()' method")
print(countries)
print('---')
countries.reverse()
print("'.reverse()' method again")
print(countries)
print('---')
countries.sort()
print("'.sort()' alphabetical sort method")
print(countries)
print('---')
countries.sort(reverse=True)
print("'.sort(reverse=True)' reverse alphabetical sort method")
print(countries)
'''

"""
# 3.9
guests = ['alice', 'robert', 'chistian', 'alex']  # формируем список гостей
for i in range(len(guests)):  # шлем приглашения гостям в цикле
    print(f"Dear, {guests[i].title()}. I'm waiting for you for dinner on October 12 at 19-00")

print(f"{len(guests)} guests were invited to dinner")
"""