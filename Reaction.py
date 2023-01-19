import tkinter as tk
import random
import time


window = tk.Tk()
window.geometry("550x300")

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

calls = 0


def counter(event):
    global calls
    calls+=1
    result.config(text=f'Wrong click counter {calls}')


phrases1 = ["You done with it!",
            "You think you can win this way?",
            "Reading this message \n makes you forget about test",
            "Це просто пекельні борошна...",
            'Sorry, you do wrong',
            'Please, pay more attention to test',
            "Are you kidding me?"]


def wrong_call():
    result_1.config(text=random.choice(phrases1))


button = tk.Button(
    text="Click me!",
    activebackground='blue',
    background="red",
    foreground="black",
    width=10,
    height=1,
    command=wrong_call
)
button.bind('<Button-1>', counter)
result = tk.Label(
    text=f'Wrong click count {calls}',
    foreground="white",
    font=("Arial", 25)
)
frame_2 = tk.Frame(
    height=10
)

result_1 = tk.Label(
    foreground="white",
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


def obnulyator():
    global calls
    calls = 0


def nothingner(event):
    pass


taskos = [task_red, task_orange, task_green, task_blue]


def task2():
    f = random.choice(taskos)
    f()
    if f == task_red:
        tik = time.time()


        def timer():
            tok = time.time()
            times = tok - tik
            result_1.config(text=f'Reaction time is {round(times, 2)} seconds')
            print(f'Reaction=')


        button.config(
            text="CLICK, quick!",
            activebackground='blue',
            background="red",
            foreground="black",
            width=10,
            height=1,
            command=timer)
        result.config(text=f'Test your destiny!')
        button.bind('<Button-1>', nothingner)
        obnulyator()
    else:
        button.config(
            text="Click me!",
            activebackground='blue',
            background="red",
            foreground="black",
            width=10,
            height=1,
            command=wrong_call)
        button.bind('<Button-1>', counter)
    window.after(random.randint(2000, 4000), task2)


window.after(2000, task2)

window.mainloop()

