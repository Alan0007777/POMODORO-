from tkinter import *
from math import floor

RED = "#cc244b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20  
SECONDS = 60
timer = None
check_no = 0
reps = 0

# CREATING A WINDOW 
window = Tk()
window.title("POMODORO APP")
window.config(padx=50 , pady=50 , bg=YELLOW)

# CRETING A COUNTDOWN
def count_down(count):
    global timer

    count_min = floor(count / 60)
    count_sec = count % 60
    if count_min < 10 :
        count_min = "0"+ str(count_min)
    
    if count_sec < 10 :
        count_sec = "0"+ str(count_sec)

    if count >= 0:
        canvas.itemconfig(timer_text , text= f"{count_min}:{count_sec}")
        timer = window.after(1000 , count_down , count-1)
    else:
        start_timer()


# CREATING A CANVAS INSIDE THE WINDOW
canvas = Canvas(height=230 , width=210 , bg=YELLOW, highlightthickness= 0)
image = PhotoImage(file="tomato.png")
canvas.create_image(105 , 115 , image= image)
timer_text = canvas.create_text(105 , 125 , text="00:00" , fill="white" , font=(FONT_NAME , 35 , "bold") )
canvas.grid(row=3, column=1)

# ADDING ENTRY FOR HEADER
header = Label(text="TIMER" , font=(FONT_NAME , 40 , "bold") , fg=GREEN , bg=YELLOW)
header.grid(row=0 , column=1)

# ADDING START BUTTON
def start_timer():
    global WORK_MIN , SHORT_BREAK_MIN , LONG_BREAK_MIN , reps , check_no 
    reps += 1
    work_sec = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60 
    if reps > 8:
        reset_timer() 
        return
    if reps == 8:
        check_no += 1
        check.config(text= check_no *  '✔')
        header.config(text="BREAK" , fg=RED)
        count_down(long_break)
    elif reps % 2 != 0:
        header.config(text="WORK" , fg=GREEN)
        count_down(work_sec)
    else:
        check_no += 1
        check.config(text=check_no * '✔')
        header.config(text="BREAK" ,fg=RED)
        count_down(short_break)



start = Button(text="START" ,bg= YELLOW, command= start_timer )
start.grid(row=6 , column=0)

# ADDING RESET BUTTON 
def reset_timer():
    global reps , check_no
    window.after_cancel(timer)
    canvas.itemconfig(timer_text , text= "00:00")
    header.config(text="TIMER" , fg=GREEN)
    reps = 0
    check_no = 0

reset = Button(text="RESET" ,bg= YELLOW,command= reset_timer)
reset.grid(row=6 , column=2)

# CREATING PROGRESS BAR
check = Label(text="" , bg=YELLOW , fg=GREEN )
check.grid(row =7, column=1)

window.mainloop()
