class Rectangle:
    def __init__(self, width, height):
        self._width = width 
        self._height = height 

        # we're going to expose width and height as properties instead of 
        # exposing them directly 
    
    @property 
    def area(self):
        return self._width * self._height 
    
    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property 
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value 

    
    @property 
    def height(self):
        return self._height 
    
    @height.setter
    def height(self, value):
        self._height = value 

class Square(Rectangle):
    """ 
    at first we'll design this such that it breaks use_it()
    even though it's a child class of Rectangle
    """
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
    
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value 

    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value 



def use_it(rc):
    w = rc.width 
    # this ends up changing the width as well... (for square)
    rc.height = 10
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')

rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(5)


"""
Solution?
- don't create a square class lol
- don't change the way getters/setters work!

"""
