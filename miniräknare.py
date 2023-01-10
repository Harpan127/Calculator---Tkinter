from tkinter import *

window = Tk()
window.resizable(False, False)
window.title("Calculator")
icon = PhotoImage(file="calculator.png")
window.iconphoto(True, icon)

numbers = ""    # This variable is the user input. The program will evaluate this variable.

textvariable = StringVar()

# REMOVE LAST CHARACTER OF DISPLAY


def backspace():
    global numbers
    numbers = numbers[:-1]
    textvariable.set(numbers)


# CLEAR DISPLAY


def clear():
    global numbers
    numbers = ""
    textvariable.set(numbers)

# Adds input to display


def show_number(x):
    global numbers
    numbers = numbers + x
    textvariable.set(numbers)


# Evaluates input on display, except SyntaxError and ZeroDivisionError


def calculate():
    global numbers
    if numbers != "":
        try:
            answer = eval(numbers)
            textvariable.set(answer)
            numbers = str(answer)
        except SyntaxError:
            textvariable.set("SyntaxError")
            numbers = ""
        except ZeroDivisionError:
            textvariable.set("ZeroDivisionError")
            numbers = ""


# This Lable displays the numbers on the screen

widget = Label(window, textvariable=textvariable,
               fg='white', bg='black', font=(0, 15), foreground="lightgreen", width=20, height=2)
widget.grid(row=0, column=0, columnspan=4)

# Buttons on interface (numbers)

Button(window, text="1", font=(0, 10), command=lambda: show_number("1"), width=6, height=3).grid(row=1, column=0)
Button(window, text="2", font=(0, 10), command=lambda: show_number("2"), width=6, height=3).grid(row=1, column=1)
Button(window, text="3", font=(0, 10), command=lambda: show_number("3"), width=6, height=3).grid(row=1, column=2)
Button(window, text="4", font=(0, 10), command=lambda: show_number("4"), width=6, height=3).grid(row=2, column=0)
Button(window, text="5", font=(0, 10), command=lambda: show_number("5"), width=6, height=3).grid(row=2, column=1)
Button(window, text="6", font=(0, 10), command=lambda: show_number("6"), width=6, height=3).grid(row=2, column=2)
Button(window, text="7", font=(0, 10), command=lambda: show_number("7"), width=6, height=3).grid(row=3, column=0)
Button(window, text="8", font=(0, 10), command=lambda: show_number("8"), width=6, height=3).grid(row=3, column=1)
Button(window, text="9", font=(0, 10), command=lambda: show_number("9"), width=6, height=3).grid(row=3, column=2)
Button(window, text="0", font=(0, 10), command=lambda: show_number("0"), width=6, height=3).grid(row=4, column=0)

# Buttons on display (operators)

Button(window, text="=", font=(0, 10), command=calculate, width=6, height=3).grid(row=4, column=1)
Button(window, text="DEL", font=(0, 10), command=clear, width=6, height=3).grid(row=4, column=2)

Button(window, text="+", font=(0, 10), command=lambda: show_number("+"),
       width=6, height=3, bg="#FA980B").grid(row=1, column=3)
Button(window, text="-", font=(0, 10), command=lambda: show_number("-"),
       width=6, height=3, bg="#FA980B").grid(row=2, column=3)
Button(window, text="/", font=(0, 10), command=lambda: show_number("/"),
       width=6, height=3, bg="#FA980B").grid(row=3, column=3)
Button(window, text="*", font=(0, 10), command=lambda: show_number("*"),
       width=6, height=3, bg="#FA980B").grid(row=4, column=3)

# Keyboard bindings

window.bind("1", lambda press: show_number("1"))
window.bind("2", lambda press: show_number("2"))
window.bind("3", lambda press: show_number("3"))
window.bind("4", lambda press: show_number("4"))
window.bind("5", lambda press: show_number("5"))
window.bind("6", lambda press: show_number("6"))
window.bind("7", lambda press: show_number("7"))
window.bind("8", lambda press: show_number("8"))
window.bind("9", lambda press: show_number("9"))
window.bind("0", lambda press: show_number("0"))
window.bind("-", lambda press: show_number("-"))
window.bind("<.>", lambda press: show_number("."))
window.bind("<*>", lambda press: show_number("*"))
window.bind("<+>", lambda press: show_number("+"))
window.bind("</>", lambda press: show_number("/"))
window.bind("<%>", lambda press: show_number("%"))

window.bind("<Return>", lambda press: calculate())
window.bind("<c>", lambda press: clear())
window.bind("<BackSpace>", lambda press: backspace())

window.mainloop()
