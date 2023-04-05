import tkinter as tk
import pandas as pd

# ---------------- constant -----------------#
FONT_NAME = "Courier"
MAIN_C1 = "#ECF2FF"
MAIN_C2 = "#3E54AC"
MAIN_C3 = "#655DBB"
TEXT_C1 = "#a9a4de"
TEXT_C2 = "#bfffad"
TEXT_C3 = "#ffb8e6"

word_index = 0
correct_cnt = 0
count = 60
timer = None
is_press = False


# ---------------- function -----------------#
def check_typing(event):
    global word_index, correct_cnt
    word_index += 1
    canvas.itemconfig(past_word_2, text=canvas.itemcget(past_word_1, "text"), fill=canvas.itemcget(past_word_1, "fill"))
    if canvas.itemcget(curr_word, "text") == type_en.get():
        canvas.itemconfig(past_word_1, text=canvas.itemcget(curr_word, "text"), fill=TEXT_C2)
        correct_cnt += 1
    else:
        canvas.itemconfig(past_word_1, text=canvas.itemcget(curr_word, "text"), fill=TEXT_C3)
    canvas.itemconfig(curr_word, text=words_list[word_index])
    canvas.itemconfig(next_word_1, text=words_list[word_index+1])
    canvas.itemconfig(next_word_2, text=words_list[word_index+2])
    type_en.delete(0, 'end')


def count_down(event):
    global timer, count, correct_cnt, is_press
    count -= 1
    if count >= 0:
        timer = window.after(1000, count_down, count)
        time_lb.config(text=count)
    else:
        canvas.itemconfig(past_word_2, text="")
        canvas.itemconfig(past_word_1, text="")
        canvas.itemconfig(curr_word, text=f"{correct_cnt} wpm")
        canvas.itemconfig(next_word_1, text="")
        canvas.itemconfig(next_word_2, text="")
        reset_btn.focus()
        type_en.delete(0, 'end')


def reset_all():
    global word_index, correct_cnt, count, timer, words_list, is_press
    word_index = 0
    correct_cnt = 0
    count = 60
    timer = None
    is_press = False
    words_list = word_data.sample(100).values[:, 0]
    canvas.itemconfig(past_word_2, text="")
    canvas.itemconfig(past_word_1, text="")
    canvas.itemconfig(curr_word, text=words_list[word_index])
    canvas.itemconfig(next_word_1, text=words_list[word_index+1])
    canvas.itemconfig(next_word_2, text=words_list[word_index+2])
    time_lb.config(text=f"{count}")


# ---------------- word data ------------------- #
word_data = pd.read_csv("oxford-5000.csv", header=None)
words_list = word_data.sample(100).values[:, 0]


# ----------------- window --------------------- #
window = tk.Tk()
window.title("Typing Speed")
window.config(padx=150, pady=50, bg=MAIN_C1)

title_lb = tk.Label(text="Typing Speed Test", font=(FONT_NAME, 45, "bold"), bg=MAIN_C1, fg=MAIN_C2)
title_lb.grid(row=0, column=1, pady=30)

canvas = tk.Canvas(width=500, height=300, bg=MAIN_C3)
past_word_2 = canvas.create_text(250, 40, text="", font=(FONT_NAME, 20, "bold"))
past_word_1 = canvas.create_text(250, 80, text="", font=(FONT_NAME, 20, "bold"))
curr_word = canvas.create_text(250, 150, text=words_list[word_index], fill="white", font=(FONT_NAME, 40, "bold"))
next_word_1 = canvas.create_text(250, 220, text=words_list[word_index+1], fill=TEXT_C1, font=(FONT_NAME, 20, "bold"))
next_word_2 = canvas.create_text(250, 270, text=words_list[word_index+2], fill=TEXT_C1, font=(FONT_NAME, 20, "bold"))
canvas.grid(row=1, column=1)

time_lb = tk.Label(height=3, text="60", bg=MAIN_C1, fg=MAIN_C2, font=(FONT_NAME, 12, "normal"))
time_lb.grid(row=2, column=1)

type_en = tk.Entry(justify="center", bg="white", font=(FONT_NAME, 30, "bold"), borderwidth=0)
type_en.grid(row=3, column=1)
type_en.bind("<FocusIn>", count_down)
type_en.bind("<Return>", check_typing)

reset_btn = tk.Button(text="Reset", bg=MAIN_C1, fg=MAIN_C2, font=(FONT_NAME, 12, "normal"), command=reset_all)
reset_btn.grid(row=4, column=1, pady=30)

window.mainloop()
