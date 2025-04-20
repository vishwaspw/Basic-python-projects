# Importing the library
import tkinter
from tkinter import messagebox

# Global variables
global label_q1, label1, op1, op2, op3, op4
global label_q2, label2, opp1, opp2, opp3, opp4
global label_q3, label3, oppp1, oppp2, oppp3, oppp4
global label_q4, label4, opppp1, opppp2, opppp3, opppp4
global label_q5, label5, oppppp1, oppppp2, oppppp3, oppppp4
global label_q6, label6, opppppp1, opppppp2, opppppp3, opppppp4
global label_t, label_u, entry, button, c, username

# Function to increase the point
def increase():
    global c
    c += 1

# Function to show final score
def show_score():
    global username
    messagebox.showinfo("Quiz Completed!", f"Congratulations {username}!\nYour final score is: {c}/6")

# Question 6
def info6():
    global label_q6, label6, opppppp1, opppppp2, opppppp3, opppppp4
    global label_q5, label5, oppppp1, oppppp2, oppppp3, oppppp4
    label_q6 = tkinter.Label(root, text="Question 6", font=("Arial", 35))
    label_q6.place(x=550, y=50)
    label6 = tkinter.Label(root, text="Which of these is used to define a block of code in Python?", font=("Arial", 30))
    label6.place(x=200, y=100)

    # Button widgets for options
    opppppp1 = tkinter.Button(root, text="Curly braces", font=("Arial", 20), command=show_score)
    opppppp1.place(x=400, y=200)
    opppppp2 = tkinter.Button(root, text="Indentation", font=("Arial", 20), command=lambda: [increase(), show_score()])
    opppppp2.place(x=800, y=200)
    opppppp3 = tkinter.Button(root, text="Parentheses", font=("Arial", 20), command=show_score)
    opppppp3.place(x=400, y=300)
    opppppp4 = tkinter.Button(root, text="Square brackets", font=("Arial", 20), command=show_score)
    opppppp4.place(x=800, y=300)
    
    if 'oppppp1' in globals():
        oppppp1.destroy()
        oppppp2.destroy()
        oppppp3.destroy()
        oppppp4.destroy()
        label_q5.destroy()
        label5.destroy()

# Question 5
def info5():
    global label_q5, label5, oppppp1, oppppp2, oppppp3, oppppp4
    global label_q4, label4, opppp1, opppp2, opppp3, opppp4
    label_q5 = tkinter.Label(root, text="Question 5", font=("Arial", 35))
    label_q5.place(x=550, y=50)
    label5 = tkinter.Label(root, text="What is the output of print(2 ** 3)?", font=("Arial", 30))
    label5.place(x=300, y=100)

    # Button widgets for options
    oppppp1 = tkinter.Button(root, text="6", font=("Arial", 20), command=info6)
    oppppp1.place(x=400, y=200)
    oppppp2 = tkinter.Button(root, text="8", font=("Arial", 20), command=lambda: [increase(), info6()])
    oppppp2.place(x=800, y=200)
    oppppp3 = tkinter.Button(root, text="5", font=("Arial", 20), command=info6)
    oppppp3.place(x=400, y=300)
    oppppp4 = tkinter.Button(root, text="Error", font=("Arial", 20), command=info6)
    oppppp4.place(x=800, y=300)
    
    if 'opppp1' in globals():
        opppp1.destroy()
        opppp2.destroy()
        opppp3.destroy()
        opppp4.destroy()
        label_q4.destroy()
        label4.destroy()

# Question 4
def info4():
    global label_q4, label4, opppp1, opppp2, opppp3, opppp4
    global label_q3, label3, oppp1, oppp2, oppp3, oppp4
    label_q4 = tkinter.Label(root, text="Question 4", font=("Arial", 35))
    label_q4.place(x=550, y=50)
    label4 = tkinter.Label(root, text="Which of these is not a Python data type?", font=("Arial", 30))
    label4.place(x=300, y=100)

    # Button widgets for options
    opppp1 = tkinter.Button(root, text="int", font=("Arial", 20), command=info5)
    opppp1.place(x=400, y=200)
    opppp2 = tkinter.Button(root, text="float", font=("Arial", 20), command=info5)
    opppp2.place(x=800, y=200)
    opppp3 = tkinter.Button(root, text="char", font=("Arial", 20), command=lambda: [increase(), info5()])
    opppp3.place(x=400, y=300)
    opppp4 = tkinter.Button(root, text="str", font=("Arial", 20), command=info5)
    opppp4.place(x=800, y=300)
    
    if 'oppp1' in globals():
        oppp1.destroy()
        oppp2.destroy()
        oppp3.destroy()
        oppp4.destroy()
        label_q3.destroy()
        label3.destroy()

# Question 3
def info3():
    global label_q3, label3, oppp1, oppp2, oppp3, oppp4
    global label_q2, label2, opp1, opp2, opp3, opp4
    label_q3 = tkinter.Label(root, text="Question 3", font=("Arial", 35))
    label_q3.place(x=550, y=50)
    label3 = tkinter.Label(root, text="Which of the following is not the core datatype in Python?",
                           font=("Arial", 30))
    label3.place(x=200, y=100)

    # Button widgets for options
    oppp1 = tkinter.Button(root, text="Tuple", font=("Arial", 20), width=8, command=info4)
    oppp1.place(x=400, y=200)
    oppp2 = tkinter.Button(root, text="Dictionary", font=("Arial", 20), width=7, command=info4)
    oppp2.place(x=800, y=200)
    oppp3 = tkinter.Button(root, text="Lists", font=("Arial", 20), width=7, command=info4)
    oppp3.place(x=400, y=300)
    oppp4 = tkinter.Button(root, text="Class", font=("Arial", 20), command=lambda: [increase(), info4()])
    oppp4.place(x=800, y=300)
    
    if 'opp1' in globals():
        opp1.destroy()
        opp2.destroy()
        opp3.destroy()
        opp4.destroy()
        label_q2.destroy()
        label2.destroy()

# Question 2
def info2():
    global label_q2, label2, opp1, opp2, opp3, opp4
    global label_q1, label1, op1, op2, op3, op4
    label_q2 = tkinter.Label(root, text="Question 2", font=("Arial", 35))
    label_q2.place(x=550, y=50)
    label2 = tkinter.Label(root, text="Which of the following is built-in function in Python?", font=("Arial", 30))
    label2.place(x=300, y=100)

    # Button widget for options
    opp1 = tkinter.Button(root, text="factorial()", font=("Arial", 20), command=info3)
    opp1.place(x=400, y=200)
    opp2 = tkinter.Button(root, text="print()", font=("Arial", 20), command=lambda: [increase(), info3()])
    opp2.place(x=800, y=200)
    opp3 = tkinter.Button(root, text="seed()", font=("Arial", 20), command=info3)
    opp3.place(x=400, y=300)
    opp4 = tkinter.Button(root, text="sqrt()", font=("Arial", 20), command=info3)
    opp4.place(x=800, y=300)
    
    if 'op1' in globals():
        op1.destroy()
        op2.destroy()
        op3.destroy()
        op4.destroy()
        label_q1.destroy()
        label1.destroy()

# Question 1
def info1():
    global label_q1, label1, op1, op2, op3, op4
    global label_t, label_u, entry, button, username
    username = entry.get()
    label_q1 = tkinter.Label(root, text="Question 1", font=("Arial", 35))
    label_q1.place(x=550, y=50)
    label1 = tkinter.Label(root, text="Which of them is a Keyword in Python?", font=("Arial", 30))
    label1.place(x=300, y=100)

    # Button widget for options
    op1 = tkinter.Button(root, text="range", font=("Arial", 20), command=info2)
    op1.place(x=400, y=200)
    op2 = tkinter.Button(root, text="def", font=("Arial", 20), command=lambda: [increase(), info2()])
    op2.place(x=800, y=200)
    op3 = tkinter.Button(root, text="Val", font=("Arial", 20), command=info2)
    op3.place(x=400, y=300)
    op4 = tkinter.Button(root, text="to", font=("Arial", 20), command=info2)
    op4.place(x=800, y=300)

    label_t.destroy()
    label_u.destroy()
    entry.destroy()
    button.destroy()

# Window
root = tkinter.Tk()
root.title("QUIZ")
root.geometry('700x900')
c = 0
username = ""
label_t = tkinter.Label(root, text="QUIZ", font=("arial", 50))
label_t.place(x=600, y=50)

# Label widget for user
label_u = tkinter.Label(root, text="Username", font=("arial", 30))
label_u.place(x=250, y=250)

# Entry widget
entry = tkinter.Entry(root, font=("arial", 30))
entry.place(x=500, y=250)

# Button widget
button = tkinter.Button(root, text="Start Quiz", font=("Arial", 20), command=info1)
button.place(x=600, y=350)

# Event loop
root.mainloop()