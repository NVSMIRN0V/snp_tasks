class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories

    def _get_name(self):
        return self._name

    def _set_name(self, name):
        self._name = name

    def _get_calories(self):
        return self._calories

    def _set_calories(self, calories):
        self._calories = calories

    def is_healthy(self):
        if isinstance(self.__calories, (int, float)):
            return self.__calories < 200
        return False

    def is_delicious(self):
        return True


class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        self._name = name
        self._calories = calories
        self._flavor = flavor

    def _get_flavor(self):
        return self._flavor

    def _set_flavor(self, flavor):
        self._flavor = flavor

    def is_delicious(self):
        return not self._flavor == 'black licorice'
