class Plant:
    def __init__(self, name):
        self._name = name
    def describe(self):
        return f"{self._name} - это растение"
class Flower(Plant):
    def __init__(self, name, color):
        super().__init__(name)
        self._color = color
    def describe(self):
        return f"{self._name} - это цветок с цветом {self._color}"
class Tree(Plant):
    def __init__(self, name, height):
        super().__init__(name)
        self._height = height
    def describe(self):
        return f"{self._name} - это дерево высотой {self._height} метров"
Lil = Flower("Лилия", "красный")
Tree = Tree("Дуб", 10)
Daisy = Flower("Ромашка", "белый")
plants = [Lil, Tree, Daisy]
for plant in plants:
    print(plant.describe())