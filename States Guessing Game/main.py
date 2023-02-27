import turtle
import pandas

data = pandas.read_csv("50_states.csv")
states = data["state"]
xcor = data["x"]
ycor = data["y"]


myscreen = turtle.Screen()
myscreen.title("U.S states game")
image = "blank_states_img.gif"
myscreen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# myscreen.onscreenclick(get_mouse_click_coor)

game_is_on = True
guessed = []
while len(guessed) < 50:
    correct = 0
    answer_state = myscreen.textinput(title=f" {len(guessed)}/50 correct state", prompt= "next state?").title()
    print(answer_state)
    if answer_state == "Exit".title():
        break
    for state in states:
        if answer_state == state:
            if answer_state not in guessed:
                guessed.append(answer_state)

                coor = (data[data["state"] == answer_state])
                newx = int(coor["x"])
                newy = int(coor["y"])
                newturtle = turtle.Turtle()
                newturtle.hideturtle()
                newturtle.penup()
                newturtle.goto(newx, newy)
                newturtle.write(answer_state)


states_to_learn = []
for state in states:
    if state not in guessed:
        states_to_learn.append(state)
print(len(states_to_learn))

df = pandas.DataFrame(states_to_learn)
df.to_csv("states_to_lear.csv")


print(states_to_learn)



# myscreen.mainloop()

myscreen.exitonclick()