import tkinter as tk
import random
import time


window = tk.Tk()
window.geometry("550x300")
#setting label
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

#setting counter funtion to count wrong function calls
def counter(event):
    global calls
    calls+=1
    result.config(text=f'Wrong click counter {calls}')

#just phrases to make user smile
phrases1 = ["You done with it!",
            "You think you can win this way?",
            "Reading this message \n makes you forget about test",
            "Це просто пекельні борошна...",
            'Sorry, you do wrong',
            'Please, pay more attention to test',
            "Are you kidding me?"]

#phrase generator func
def wrong_call():
    result_1.config(text=random.choice(phrases1))

#configuring button
button = tk.Button(
    text="Click me!",
    activebackground='blue',
    background="red",
    foreground="black",
    width=10,
    height=1,
    command=wrong_call
)
# binding left click on button on counter function to count wrong calls
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

#configuring label colors hard way
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

#function to set calls=0 when red callor already shown
def obnulyator():
    global calls
    calls = 0

#function to bind left mouse click to nothing during label color is red
def nothingner(event):
    pass

#list of tasks - colors
taskos = [task_red, task_orange, task_green, task_blue]

#task that will be called in endless cycle
def task2():
    f = random.choice(taskos)
    f()
    if f == task_red: #when color of label is red - needed parameters are set
        tik = time.time()


        def timer(): #timer function
            tok = time.time()
            times = tok - tik
            result_1.config(text=f'Reaction time is {round(times, 2)} seconds')
            print(f'Reaction=')

#button config that calls timer function
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

#first call of function to start chellenge
window.after(2000, task2)

window.mainloop()

