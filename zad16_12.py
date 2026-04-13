#1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type,rating=0.0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating=rating
    def describe_restaurant(self):
        print(f'{self.restaurant_name} - это ресторан, у которого {self.cuisine_type} кухня')
    def open_restaurant(self):
        print('Ресторан открыт')


newRestaurant = Restaurant('Кидо','японская')
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()


#2
print()
Rest1 = Restaurant('Фрида','мексиканская')
Rest2 = Restaurant('Пармеджано','итальянская')
Rest3 = Restaurant('Олень','скандинавская')
Rest1.describe_restaurant()
Rest2.describe_restaurant()
Rest3.describe_restaurant()
