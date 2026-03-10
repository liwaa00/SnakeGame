from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
       super().__init__()
       self.score=0#sonuç=نتيجة
       self.color("white")
       self.penup()
       self.goto(0,350)
       self.hideturtle()
       self.update_scoreboard()

    def update_scoreboard(self):#لوحة النتيجة
        self.write(f"score:{self.score}",align="center",font=("Arial",24,"normal"))

    def increase_score(self):#زيادة النتيجة
        self.clear()
        self.score+=1
        self.update_scoreboard()
    def game_over(self):
        self.screen.bgcolor("red")
        self.goto(0,0)
        self.write(f"Game Over \nFinal score:{self.score}",align="center",font=("Arial",25,"normal"))