# A start I guess
# Wish me luck
# ;)

import turtle

# Setup

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-345,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(345,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

# Functions
    #Paddle A
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

    #Paddle B
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

    #Ball

# Keyboard binding
wn.listen()
    #Paddle A
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
    #Paddle B
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    #Border Checking
    if(ball.xcor() >= 400 or ball.xcor() <= -400):
        ball.goto(0,0)
    if(ball.ycor() >= 300 or ball.ycor() <= -300):
        ball.dy = -ball.dy

    #Collision
    if(345 <= ball.xcor() <= 365 and paddle_b.ycor()-50 <= ball.ycor() <= paddle_b.ycor()+50):
        ball.dx *= -1
      #  ball.dy *= -1
    if(-345 >= ball.xcor() >= -365 and paddle_a.ycor()-50 <= ball.ycor() <= paddle_a.ycor()+50):
        ball.dx *= -1
      #  ball.dy *= -1

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Update
    wn.update()