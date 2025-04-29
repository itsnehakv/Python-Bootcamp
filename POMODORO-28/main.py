from math import trunc, floor
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.03
SHORT_BREAK_MIN = 0.03
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    global reps
    reps=0
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(countdown_text, text="00:00")  #(what we want to change, what r the changes)
    tickmark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps #it is global bcs we do not want it to keep resetting
    reps+=1
    work_count=WORK_MIN*60
    short_break_count=SHORT_BREAK_MIN*60
    long_break_min=LONG_BREAK_MIN*60

    if reps%2==1:
        count_down(work_count)
        timer_label.config(text="Work", fg=RED, font=("Vivaldi", 45, "bold"))
    elif reps==8:
        count_down(long_break_min)  #placed before short_break_count bcs we need to weed out reps==8 before it reaches if reps%2==0
        timer_label.config(text="Long break!", fg=GREEN,font=("Vivaldi", 30, "bold"))

    elif reps%2==0:
        count_down(short_break_count)
        timer_label.config(text="Short break!", fg=GREEN, font=("Vivaldi", 30, "bold"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 4
def count_down(count):
    count_seconds=int(round(count%60,2))
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    '''what i did initially..'''
    # length=0
    # for digit in count_seconds:
    #     length+=1
    # if length==1:
    #     count_seconds=f"0{count_seconds}"


    canvas.itemconfig(countdown_text, text=f"{trunc(count/60)}:{count_seconds}")
    '''If you need to configure the Canvas item dynamically, then tkinter provides itemconfig(**options) method.'''
    '''text=f"{math.floor(count/60)}'''
    if count>0:
        global timer
        timer=window.after(1000, count_down, count-1)
    else:  # i.e when count_down ends
        start_timer()
        mark=""
        for i in range(floor(reps/2)): #bcs reps/2==float value
            mark+="✔"
        tickmark.config(text=mark)
    '''after: executes command after a time delay. after(ms, func, *args), The arguments passed in *args is passed onto func'''
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.minsize(width=400, height=400)
window.title("POMODORO 🍅")
window.config(background='#FFCCE1')
window.config(padx=100, pady=50)


tickmark=Label(text="", fg=GREEN, bg="#FFCCE1", font=(20)) #fg colors text elements, bg = background of canvas
tickmark.grid(column=1, row=2)
tickmark.config(padx=50, pady=20)

timer_label=Label(text="Timer", fg=GREEN, bg="#FFCCE1", font=("Vivaldi", 45, "bold"))
timer_label.grid(column=1, row=0)
timer_label.config(pady=10)

start_button=Button(text="Start", font=("Perpetua", 15, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button=Button(text="Reset", font=("Perpetua", 15, "bold"), command=reset_time)
reset_button.grid(column=2, row=2)

canvas=Canvas(width=220, height=224, bg='#FFCCE1', highlightthickness=0) #highlightthickness removes border
tomato=PhotoImage(file="tomato.png") #reads through file to fetch image
canvas.create_image(105,112,image=tomato) #half of canvas size so it is right in the center. image="tomato.png", is not possible
countdown_text=canvas.create_text(100,130, text="00:00", fill="white", font=("Perpetua", 24, "bold"))
canvas.grid(column=1, row=1)

#function should be called below canvas creation bcs we access canvas through canvas.itemconfig()


window.mainloop()
