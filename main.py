from tkinter import *
import math
import pygame

PINK = "#FF9E9E"
RED = "#e7305b"
GREEN = "#285430"
TEAL = "#3A8891"
BLUE ="#DEF5E5"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    canvas.itemconfig(counter, text="00:00")
    global reps
    reps = 0

def start_timer():
    global reps
    reps += 1
    work_min_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(5)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(3)
    else:
        timer_label.config(text="Work", fg=TEAL)
        count_down(10)

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}" # dynamic typing python

    canvas.itemconfig(counter, text=f"{count_min}:{count_sec}") # itemconfig for canvas widget updates text
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        # play_sound()
        start_timer()
        checks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range (work_sessions):
            checks += "✓"
            check_marks.config(text=checks)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BLUE)

canvas = Canvas(width=200, height=224, bg=BLUE, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
counter = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label(text="Timer", font=(FONT_NAME, 50), bg=BLUE, fg=PINK)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, bg=BLUE,  command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=BLUE)
check_marks.grid(column=1, row=3)

window.mainloop()
