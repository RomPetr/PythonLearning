# Наследование
class Car():
    ''' Простая модель автомобиля '''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # назначение атрибуту значения по умолчанию
        self.odometer_reading = 0

    def get_descriptive_name(self):
        ''' Возвращает аккуратно отформатированное описание '''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        ''' Выводит пробег машины в милях'''
        print(f"This car has {self.odometer_reading} miles on it.")

    # изменение значения атрибута с использованием метода
    def update_odometer(self, mileage):
        '''
        Устанавливает заданное значение на одометре.
        При попытке обратной подкрутки изменение отклоняется
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    # изменение значения атрибута с приращением
    def increment_odometer(self, miles):
        ''' Увеличивает показания одометра с заданным приращением '''
        self.odometer_reading += miles

"""
class ElectricCar(Car):
    ''' Представляет аспекты машины, спецефические для электромобилей '''
    def __init__(self, make, model, year):
        '''
        Инициализирует атрибуты класса-родителя
        Затем инициализирует атрибуты, специфические для электромобиля
        '''
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        ''' Выводит информацию о мощности аккумулятора '''
        print(f"This car has a {self.battery_size}-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
"""
# -------------------------------------
# Экземпляры как атрибуты

class Battery():
    ''' Простая модель аккумулятора электромобиля '''
    def __init__(self, battery_size=75):
        ''' Инициализирует атрибуты аккумулятора '''
        self.battery_size = battery_size

    def describe_battery(self):
        ''' Выводит информацию о мощности аккумулятора '''
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        ''' Выводит приблизительный запас хода для аккумулятора '''
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    # HW 9.9
    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100


class ElectricCar(Car):
    ''' Представляет аспекты машины, спецефические для электромобилей '''
    def __init__(self, make, model, year):
        '''
        Инициализирует атрибуты класса-родителя
        Затем инициализирует атрибуты, специфические для электромобиля
        '''
        super().__init__(make, model, year)
        self.battery = Battery()

    # def describe_battery(self): # перемещен в класс Battery()
    #     ''' Выводит информацию о мощности аккумулятора '''
    #     print(f"This car has a {self.battery_size}-kWh battery.")


my_battery = Battery(90)
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# HW 9.9
print('\n')
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()