from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard
window=Screen()
window.bgcolor("black")
window.setup(800,800)
window.tracer(0)

sam=Snake()
food=Food()
score=Scoreboard()

game_on=True
while game_on:
    sam.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(sam.up,"Up")
    window.onkey(sam.down,"Down")
    window.onkey(sam.left,"Left")
    window.onkey(sam.right,"Right")
    if sam.head.distance(food) < 17:#distance=aradaki mesafe
        food.appear()
        sam.extend()
        score.increase_score()

    if sam.head.xcor()>370 or sam.head.xcor()<-370 or sam.head.ycor()>370 or sam.head.ycor()<-370:
        game_on=False  
        score.game_over()

    for segment in sam.turtels[0:-1]:
        if sam.head.distance(segment)<10:
            game_on=False
            score.game_over()

window.exitonclick()