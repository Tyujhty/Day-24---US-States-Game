import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(725, 491)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another State's name?")
print(answer_state)
