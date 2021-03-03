from tkinter import *
from tkinter import messagebox, Tk, Button, Label, DoubleVar, Entry


win = Tk()
win.geometry("210x350")
win.maxsize(210, 350)
win.minsize(210, 350)
win.title("My App")
#
# b0 = Button(win, text="0",  padx=5, pady=5, activeforeground="blue", background="yellow"
# b0.grid(row=10, column=10)

def pr_eq():
    print("=")

eq_Button = Button(win, text="=", command=pr_eq, padx=5, pady=5, bg="darkgrey", fg="white",width=8, relief=RAISED, bd=10)
eq_Button.grid(column=0,row=0, padx=30, pady=15)
eq_Button.place(x=55, y=225)

eq_value = DoubleVar()
eq_entry = Entry(win,textvariable=eq_value, relief=RAISED, bd=5)
eq_entry.grid(column=0,row=0, padx=40, pady=15, )
eq_entry.delete(0,'end')

def pr1():
    print("1")
def pr2():
    print("2")
def pr3():
    print("3")
def pr4():
    print("4")
def pr5():
    print("5")
def pr6():
    print("6")
def pr7():
    print("7")
def pr8():
    print("8")
def pr9():
    print("9")
def pr0():
    print("0")




b1 = Button(win, text="1", command=pr1, padx=5, pady=5, activeforeground="blue", background="yellow", relief=GROOVE, bd=10)
b1.grid(row=10, column=10)
b1.place(x=5, y=60)


b2 = Button(win, text="2", command=pr2, padx=5, pady=5, activeforeground="blue", background="yellow", relief=GROOVE,
            bd=10)
b2.grid(row=10, column=10)
b2.place(x=55, y=60)


b3 = Button(win, text="3", command=pr3, padx=5, pady=5, activeforeground="blue", background="yellow", relief=RAISED,
            bd=10)
b3.grid(row=10, column=10)
b3.place(x=105, y=60)


b4 = Button(win, text="4", command=pr4, padx=5, pady=5, activeforeground="blue", background="yellow", relief=GROOVE,
            bd=10)
b4.grid(row=10, column=10)
b4.place(x=5, y=115)


b5 = Button(win, text="5", command=pr5, padx=5, pady=5, activeforeground="blue", background="yellow", relief=RAISED,
            bd=10)
b5.grid(row=10, column=10)
b5.place(x=55, y=115)

b6 = Button(win, text="6", command=pr6, padx=5, pady=5, activeforeground="blue", background="yellow", relief=RAISED,
            bd=10)
b6.grid(row=10, column=10)
b6.place(x=105, y=115)

b7 = Button(win, text="7", command=pr7, padx=5, pady=5, activeforeground="blue", background="yellow", relief=RAISED,
            bd=10)
b7.grid(row=10, column=10)
b7.place(x=5, y=170)

b8 = Button(win, text="8", command=pr8, padx=5, pady=5, activeforeground="blue", background="yellow", relief=RAISED,
            bd=10)
b8.grid(row=10, column=10)
b8.place(x=55, y=170)

b9 = Button(win, text="9", command=pr9, padx=5, pady=5, activeforeground="blue", background="yellow", relief=RAISED,
            bd=10)
b9.grid(row=10, column=10)
b9.place(x=105, y=170)

b0 = Button(win, text="0", command=pr0, padx=5, pady=5, activeforeground="blue", background="yellow", relief=RAISED,
            bd=10)
b0.grid(row=10, column=10)
b0.place(x=5, y=225)




def pradd(x, y):
    print("+")
    return x + y

def prsub(x, y):
    print("-")
    return x - y

def prmul(x, y):
    print("x")
    return x * y

def prdiv(x, y):
    print("/")
    return x / y



add = Button(win, text="+", command=pradd, padx=5, pady=5, activeforeground="blue", background="lightgrey", relief=RAISED,
            bd=10)
add.grid(row=10, column=10)
add.place(x=160, y=60)

sub = Button(win, text="-", command=prsub, padx=5, pady=5, activeforeground="blue", background="lightgrey", relief=RAISED,
            bd=10)
sub.grid(row=10, column=10)
sub.place(x=160, y=115)

mul = Button(win, text="X", command=prmul, padx=5, pady=5, activeforeground="blue", background="lightgrey", relief=RAISED,
            bd=10)
mul.grid(row=10, column=10)
mul.place(x=160, y=170)

div = Button(win, text="/", command=prdiv, padx=5, pady=5, activeforeground="blue", background="lightgrey", relief=RAISED,
            bd=10)
div.grid(row=10, column=10)
div.place(x=160, y=225)


# def h_b_click():
#     messagebox.showinfo("From System","VIRUS DETECTED! Your Computer has been HACKED")
#
# b_click = Button(win,text="CLICK HERE to Start",command=h_b_click)
#
# b_click.pack()


print("Select operation.")

while True:
    # Take input from the user
    choice = input("Enter choice('+'or '-' or 'x' or '/'): ")

    if choice in ('+', '-', '*', '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            print(num1, "+", num2, "=", pradd(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", prsub(num1, num2))

        elif choice == '*':
            print(num1, "x", num2, "=", prmul(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", prdiv(num1, num2))
        break
    else:
        print("Invalid Input")

win.mainloop()
