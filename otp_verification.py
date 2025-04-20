from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.geometry("600x550")
root.title("OTP Verification")

# Generate OTP
def generateOTP():
    n = random.randint(1000, 9999)
    messagebox.showinfo("OTP", f"Your OTP is: {n}")
    return n

# Check OTP
def checkOTP():
    if int(otp.get()) == n:
        messagebox.showinfo("Success", "OTP Verified Successfully!")
    else:
        messagebox.showerror("Error", "Invalid OTP!")

# Create canvas
canvas = Canvas(root, width=400, height=300)
canvas.pack()

# Create labels and entry
Label(root, text="OTP Verification", font=("Arial", 20)).place(x=210, y=50)
Label(root, text="Enter OTP:", font=("Arial", 12)).place(x=150, y=150)
otp = Entry(root, font=("Arial", 12))
otp.place(x=250, y=150)

# Create buttons
Button(root, text="Generate OTP", command=generateOTP, font=("Arial", 12)).place(x=200, y=200)
Button(root, text="Submit", command=checkOTP, font=("Arial", 12)).place(x=250, y=250)

# Generate initial OTP
n = generateOTP()

root.mainloop()