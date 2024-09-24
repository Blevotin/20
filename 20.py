class Vehicle:
    def __init__(self, __model, owner, __engine_power, __color):
        self.__model = __model
        self.owner = owner
        self.__engine_power = __engine_power
        self.__color = __color
        self.__COLOR_VARIANTS = ['red', 'black', 'white']

    def get_model (self):
       print(f"Модель {self.__model}")

    def get_horsepower(self):
        print(f"Мощность двигателя {self.__engine_power}")

    def get_color(self):
        print(f"Цвет {self.__color}")

    def print_info(self):
        self.get_model()
        self.get_color()
        self.get_horsepower()
        print(F"Владелец {self.owner}")

    def set_colors(self,  new_color):
        new_color2 = new_color.lower()
        new_color = new_color2
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    def __init__(self, model, owner, engine_power, color):
        super().__init__(model, owner, engine_power, color)
    __PASSENGERS_LIMIT = 5
    def set_colors(self,  new_color):
        new_color2 = new_color.lower()
        new_color = new_color2
        super().set_colors(new_color)


# vh = Vehicle("Audi", "Анатолий", 133, "red")
# vh.print_info()
# vh.set_colors("black")
# vh.print_info()
sd = Sedan("BMW", "Дмитрий", 155, "red")
sd.print_info()
sd.set_colors("bLack")
