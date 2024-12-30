# Запись в файл
"""
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
"""
# -------------------------------------
"""
# HW 10.3
name = input("Please, enter your name: ")
with open('guest.txt', 'w') as f:
    f.write(name)
"""
# -------------------------------------
"""
# HW 10.4
with open('guest_book.txt', 'a') as file:
    while(True):
        name = input("Please, enter your name, for quit type 'q': ")
        if name.lower() == 'q':
            break
        greeting = f'Hello, {name}\n'
        file.write(greeting.title())
"""
# -------------------------------------
"""
# division_calculator
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while(True):
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
"""
# -------------------------------------
"""
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Подсчет приблизительного количества слов в файле.
    words = contents.split()
    # print(words)
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
"""