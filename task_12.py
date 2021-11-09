class Dessert:
    def __init__(self, name=None, calories=None):
        self.name = name
        self.calories = calories

    def _get_name(self):
        return self.name

    def _set_name(self, name):
        self.name = name

    def _get_calories(self):
        return self.calories

    def _set_calories(self, calories):
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

    def _get_flavor(self):
        return self.flavor

    def _set_flavor(self, flavor):
        self.flavor = flavor

    def is_delicious(self):
        return not self.flavor == 'black licorice'