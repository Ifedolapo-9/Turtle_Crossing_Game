FONT = ("Courier", 50, "normal")


from turtle import Turtle
class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.color = ("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level {self.level}", FONT)

    def increase(self):
        self.level += 1
        self.update()

    def over(self):
        self.goto(0, 0)
        self.write("GAME OVER", FONT)




