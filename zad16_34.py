#3 и 4

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


Rest_rating = Restaurant('Абоба','русская','Валерий', 5.5)
Rest_rating.describe_restaurant()
Rest_rating.update_rating(10.0)
Rest_rating.describe_restaurant()
print()

Rest_rating.cleaning()
