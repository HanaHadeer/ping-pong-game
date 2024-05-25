import turtle

# Setup window
window = turtle.Screen()
window.title("Ping Pong Game By Hana")
window.setup(width=800, height=600)
window.tracer(
    0)  # video games are pictures and frames that are refreshed in very high speed, when you refresh the frame don't make time interval (delay)
window.bgcolor(.1, .1, .1)  # (r,g,b) from 0(black) to 1(white)

# Setup game objects
### Ball ###
ball = turtle.Turtle()
ball.speed(0)  # drawing speed(fastest) - it takes values from 1 to 10 . Here, 0 means the fastest speed (which is 10)
ball.shape("square")
ball.color("white")
# Scale factor * default size (20px * 20px)
ball.shapesize(stretch_len=1, stretch_wid=1)
ball.goto(x=0, y=0)
# Stop drawing lines when moving
ball.penup()
ball_dx, ball_dy = 1, 1
ball_speed = .2     # multiply it later in the game loop by the dx & dy to control the ball speed (based on your device's speed)


### Center line ###
center_line = turtle.Turtle()
center_line.speed(0)
center_line.shape("square")
center_line.color("white")
# width => 500px = 25 * 20px default
# #.1 equals 2 pixels
center_line.shapesize(stretch_len=.1, stretch_wid=25)
center_line.penup()
center_line.goto(0, 0)


### Player1 ###
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_len=1, stretch_wid=5)  # 20px, 100px
player1.color("blue")
player1.penup()
player1.goto(-350, 0)


### Player2 ###
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_len=1, stretch_wid=5)  # 20px, 100px
player2.color("red")
player2.penup()
player2.goto(350, 0)


### Score text ###
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(0, 260)
score.write("Player1: 0 Player2: 0", align="center", font=("Courier", 14, "normal"))
# If we didn't determine the shape of the object, it will show the normal shape which is arrow, the score text will be written above this arrow
score.hideturtle()  # We hide the object (arrow) bcs we only want to see the text
p1_score, p2_score = 0, 0   #variables to hold player 1 & player 2 scores


# Players Movement
players_speed = 20
def p1_move_up():
    player1.sety(
        player1.ycor() + players_speed)  # player1.ycor() gives you the current coordination of p1 on y and then add 20 for each press


def p1_move_down():
    player1.sety(player1.ycor() - players_speed)


def p2_move_up():
    player2.sety(player2.ycor() + players_speed)


def p2_move_down():
    player2.sety(player2.ycor() - players_speed)


# Get users inputs (Key Bindings)
window.listen()  # Tell the window to expect user input
window.onkeypress(p1_move_up, "w")  # Ensure the keyboard in "En" and "small letters"
window.onkeypress(p1_move_down, "s")

window.onkeypress(p2_move_up, "Up")  # Ensure the keyboard in "En" and "small letters"
window.onkeypress(p2_move_down, "Down")

# Game loop
# this part is executing with every frame or refresh of the screen during the game
while True:
    window.update()

    ball.setx((ball.xcor() + (ball_dx * ball_speed)))
    ball.sety((ball.ycor() + (ball_dy * ball_speed)))

    # Ball & borders collisions
    if(ball.ycor() > 290):  # 290 => 300(top border) - 10(half ball size)
        ball.sety(290)
        ball_dy *= -1       # invert y direction

    if (ball.ycor() < -290):  # 290 => 300(top border) - 10(half ball size)
        ball.sety(-290)
        ball_dy *= -1         # invert y direction

    # Ball & players collisions
    # Collision with player1
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (player1.ycor()-60) and ball.ycor() < (player1.ycor()+60):
        ball.setx(-340)
        ball_dx *= -1

    # Collision with player2
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() > (player2.ycor()-60) and ball.ycor() < (player2.ycor()+60):
        ball.setx(340)
        ball_dx *= -1

    # score handling
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_dx *= -1   # invert x direction
        score.clear()
        p1_score += 1
        score.write(f"Player1: {p1_score} Player2: {p2_score}", align="center",
                    font=("Courier", 14, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_dx *= -1  # invert x direction
        score.clear()
        p2_score += 1
        score.write(f"Player1: {p1_score} Player2: {p2_score}", align="center",
                    font=("Courier", 14, "normal"))