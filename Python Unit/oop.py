# from collections import Counter
# my_counter = Counter('oompa loompa')  # Counter({'p': 2, 'o': 2, 'm': 2, 'a': 2, ' ': 1, 'l': 1, 'u': 1})
# isinstance(my_counter, Counter)  # True
# my_counter.most_common()  # [('p', 2), ('o', 2), ('m', 2), ('a', 2), (' ', 1), ('l', 1), ('u', 1)]

# from datetime import date
# today = date.today()  # datetime.date(2020, 3, 24)
# today.weekday()  # 2

# get/set attr of obj o.name
# call method o.method()
# retrieve value from dict o['key']

# help - how to use
# dir - methods/attr to use



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~classes~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# from math import sqrt
# from random import randint

# class Triangle:
#     """
#     A class used to represent a right triangle
    
#     Attributes
#     ~~~~~~~~~~
#      a: int
#       length of side a
#     b: int
#       length of side b
#     """
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def __repr__(self):
#         //for devs/debugging
#         return f"Triangle(a={self.a}, b={self.b})"
    
#     def __str__(self):
#         //for users
#         return self.describe()
    
#     def __eq__(self, other):
#         //for ==
#         return self.a == other.a and self.b == other.b

#     @classmethod 
#     def random(cls):
#         """Class method which returns triangle with random sides"""
#         return cls(randint(1,20),randint(1,20))          #make a new instance of the class
    
#     def get_hypotenuse(self):
#         """Caluclates the hypotenuse (3rd side of rihgt triangle)"""
#         return sqrt(self.a**2 + self.b**2)
    
#     def get_area(self):
#         """Calculates the area of the right triangle"""
#         return self.a * self.b / 2
    
#     def describe(self):
#         """Returns string representing triangle"""
#         return f'I am a triangle with sides: {self.a} and {self.b}.'
    

    # tri = Triangle(3,4)
    # tri   #  <__main__.Triangle at 0x7fb99c2efa30>
    # def __repr__(self):
    #     return f"Triangle a={self.a}, b={self.b}" # Triangle a=3, b=4
    
