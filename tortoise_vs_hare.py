
## This program shows a race between a Tortoise and a Hare from a sky view. We have here two functions, one for tortoise
# movement and the other for Hare movement. At the bottom we have a while loop to count the number of "seconds" the race takes.

# Below are the turtle operations used for the program

import turtle

tortoise = turtle.Turtle()
hare = turtle.Turtle()
course = turtle.Turtle()

title = turtle.Turtle()
title.penup()
title.goto(-110,100)
title.pendown()
title.color("deep pink")
title.write('TORTOISE VS. HARE - Who Will Win!?', font=16)
title.hideturtle()

result1 = turtle.Turtle()
result1.hideturtle()
result1.penup()
result1.goto(-110,-80)
result1.color("deep pink")
result1.pendown()

result2 = turtle.Turtle()
result2.hideturtle()
result2.penup()
result2.goto(-80,-100)
result2.color("deep pink")
result2.pendown()


course.penup()
course.setpos(-100,0)
course.right(-90)
course.pendown()
course.forward(50)
course.write('Start', font=19)
course.right(90)
course.penup()
course.forward(200)
course.right(90)
course.write('End', font=19)
course.pendown()
course.forward(50)
course.penup()
course.hideturtle()
course.setpos(-155,5)
course.penup()
course.write('Tortoise',font=16)
course.penup()
course.setpos(-135,35)
course.write('Hare', font=16)

tortoise.penup()
tortoise.color("red")
tortoise.setpos(-100,10)
tortoise.shape("turtle")
tortoise.shapesize(.5,.5)
hare.penup()
hare.color("blue")
hare.setpos(-100,40)
hare.shape("circle")
hare.shapesize(.5,.5)

# After importing random, we now have two function that calculate the x coordinates as the randint function gives values to move the tortoise/hare

import random

def hare2():
    if hare.xcor() >= -100 and hare.xcor() < 100:
        hare_turn = random.randint(1,10)
        if hare_turn >=1 and hare_turn <=2:
            hare.fd(7)
            if hare.xcor() > 100:
                hare.setpos(100,40)
        elif hare_turn == 3:
            hare.bk(10)
            if hare.xcor() < -100:
                hare.setpos(-100,40)
        elif hare_turn >=4 and hare_turn <=6:
            hare.fd(1)
            if hare.xcor() > 100:
                hare.setpos(100,40)
        elif hare_turn >= 7 and hare_turn <=8:
            hare.bk(2)
            if hare.xcor() < -100:
                hare.setpos(-100,40)
    else:
        quit()




def tort2():
    
    if tortoise.xcor() >= -100 and tortoise.xcor() < 100:
        tort_turn = random.randint(1,10)
        if tort_turn >= 1 and tort_turn <= 5:
            tortoise.fd(3)
            if tortoise.xcor() > 100:
                tortoise.setpos(100,10)
        elif tort_turn >= 6 and tort_turn <= 7:
            tortoise.bk(5)
            if tortoise.xcor() < -100:
                tortoise.setpos(-100,10)
        else:
            tortoise.fd(1)
            if tortoise.xcor() > 100:
                tortoise.setpos(100,10)
    else:
        quit()

# This is the while loop to count the number of iterations it takes for the race to complete

# Also, there is an if-else statement showing the results of the race!

i = 0
while hare.xcor() < 100 and tortoise.xcor() < 100:
    i += 1
    hare2()
    tort2()
    
    if hare.xcor() == 100:
        print(f'"Time" of race: {i} "seconds"')
        print(f'The Hare wins!')

        result1.write(f'"Time" of race: {i} "seconds"', font=16)
        result2.write(f'The Hare wins!', font=16)
        
    elif tortoise.xcor() == 100:
        print(f'"Time" of race: {i} "seconds"')
        print(f'The Tortoise wins!')

        result1.write(f'"Time" of race: {i} "seconds"', font=16)
        result2.write(f'The Tortoise wins!', font=16)
        
    else:
        continue

