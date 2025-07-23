class Dessert:

    def __init__(self, name=None, calories=None):
        self.name = name
        self.calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) == str:
            self._name = name
        else:
            self._name = None

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, calories):
        if type(calories) not in (int, float):
            self._calories = None

    def is_healthy(self):
        if self._calories is None:
            return False

        else:
            return self.calories < 200

    def is_delicious(self):
        return isinstance(self, Dessert)

