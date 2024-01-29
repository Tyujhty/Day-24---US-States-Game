import turtle
import pandas

FONT_STATE_NAME = ('Arial', 10, 'normal')
FONT_SCOREBOARD = ('Arial', 24, 'normal')
ALIGN = 'center'
IMAGE = "blank_states_img.gif"
OUTPUT_NAME = "missing_state_list.csv"

def write_name(answer_state, x_coord, y_coord):
    show_state = turtle.Turtle()
    show_state.hideturtle()
    show_state.penup()
    show_state.color("black")
    show_state.goto(x=int(x_coord), y=int(y_coord))
    show_state.write(arg=answer_state, font=FONT_STATE_NAME, align=ALIGN)

def create_scoreboard(score):
    scoreboard.hideturtle()
    scoreboard.penup()
    scoreboard.goto(x=0, y=260)
    scoreboard.clear()
    scoreboard.write(arg=f"Number of State found: {score}/50", font=FONT_SCOREBOARD, align=ALIGN)

def update_scoreboard(score):
    scoreboard.clear()
    scoreboard.write(arg=f"Number of State found: {score}/50", font=FONT_SCOREBOARD, align=ALIGN)

screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(IMAGE)
screen.setup(725, 600)

turtle.shape(IMAGE)

state_list = pandas.read_csv("50_states.csv")
state_names = state_list["state"].to_list()
state_found = []

score = 0
scoreboard = turtle.Turtle()

game_is_on = True

while len(state_found) <= 50:
    create_scoreboard(score)
    answer_state = screen.textinput(title="Guess the State", prompt="What's another State's name?").title()

    if answer_state.title() == "Exit":
        missing_states = []
        for state in state_names:
            if state not in state_found:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(OUTPUT_NAME)
        break

    if answer_state in state_names:
        state_found.append(answer_state)
        answer_to_print = state_list[state_list.state == answer_state]
        x_coord = int(answer_to_print['x'].iloc[0])
        y_coord = int(answer_to_print['y'].iloc[0])
        write_name(answer_state, x_coord, y_coord)
        score += 1
        update_scoreboard(score)

