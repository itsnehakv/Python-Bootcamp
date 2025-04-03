import turtle as t
import pandas

screen=t.Screen()
screen.title("U.S STATES")
image="blank_states_img.gif"
screen.addshape(image)
''''in turtle, when we need to make use of an image, it has to be in .gif format
This function is used to Add a turtle shape to TurtleScreen’s shapelist.'''
t.shape(image) #the image is "added" to the turtle shapelist bcs of prev func. now we use it


state_data=pandas.read_csv("50_states.csv")
state_list=state_data.state.to_list()

guessed_states=[]
missed_states=[]
while len(guessed_states)<50:
    user_answer = screen.textinput(title=f"You got {len(guessed_states)}/51 states", prompt="Whats the state name?").title()
    if user_answer=="Exit":
        for state in state_list:
            if state not in guessed_states:
                missed_states.append(state)
        new_data=pandas.DataFrame(missed_states)
        new_data.to_csv("new_states_to_learn.csv")
        break #exits while loop
    if user_answer in state_list:   #"in" keyword only works w/ lists
        guessed_states.append(user_answer)
        turt=t.Turtle()
        turt.penup()
        turt.hideturtle()
        answer_state_data=state_data[state_data.state==user_answer]  #accesses the state name that matches user_answer
        turt.goto(answer_state_data.x.item(),answer_state_data.y.item())
        turt.write(user_answer)  #or print(answer_state_data.state.item())

screen.exitonclick()
'''orrr turtle.mainloop()'''
