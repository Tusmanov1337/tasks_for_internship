class Dessert:

    def __init__(self, name= '', calories= ''):
        self.name = name
        self.calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        
    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, calories):
        self._calories = calories
    
    def is_healthy(self):
        try: 
            return self.calories < 200
        except TypeError:
            return False

    def is_delicious(self):
        return isinstance(self, Dessert)
