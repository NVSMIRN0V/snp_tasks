class Dessert:
    def __init__(self, name=None, calories=None):
        self.name = name
        self.calories = calories

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_calories(self):
        return self.calories

    def set_calories(self, calories):
        self.calories = calories

    def is_healthy(self):
        if isinstance(self.calories, (int, float)):
            return self.calories < 200
        return False

    def is_delicious(self):
        return True


class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        self.name = name
        self.calories = calories
        self.flavor = flavor

    def get_flavor(self):
        return self.flavor

    def set_flavor(self, flavor):
        self.flavor = flavor

    def is_delicious(self):
        return not self.flavor == 'black licorice'