class component:
    def __init__(self, name, grade, conditions):
        self.name = name
        self.grade = grade
        self.conditions = conditions

    def operate(self):
        pass

    def copy(self):
        return component(self.name, self.grade, self.conditions)







# MAKE COMPONENTS


# EVERY COMPONENTS USED IN GAMEPLAY
pool = []
