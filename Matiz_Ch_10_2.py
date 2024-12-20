"""
# Работа с несколькими файлами
def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Подсчет приблизительного количества слов в файле.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
"""
# -------------------------------------
"""
# HW 10.6
n1 = input("Enter the first number: ")
try:
    n1 = int(n1)
except ValueError:
    print("This is not number!")
else:
    n2 = input("Enter the second number: ")
    try:
        n2 = int(n2)
    except ValueError:
        print("This is not number!")
    else:
        print(f"Summ of {n1} and {n2} is {n1+n2}")
"""
# -------------------------------------
"""
# HW 10.7
while(True):
    n1 = input("Enter the first number (for quit, enter 'q'): ")
    if n1.lower() == 'q':
        break
    try:
        n1 = int(n1)
    except ValueError:
        print("This is not number!")
    else:
        n2 = input("Enter the second number: ")
        try:
            n2 = int(n2)
        except ValueError:
            print("This is not number!")
        else:
            print(f"Summ of {n1} and {n2} is {n1+n2}")
"""
# -------------------------------------
"""
# HW 10.8, 10.9
def read_pets_name(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
        # print(f"Sorry, the file {filename} does not exist.")
    else:
        # Вывод кличек животных
        # names = contents.split()
        print(contents.title())

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    read_pets_name(filename)
"""
# -------------------------------------
# HW 10.10
filename = 'little_women.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Подсчет приблизительного количества слова 'the' в файле.
    numbers = contents.lower().count('the ')
    print(f"The average number of word 'the' is {numbers}")