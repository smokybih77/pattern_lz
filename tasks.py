# вариант 4
# 1 строитель

class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.windows = None

    # чтоб красиво выводило
    def __str__(self):
        return f'Дом: стены = {self.walls}, крыша = {self.roof}, окна = {self.windows}'


class HouseBuilder:
    def __init__(self):
        self.house = House()

    def set_walls(self, w):
        self.house.walls = w
        return self

    def set_roof(self, r):
        self.house.roof = r
        return self

    def set_windows(self, w):
        self.house.windows = w
        return self

    def build(self):
        result = self.house
        self.house = House()
        return result



# 2 компоновщик

class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self, indent=0):
        print(' ' * indent + f'{self.name} — {self.price} руб.')   # ' ' * indent делает отступы пробелами


class Combo:
    def __init__(self, name):
        self.name = name
        self.items = []     # список для блюд и комбо

    def add(self, item):
        self.items.append(item)

    def show(self, indent=0):
        print(' ' * indent + f'набор: {self.name}')
        for item in self.items:
            item.show(indent + 2)



# 3 команда

class Light:
    def on(self):
        print('свет включен')

    def off(self):
        print('свет выключен')


class LightOnCommand:
    def __init__(self, light_object):
        self.light = light_object       # привязка команды к обьекту света

    def execute(self):
        self.light.on()     # включение света при выполнении


# аналогично включению выключение
class LightOffCommand:
    def __init__(self, light_object):
        self.light = light_object

    def execute(self):
        self.light.off()


class Remote:
    def __init__(self):
        self.cmds = []      #очередь команд

    def add(self, command):
        self.cmds.append(command)

    def run(self):
        for cmd in self.cmds:   # ывполнение команд из очереди
            cmd.execute()
