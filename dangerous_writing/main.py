import tkinter as tk

MAIN_C1 = '#E8F9FD'
MAIN_C2 = '#0AA1DD'
MAIN_C3 = '#2155CD'

WAIT_TIME = 5
timer = None

# 색상 그라데이션
red_diff = int((int(MAIN_C1[1:3], 16) - int(MAIN_C3[1:3], 16)) / (WAIT_TIME * 4 - 1))
green_diff = int((int(MAIN_C1[3:5], 16) - int(MAIN_C3[3:5], 16)) / (WAIT_TIME * 4 - 1))
blue_diff = int((int(MAIN_C1[5:7], 16) - int(MAIN_C3[5:7], 16)) / (WAIT_TIME * 4 - 1))

colors = [MAIN_C1]
for i in range(1, WAIT_TIME * 4):
    # 각 구간마다 색상 계산
    r = int(MAIN_C1[1:3], 16) - (i * red_diff)
    g = int(MAIN_C1[3:5], 16) - (i * green_diff)
    b = int(MAIN_C1[5:7], 16) - (i * blue_diff)
    color = f"#{r:02x}{g:02x}{b:02x}"
    colors.append(color)


# 입력 후 지정한 시간을 카운트 함과 시간이 지날수록 글씨가 투명해 짐
def count_down(count):
    global timer
    if count > 0:
        text_box.config(fg=colors[count-1])
        timer = window.after(1000//4, count_down, count - 1)
    else:
        text_box.delete(0.0, "end")


# 키가 눌렸을 때의 함수
def key_press(event):
    global timer
    if timer:
        window.after_cancel(timer)
    count_down(WAIT_TIME * 4)


window = tk.Tk()
window.title("Most Dangerous Writing")
window.config(padx=100, pady=30, bg=MAIN_C1)

title_lb = tk.Label(text="Write anything", bg=MAIN_C1, fg=MAIN_C3, font=('Corbel', 30, 'bold'))
title_lb.grid(row=0, column=1, pady=20)

text_box = tk.Text(window, width=100, height=25, wrap="word")
text_box.config(bg=MAIN_C1, fg=MAIN_C3, borderwidth=0, font=('Corbel', 18))
text_box.config(insertwidth=5, insertbackground=MAIN_C2, spacing1=5)
text_box.grid(row=1, column=0, columnspan=3, pady=20)
text_box.focus()
text_box.bind("<Key>", key_press)


window.mainloop()
