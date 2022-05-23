import turtle
import pandas

"""
def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
"""

screen = turtle.Screen()

screen.title("U.S States Game")

image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guess_state = []

while len(guess_state) < 50:

    answer_state = screen.textinput(
        title=f" {len(guess_state)}/50 Guess the state", prompt="What's another states name?: ").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guess_state:
                missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("state_to_learn")
        break
    if answer_state in all_states:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()


