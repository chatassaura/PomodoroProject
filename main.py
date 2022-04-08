from tkinter import *
import time
import math

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
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(txt_timer, text="00:00")
    lbl_timer.config(text="Timer", bg=YELLOW, fg=GREEN)
    ckb_active.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 2 == 1:
        count_down(WORK_MIN * 60)
        lbl_timer.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        lbl_timer.config(text="Break", fg=RED)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        lbl_timer.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(txt_timer, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        ckb_active.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
txt_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

lbl_timer = Label(text='Timer', font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
lbl_timer.grid(column=1, row=0)

btn_start = Button(text="Start", font=(FONT_NAME, 10, "bold"), bg=YELLOW, command=start_timer)
btn_start.grid(column=0, row=2)

btn_reset = Button(text="Reset", font=(FONT_NAME, 10, "bold"), bg=YELLOW, command=reset_timer)
btn_reset.grid(column=2, row=2)

ckb_active = Label(font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)
ckb_active.grid(column=1, row=3)

window.mainloop()
