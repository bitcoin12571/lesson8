import turtle # turtle librarie folosim toata

#turtle initializatiom
broasca =turtle.Turtle()#broasca este un nume

for i in range(3):# 3 laturi
    broasca.forward(200)
    broasca.right(120)

turtle.exitonclick()# cand apesi  pe clik iese din program
turtle.done()#termin

import random

win = random.randint (1,6)
answer =int(input("Enter number"))
life = True

while life:
    if answer == win:
        print("you lose")
        life =False
        break
    else:
        print("u have one more change")
    answer =int(input("Enter number "))
