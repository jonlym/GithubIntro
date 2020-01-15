class Dog:
    def __init__(self, name, favorite_color='gray'):
        self.name = name
        self.favorite_color = favorite_color
        
    def bark(self):
        print(('My name is {} and my favorite color is {}. Er... I mean... '
               'bark bark'.format(self.name, self.favorite_color)))