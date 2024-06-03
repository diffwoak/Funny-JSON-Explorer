# Leaf类

class Leaf:
    def __init__(self, name, level = -1, icon = " ",state = ""):
        self.name = name
        self.level = level
        self.icon = icon
        self.state = state
    def set_icon(self,icon):
        self.icon = icon
    def get_state(self):
        return self.state
    def get_level(self):
        return self.level
    def draw(self):
        result = ""
        if self.level == -1:
            result += ":"
        result += f"{self.icon}{self.name}"
        return result