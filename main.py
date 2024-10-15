from tkinter import *
from tkinter import Label

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title_text.config(text="Timer")
    canvas.itemconfig(timer_time,text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    # options = [work_secs, short_break_secs, long_break_secs]

    reps += 1
    if reps % 8 == 0:
        count_down(long_break_secs)
        title_text.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        title_text.config(text="Break", fg=PINK)
    else:
        count_down(work_secs)
        title_text.config(text="Work", fg=GREEN)

    # count_down(option)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = int(count/60)   #or import math, math.floor(count/60)
    if count_min < 10:
        count_min = f"0 {count_min}"
    """dynamic typing"""

    count_sec = count % 60
    display_sec = count_sec
    if count_sec < 10:
        display_sec = "0" + str(count_sec)
    """changing data type manually"""

    canvas.itemconfig(timer_time, text=f"{count_min}:{display_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        window.attributes('-topmost',1)
        window.attributes('-topmost', 0)
        window.after(1000, start_timer)
        checks = ""
        sessions = int((reps+1)/2)    #so the check appears after a work session, not after a break
        for i in range(sessions):
            checks += "✔"
        check_marks.config(text=checks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# def say_something(a,b,c):
#     print(a)
#     print(b)
#     print(c)
#
# window.after(1000, say_something, 3, 6, 4)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)     #numbers are position
timer_time = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title_text = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "normal"), bg=YELLOW)
title_text.grid(row=0, column=1)

button_start = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset",width=0, highlightbackground=YELLOW, command=reset_timer)
button_reset.grid(row=2, column=2)

check_marks = Label(bg=YELLOW, fg=GREEN)
check_marks.grid(row=3, column=1)



window.mainloop()