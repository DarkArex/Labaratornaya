class Plant:
    def __init__(self, name):
        self._name = name
        self._growth_stage = 1
    def grow(self):
        self._growth_stage += 1
    def describe(self):
        if self._growth_stage == 1:
            return f"{self._name} - это молодое растение"
        elif self._growth_stage == 2:
            return f"{self._name} - это зрелое растение"
        else:
            return f"{self._name} - это цветущее растение"
Lil = Plant("Лилия")
print(Lil._name)
print(Lil.describe())
