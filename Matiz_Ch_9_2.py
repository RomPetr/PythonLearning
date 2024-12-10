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