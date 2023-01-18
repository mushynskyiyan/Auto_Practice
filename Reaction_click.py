import tkinter as tk
import random
import time

window = tk.Tk()
fg_tones = ['red', 'green', 'blue']
window.geometry("400x300")


label = tk.Label(
    text="Reaction test",
    foreground="white",  # Set the text color to white
    background=random.choice(fg_tones),  # Set the background color to black
    width=100,
    height=2
)

entry = tk.Entry()

frame = tk.Frame(
    height=10
)


def send_message():
    var = entry.get()
    print(var)
    result_1.config(
        text=var
    )


button = tk.Button(
    text="Click me!",
    activebackground='blue',
    background="red",
    foreground="black",
    width=10,
    height=1,
    command=send_message
)

result = tk.Label(
    text="0.0",
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


def timer_update():
    value = f'Your time:'
    result.config(text=value)
    window.after(2000, timer_update)


window.after(2000, timer_update)

window.mainloop()
