# Create a basic class example
class Pen:
    origin = 'China'
    material = 'Plastic'

    # basic constructor
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # a random function just for poc
    def print_info(self):
        print('Brand: {brand} \nColor: {color}'.format(
            brand = self.brand,
            color = self.color,
        ))

    # create a class method, that will be shared with all Pen instances
    @classmethod
    def get_brand(cls):
        print('Origin: {origin} \n'.format(
            origin = cls.origin
        ))

# creates a new class that has a inheritance on Pen class
class Pencil(Pen):
    origin = 'Brazil'
    material = 'Wood'

    def __init__(self, brand, color):
        # uses the python super() method to get the constructor and functions of Pen()
        super().__init__(brand, color)

# instantiate the classes
pen = Pen(brand='Bic', color='Blue')
pen.print_info()
pen.get_brand()

pencil = Pencil(brand='Faber Castell', color='Grey')
pencil.print_info()
pencil.get_brand()
