# Работа с файлами
"""
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())
"""
# -------------------------------------
"""
# Создание списка строк по содержимому файла
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
"""
# -------------------------------------
"""
# Работа с содержимым файла
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

print(lines)

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
"""
# -------------------------------------
"""
# Большие файлы: миллион цифр
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}")
print(len(pi_string))
"""
# -------------------------------------
# Проверка дня рождения
"""
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appears in the first million digits of pi!")
"""
# --------------------------------
"""
# HW 10.1
filname = 'learning_python.txt'
with open(filname) as file_object:
    '''
    # 1
    contents = file_object.read()
print(contents.rstrip())
    '''
    '''
    # 2
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
    '''
    '''
    # 3
    lines = file_object.readlines()
content = ""
for line in lines:
    content += line
print(content)
'''
"""
# -------------------------------------
# HW 10.2
filname = 'learning_python.txt'
with open(filname) as file_object:
    lines = file_object.readlines()
for line in lines:
    line = line.replace('Python', 'C')
    print(line.rstrip())