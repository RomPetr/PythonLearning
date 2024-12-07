"""
import Matiz_Ch_8_Pizza

Matiz_Ch_8_Pizza.make_pizza(16, 'pepperoni')
"""
# -------------------------------------
"""
# Импортирование конкретных функций
from Matiz_Ch_8_Pizza import make_pizza

make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
"""
# -------------------------------------
# Назначение псевдонима для функции
from Matiz_Ch_8_Pizza import make_pizza as mp

mp(16, 'pepperoni')
