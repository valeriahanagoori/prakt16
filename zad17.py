# Задание Практика 17:
#
# 11.1) На основе ранее созданного класса Restaurant из прошлого задания
# создайте разновидность ресторана – «Кафе-мороженое». Напишите класс IceCreamStand,
# наследующий от класса Restaurant. Добавьте атрибут с именем flavors для хранения списка сортов мороженого.
# Напишите метод, который выводит этот список. Создайте экземпляр IceCreamStand и вызовите этот метод.
# 11.2) Модифицировать ранее созданный класс  IceCreamStand:
#    а)  Добавить атрибуты для описания локации и времени работы кафе-мороженого.
#    б)  Реализовать методы для добавления и удаления сортов мороженого из списка flavors.
#    в)  Реализовать метод для проверки наличия определенного сорта мороженого в списке flavors.
#    г)   Добавить методы для разных типов мороженого
#    (например, мороженое на палочке, мягкое мороженое, и т.д.) и реализовать методы для работы с каждым типом.

class Cleaner:
    def __init__(self, name):
        self.name = name
    def clean(self):
        print(f'Уборщик {self.name} только что сделал уборку')

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, cleaner_name,rating=0.0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating=rating
        self.cleaner = Cleaner(cleaner_name)
    def describe_restaurant(self):
        print(f'{self.restaurant_name} - это ресторан, у которого {self.cuisine_type} кухня и рейтинг: {self.rating}')
    def open_restaurant(self):
        print('Ресторан открыт')
    def update_rating(self,new_rating):
        self.rating = new_rating
        print(f'Обновлённый рейтинг ресторана {self.restaurant_name}: {self.rating}!')
    def cleaning(self):
        print(self.cleaner.clean())

class IceCreamStand(Restaurant):
    def __init__(self, flavors=[], location='', time='', restaurant_name='', cuisine_type='', cleaner_name='', rating=0.0):
        super().__init__(restaurant_name, cuisine_type, cleaner_name, rating=0.0)
        self.location = location
        self.time = time
        self.flavors = flavors
        self.popsicles = []
        self.soft = []
        self.wafer = []
        self.fruit_ice = []
    # def IceCreamLocation(self):
    #     print(f'Заведение находится по адресу: {location}')
    # def IceCreamTime(self):
    #     print(f'Часы работы заведения: {time}')
    def Popsicles(self,flavor):
        if flavor.lower() not in self.popsicles:
            self.popsicles.append(flavor.lower())
            print(f'Добавлено моложеное на палочке: {flavor}')
            if flavor.lower() not in self.flavors:
                self.flavors.append(flavor.lower())
        else:
            print('Мороженое на палочке с таким вкусом уже есть')

    def Soft(self,flavor):
        if flavor.lower() not in self.soft:
            self.soft.append(flavor.lower())
            print(f'Добавлено мягкое мороженое - {flavor}')
            if flavor.lower() not in self.flavors:
                self.flavors.append(flavor.lower())
        else:
            print('Мягкое мороженое с таким вкусом уже есть')
    def Wafer(self,flavor):
        if flavor.lower() not in self.wafer:
            self.wafer.append(flavor.lower())
            print(f'Добавлено мороженое в вафле со вкусом {flavor}')
            if flavor.lower() not in self.flavors:
                self.flavors.append(flavor.lower())
        else:
            print('Вафля с таким вкусом уже есть')
    def Fruit_ice(self,flavor):
        if flavor.lower() not in self.fruit_ice:
            self.fruit_ice.append(flavor.lower())
            print(f'Добавлен фруктовый лёд со вкусом {flavor}')
            if flavor.lower() not in self.flavors:
                self.flavors.append(flavor.lower())
        else:
            print('Фруктовый лёд с этим вкусом уже есть')
    def show_flavors_types(self):
        print(f'~ ~ ~ ~ ~ ~ ~ ~\nВСЕ ТИПЫ МОРОЖЕНОГО\nНа палочке: {", ".join(self.popsicles)}'
              f'\nМягкое: {", ".join(self.soft)}\nВафля: {", ".join(self.wafer)}'
              f'\nФруктовый лёд: {", ".join(self.fruit_ice)}\n~ ~ ~ ~ ~ ~ ~ ~')
    def add_flavor(self, flavor):
        if flavor.lower() not in self.flavors:
            self.flavors.append(flavor.lower())
            print(f"Вкус {flavor} добавлен в список")
        else:
            print('Этот вкус уже есть в списке')
    def remove_flavor(self, flavor):
        if flavor.lower() in self.flavors:
            self.flavors.remove(flavor.lower())
            print(f"Вкус {flavor} удалён из списка")
        else:
            print('Этого вкуса нет в списке')
    def find_flavor(self,flavor):
        if flavor.lower() in self.flavors:
            print(f"Вкус {flavor} в наличии!")
        else:
            print('Этого вкуса нет в наличии :(')
    def show_flavors(self):
        print(f'{self.restaurant_name}\nТекущие сорта: {', '.join(sorted(self.flavors))}\n~ ~ ~ ~ ~ ~ ~ ~')

# 1
IceCream = IceCreamStand(['Фисташка','Шоколад','Ваниль'], restaurant_name='Кафе-мороженое')
IceCream.show_flavors()
# 2
flavors_list = ['фисташка','шоколад','ваниль', 'клубника','лакрица']
flavors_stand = IceCreamStand(flavors_list,restaurant_name='Кафе-мороженое')
flavors_stand.Popsicles('Манго')
flavors_stand.Popsicles('Лакрица')
flavors_stand.Fruit_ice('Шоколад')
flavors_stand.Fruit_ice('Шоколад')
flavors_stand.Fruit_ice('Ваниль')
flavors_stand.Fruit_ice('Фисташка')
flavors_stand.Wafer('Шоколад')
flavors_stand.Soft('Клубника')
flavors_stand.add_flavor("Орео")
flavors_stand.find_flavor('Орео')
flavors_stand.remove_flavor("Орео")
flavors_stand.show_flavors_types()
flavors_stand.show_flavors()