import time
from snake import Snake
from turtle import Screen
from food import Food
from score import Score
#screen settings
Screen().setup(width=600, height=600)
Screen().bgcolor("black")
Screen().title("Snake Game")
Screen().tracer(0)

#make snake and food and scoreboard
snake = Snake()
food=Food()
score=Score()

#activating the keyboard
Screen().listen()
Screen().onkey(snake.up, "Up")
Screen().onkey(snake.down, "Down")
Screen().onkey(snake.left, "Left")
Screen().onkey(snake.right, "Right")

score.write(f'SCORE: {score.score}' ,move=False, align="center", font=('Arial', 19, 'normal'))
score.hideturtle()
#moving snake
play= True
while play:
    Screen().update()
    time.sleep(0.1)
    snake.move()
    #food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.inc()
        snake.extend()

    #collision with wall
    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        play = False
        score.goto(x=0, y=0)
        score.write(f'  GAME OVER\n\nFINAL SCORE: {score.score}', move=False, align="center", font=('Arial', 19, 'normal'))

    #tail collision
    for t in snake.tims:
        if t == snake.head:
            pass
        elif snake.head.distance(t) <10:
            play = False
            score.goto(x=0, y=0)
            score.write(f'  GAME OVER\n\nFINAL SCORE: {score.score}', move=False, align="center", font=('Arial', 19, 'normal'))


#exir screen
Screen().exitonclick()