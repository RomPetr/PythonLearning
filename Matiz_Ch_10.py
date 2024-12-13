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
# Большие файлы: миллион цифр
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}")
print(len(pi_string))