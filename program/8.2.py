class Plant:
    def __init__(self, name):
        self.name = name
        self.growth_stage = 1
    def grow(self):
        self.growth_stage += 1
    def describe(self):
        if self.growth_stage == 1:
            return f"{self.name} - это молодое растение"
        elif self.growth_stage == 2:
            return f"{self.name} - это зрелое растение"
        else:
            return f"{self.name} - это цветущее растение"
Lil = Plant("Лилия")
print(Lil.describe())
Lil.grow()
print(Lil.describe())