from turtle import Turtle
with open("data.txt", mode="r") as data:
    read_hs = data.read()


STYLE = ('Courier', 24, 'italic')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score =int(read_hs)
        self.color("white")
        self.penup()
        self.write_turtle()

    def write_turtle(self):
        self.clear()
        self.goto(0, 270)

        self.write(f"Score: {self.score} High score: {self.high_score}", font=STYLE, align='center')
        self.hideturtle()

    def rewrite_score(self):
        self.score += 1
        self.write_turtle()

    def reset_score(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as data:
                self.high_score = self.score
                data.write(str(self.high_score))



        self.score = 0
        self.write_turtle()









