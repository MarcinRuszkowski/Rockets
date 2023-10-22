class Rocket:
    def __init__(self, height=0):
        self.hight = height

    def move_up(self):
        self.height += 1
        return self.height