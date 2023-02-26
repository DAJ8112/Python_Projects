import turtle
import pandas
screen = turtle.Screen()
screen.title('U.S States Game')

'''
code to get the coordinates of states so that we can map out the names one's the user gets it correct
note: this is already done in the data file so no need here.
def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()  # Alternative to keeping our screen open because if we use exitonclick 
so when we will click it will not exit 
'''


def prompt(correct):
    answers = screen.textinput(title=f"{correct}/50 States Correct", prompt="What's another state's name?").title()
    return answers


# some variables to be used in further program
correct_answer = 0
guessed_answers = []
# Set image as background
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Data reading from data file
data = pandas.read_csv("./50_states.csv")
states = data.state
states_list = states.to_list()
print(states_list)

tim = turtle.Turtle()
tim.penup()
tim.hideturtle()

while len(guessed_answers) < 50:
    answer = prompt(correct_answer)
    if answer in states_list and answer not in guessed_answers:
        guessed_answers.append(answer)
        correct_answer += 1
        state_row = data[data.state == answer]
        tim.goto(int(state_row.x), int(state_row.y))
        tim.write(answer)
