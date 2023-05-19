import time
import turtle
import random

#цвета ргб
PaleGoldenrod = 238, 232, 170
LimeGreen = 50, 205, 50
LightCyan = 224, 255, 255

score = 0 
high_score = 0
delay = 0.1


#экран
wind = turtle.Screen()
wind.title("Змейка")
wind.bgcolor("PaleGoldenrod")

wind.setup(width = 600, height = 600)
wind.tracer(0)

head = turtle.Turtle()
head.shape('square')
head.color('LimeGreen')
head.goto(0, 0)
head.penup()
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)
 
 
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("LightCyan")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center",
font=("Arial", 24, "bold"))

def group():
    if head.direction != "dowind":
        head.direction = "up"
 
def godowind():
    if head.direction != "up":
        head.direction = "dowind"
 
def goleft():
    if head.direction != "right":
        head.direction = "left"
 
def goright():
    if head.direction != "left":
        head.direction = "right"
 
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "dowind":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
 
wind.listen()
wind.onkeypress(group, "w")
wind.onkeypress(godowind, "s")
wind.onkeypress(goleft, "a")
wind.onkeypress(goright, "d")

segments = []
 
while True:
    wind.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("Arial", 24, "bold"))
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
 

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("Arial", 24, "bold"))

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()
 
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("Arial", 24, "bold"))
    time.sleep(delay)
 
wind.mainloop()