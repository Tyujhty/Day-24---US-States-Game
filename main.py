import turtle
import pandas
import pyarrow

def write_name(name, x_coord, y_coord):
    show_state = turtle.Turtle()
    show_state.hideturtle()
    show_state.penup()
    show_state.color("black")
    show_state.goto(x=int(x_coord), y=int(y_coord))
    show_state.write(arg=name, font=("Arial", 10, "normal"), align="center")


screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(725, 491)

turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another State's name?")

state_list = pandas.read_csv("50_states.csv")
state_names = state_list["state"]

for name in state_names:
    if name.lower() == answer_state.lower():
        answer_to_print = state_list[state_names == name]
        x_coord = answer_to_print['x']
        y_coord = answer_to_print['y']
        write_name(name, x_coord, y_coord)



