import tkinter as tk
import random
import time
import datetime
from tkinter import ACTIVE, DISABLED

tik = time.time()
window = tk.Tk()
fg_tones = ['red', 'green', 'blue']
window.geometry("450x300")


def generate_text():
    text = ["Reaction test starts in 3..2..1", "Click on the button when you see red"]
    for i in range(len(text)):
        return text[i]


label = tk.Label(
    text="Reaction test starts in 3..2..1",
    foreground="white",
    background='black',
    width=100,
    height=2
)

frame = tk.Frame(
    height=10
)


def timer():
    tok = time.time()
    times = tok - tik
    result_1.config(text=f'Reaction time is {times}')
    print(f'Reaction=')


button = tk.Button(
    text="Click me!",
    activebackground='blue',
    background="red",
    foreground="black",
    width=10,
    height=1,
    command=timer
)
result = tk.Label(
    text="Test your destiny!",
    foreground="white",  # Set the text color to white
    font=("Arial", 25)
)
frame_2 = tk.Frame(
    height=10
)

result_1 = tk.Label(
    foreground="white",  # Set the text color to white
    font=("Arial", 25)
)
for c in window.children:
    print(c)
    window.children[c].pack()


def task_red():
    label.configure(
        text="Click on the button when you see red",
        foreground="white",
        background='red',
        width=100,
        height=2
    )


def task_blue():
    label.configure(
        text="Click on the button when you see red",
        foreground="white",
        background='blue',
        width=100,
        height=2
    )


def task_green():
    label.configure(
        text="Click on the button when you see red",
        foreground="white",
        background='green',
        width=100,
        height=2
    )


def task_orange():
    label.configure(
        text="Click on the button when you see red",
        foreground="white",
        background='#ff6f3c',
        width=100,
        height=2
    )


taskos = [task_red, task_orange, task_green, task_blue]


def task2():
    # label.config(
    #     text="Click on the button when you see red",
    #     foreground="white",
    #     background=random.choice(fg_tones),
    #     width=100,
    #     height=2
    # )
    f = random.choice(taskos)
    f()
    if f == task_red:


    window.after(random.randint(2000, 4000), task2)


window.after(2000, task2)

window.mainloop()
# time.sleep(1)
# label = tk.Label(
#     text=generate_text(),
#     foreground="white",
#     background='black',
#     width=100,
#     height=2
# )
# label.pack()
# window.update()
