import turtle
import pandas
import pyarrow

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
        print("same")

