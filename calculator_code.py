import tkinter as tk

def click(a):
    global expression
    text = a.widget["text"]
    if text == "=":
        try:
            expression = str(eval(expression))
            screen_var.set(expression)
        except:
            screen_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        screen_var.set("")
    else:
        expression += text
        screen_var.set(expression)

# Initialize main window

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

expression = ""
screen_var = tk.StringVar()

# Display Screen

screen = tk.Entry(root, textvariable=screen_var, font="Helvetica 20", justify="right", bd=8, relief="ridge")
screen.pack(fill="both", ipadx=8, pady=10)

# Buttons

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

for i, button in enumerate(buttons):
    btn = tk.Button(button_frame, text=button, font="Helvetica 15", height=2, width=5)
    btn.grid(row=i//4, column=i%4, padx=5, pady=5)
    btn.bind("<Button-1>", click)


root.mainloop()
