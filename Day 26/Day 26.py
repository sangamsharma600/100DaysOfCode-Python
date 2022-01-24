import math
from pydoc import text
from tkinter import *
import tkinter
from turtle import title, width
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
after_timer = None
ticks = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer(): 
    global ticks
    global reps
    window.after_cancel(after_timer)
    timer.config(text="Timer")
    canvas.itemconfig(timer_text, text= "00:00")
    ticks = ""
    check_mark.config(text=ticks)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    countdown(WORK_MIN)



# COUNTDOWN #

def countdown(count):
    global ticks
    global after_timer
    global reps
    count_minute = math.floor(count/60)
    if reps == 0:
        timer.config(text="Work",font=(FONT_NAME,35,'bold'),fg=GREEN)
    count_sec= count%60
    if count_sec==0:
        count_sec="00"
    elif count_sec<10:
        count_sec=f"0{count}"
    canvas.itemconfig(timer_text,text = f"{count_minute} : {count_sec}")
    print(count)
    if count>0:
       after_timer =  window.after(1000,countdown,count -1)
    elif count == 0:
        ticks += "✔"
        check_mark.config(text=ticks)
        reps += 1
        if reps == 1 or reps == 3 or reps == 5:
            countdown(SHORT_BREAK_MIN )
            timer.config(text="Break",font=(FONT_NAME,35,'bold'),fg=PINK)
        elif reps == 2 or reps == 4 or reps == 6:
            countdown(WORK_MIN  )
            timer.config(text="Work",font=(FONT_NAME,35,'bold'),fg=GREEN)
        elif reps == 7:
            countdown(LONG_BREAK_MIN )
            timer.config(text="Break",font=(FONT_NAME,35,'bold'),fg=RED)




     



# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Remind Me")
window.config(padx=120,pady=80,bg=YELLOW)
canvas = Canvas(width=200, height=224,bg= YELLOW, highlightthickness=0)
image_location = PhotoImage(file = "Day 26/tomato.png")
canvas.create_image(100,112,image = image_location)
timer_text = canvas.create_text(100,130,text="00 : 00",fill = "white",font=("Arial",26,"bold"))
timer = Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)
start = Button(text="Start",command=start_timer)
reset = Button(text="Reset",command=reset_timer)
check_mark = Label(font=(FONT_NAME,13,'bold'),fg=GREEN,bg=YELLOW)


check_mark.grid(row=3,column=1)
reset.grid(row=2,column=2)
start.grid(row=2,column=0)
timer.grid(row=0,column=1)
canvas.grid(row=1,column=1)











window.mainloop()