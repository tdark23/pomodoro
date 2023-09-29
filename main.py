from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✔️"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


reps = 0 # repetition number
timer_running = False  # Flag to indicate if the timer is running
paused_time = 0  # Store the time remaining when paused
remaining_time = WORK_MIN * 60  # New variable to store remaining time

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(count_down)
    canvas.itemconfig(timer_text, text="00:00")
    session_label.config(text="Work", fg=GREEN)


# ---------------------------- TIMER PAUSE ------------------------------- # 

def pause_timer():
    global timer_running, paused_time
    if timer_running:
        # Stop the timer and store the remaining time
        window.after_cancel(count_down)
        timer_running = False 
        # Update the paused_time variable
        paused_time = remaining_time

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps, timer_running
    work_sec = WORK_MIN * 60  # Convert work minutes to seconds

    if not timer_running:
        timer_running = True
        if reps % 8 == 7:
            count_down(LONG_BREAK_MIN * 60)
            session_label.config(text="Long Break", fg=RED)
        elif reps % 2 == 0:
            count_down(remaining_time)  # Use the remaining_time
            session_label.config(text="Work", fg=GREEN)
        else:
            count_down(SHORT_BREAK_MIN * 60)
            session_label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps, remaining_time
    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    if count >= 0:
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        remaining_time = count  # Update the remaining time
        window.after(1000, count_down, count - 1)
    else:
        reps += 1
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔️"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



session_label = Label(text="Work", fg=GREEN, font=(FONT_NAME, 30), background=YELLOW)
session_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start 🏁", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)


reset_button = Button(text="Reset 🔄", highlightthickness=0, command=reset_timer)
reset_button.grid(column=0, row=4)

pause_button = Button(text="Pause ⏸️", command=pause_timer, highlightthickness=0)
pause_button.grid(column=2, row=2)

play_button = Button(text="Play ▶️ ", command=start_timer, highlightthickness=0)
play_button.grid(column=2, row=4)

check_mark = Label(text="", fg=GREEN, background=YELLOW)
check_mark.grid(column=1, row=3)


window.mainloop()