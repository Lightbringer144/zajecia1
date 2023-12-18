class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f'Property Details:\n' \
               f'Area: {self.area} m2\nRooms: {self.rooms}\n' \
               f'Price: {self.price} zl\nAddress: {self.address}'


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'House Details:\n' \
               f'{super().__str__()}\nPlot Size: {self.plot} m2'


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Flat Details:\n' \
               f'{super().__str__()}\nFloor: {self.floor}'


house1 = House(200, 5, 300000, "Katowice, Zygmunta Krasinskiego 1", 500)
flat1 = Flat(80, 3, 150000, "Katowice, Warszawska 38", 2)

print("\n====================\n")
print(house1)
print("\n====================\n")
print(flat1)
print("\n====================\n")