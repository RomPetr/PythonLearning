import unittest
from name_function import get_formatted_name

"""
print("Enter 'q' at any time to quit.")
while(True):
    first = input("Please, give me a first name: ")
    if first == 'q':
        break
    last = input("Please, give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}")
"""
# -------------------------------------
class NamesTestCase(unittest.TestCase):
    """ Тесты для 'name_function.py' """

    def test_first_last_name(self):
        """ Имена вида 'Janis Joplin' работают правильно? """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()