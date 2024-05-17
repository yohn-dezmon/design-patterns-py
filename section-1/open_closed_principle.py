from enum import Enum

class Color(Enum):
    RED = 1 
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color 
        self.size = size 


# Bad way of doing things
class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p


# Good way of doing things


class Specification:
    """A class that determines whether or not a particular item
    satisfies a particular criterion.
    
    """
    def is_satisfied(self, item):
        # you override this method
        pass

class Filter:
    def filter(self, items, spec):
        # you extend/override this
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color
    
    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size
    
    def is_satisfied(self, item):
        return item.size == self.size
    
class AndSpecification(Specification):
    # why do we initialize this with *args?
    def __init__(self, *args):
        self.args = args 
    
    def is_satisfied(self, item):
        # all checks that every argument is a boolean value
        # where is `spec` defined?
        # oh in the input of the lambda function lol
        # ok so you call map over self.args, and for each one you want to get 
        # back a true value from the lambda
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))
    
class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house] 

    # 11:56
    pf = ProductFilter()
    print('Green products (old): ')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f'product {p.name} is green')
    

    bf = BetterFilter()

    print("Green products (new):")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f'product {p.name} is green')
    
    large = SizeSpecification(Size.LARGE)
    print("large blue items:")
    large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    for p in bf.filter(products, large_blue):
        print(f' - {p.name} is large')
    

