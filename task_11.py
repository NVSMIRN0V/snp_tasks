class Dessert:
    def __init__(self, name=None, calories=None):
        self.__name = name
        self.__calories = calories

    def _get_name(self):
        return self.__name

    def _set_name(self, name):
        self.__name = name

    def _get_calories(self):
        return self.__calories

    def _set_calories(self, calories):
        self.__calories = calories

    def is_healthy(self):
        return self.__calories < 200

    def is_delicious(self):
        return True
