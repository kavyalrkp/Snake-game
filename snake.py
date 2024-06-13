import turtle
import time
import random

delay = 0.1

#Score
score = 0
high_score = 0

#set up screen
# wn=windows
wn=turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0) #turns off screen updates

#snake head
head = turtle.Turtle()
head.speed(0) #animation speed
head.shape("square")
head.color("blue")
head.penup() #doesnt draw anything when its moving
head.goto(0,0) #starts at centre of the the screen
head.direction="stop" #the head doesn't move when the window is opened

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup() #doesnt draw anything when its moving
food.goto(0,100) #starts at centre of the the screen

segments = []


# Pen
pen=turtle.Turtle()
pen.speed(0)
pen.direction="stop"
pen.color("black")
pen.shape("square")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions

def go_up():
    if head.direction != "down":
          head.direction = "up"

def go_down():
    if head.direction != "up":      
          head.direction = "down"

def go_right():
    if head.direction != "left":      
          head.direction = "right"

def go_left():
    if head.direction != "right":
          head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)   


# Keyboard bindings (connects a particular key press to a function)
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")

# Main game loop
while True:
    wn.update()

    #check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
          print("GAME OVER!")

          time.sleep(1)
          head.goto(0,0)
          head.direction="stop"

          # Hide the segments
          for segment in segments:
                segment.goto(1000, 1000)
          # Clear the segments list
          segments.clear()

          #reset the score
          score = 0

          #update score display
          pen.clear() # clears the previous score off the screen     
          pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
      
          #reset the delay
          delay = 0.1
          

    #check for a collision with the food
    if head.distance(food) < 20:
          #Move the food to a random spot
          x=random.randint(-290,290)
          y=random.randint(-290,290)
          food.goto(x,y)


          # Add a segment
          new_segment = turtle.Turtle()
          new_segment.speed(0)
          new_segment.shape("square")
          new_segment.color("navy")
          new_segment.penup()
          segments.append(new_segment)

          #shorten the delay
          delay -= 0.01

          # Increase the score
          score += 10

          if score > high_score:
               high_score = score

          pen.clear() # clears the previous score off the screen     
          pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
          x= segments[index-1].xcor()
          y=segments[index-1].ycor()
          segments[index].goto(x,y)

    # Move segment 0 to where the head is
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move()

    # Check for head collisions with the body segments
    for segment in segments:
          if segment.distance(head) < 20:
              print("GAME OVER!")

              time.sleep(1)
              head.goto(0,0)
              head.direction="stop"
              # Hide the segments
              for segment in segments:
                    segment.goto(1000, 1000)

                # Clear the segments list
              segments.clear()     

              #reset the score
              score = 0

              pen.clear() # clears the previous score off the screen     
              pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

              #reset the delay
              delay = 0.1


    time.sleep(delay)

wn.mainloop() #keeps the window open 