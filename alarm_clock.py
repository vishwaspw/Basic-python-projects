import tkinter
import tkinter as Tk
import datetime
import time
from pygame import mixer
from tkinter import messagebox

# Initializing the mixer
mixer.init()

# Creating the window
root = tkinter.Tk()
root.title("Alarm Clock")
root.geometry("550x330")

# variable to manage value of the widget
alarmtime = tkinter.StringVar()
message = tkinter.StringVar()

# Label widget
head = tkinter.Label(root, text="Alarm Clock", font=('comic sans', 20))
head.grid(row=0, columnspan=3, pady=10)

# Alarm functionality
def alarm():
    a = alarmtime.get()
    alarm_t = a
    Current_Time = time.strftime("%H:%M")

    # Changing the Current time
    while alarm_t != Current_Time:
        Current_Time = time.strftime("%H:%M")
        time.sleep(1)

    # Play alarm sound
    if alarm_t == Current_Time:
        try:
            mixer.music.load("sound.wav")
            mixer.music.play()
        except:
            # If sound file is not found, use system beep
            import winsound
            winsound.Beep(1000, 1000)
        
        msg = messagebox.showinfo('Info', f'{message.get()}')
        if msg == 'ok':
            mixer.music.stop()

# To display clock Image
clockimg = tkinter.PhotoImage(file="img_61.png")

# Label widget for image
img = tkinter.Label(root, image=clockimg)
img.grid(rowspan=5, column=0)

# Label widget for time input
input_time = tkinter.Label(root, text="Input time (HH:MM)", font=('comic sans', 15))
input_time.grid(row=1, column=1)

# Entry widget
altime = tkinter.Entry(root, textvariable=alarmtime, font=('comic sans', 15), width=6)
altime.grid(row=1, column=2)

# Label widget for message
msg = tkinter.Label(root, text="Message", font=('comic sans', 15))
msg.grid(row=2, column=1, columnspan=2)

# Entry widget
msg_input = tkinter.Entry(root, textvariable=message, font=('comic sans', 15))
msg_input.grid(row=3, column=1, columnspan=2)

# Button widget
submit = tkinter.Button(root, text="Set Alarm", font=('comic sans', 15), command=alarm)
submit.grid(row=4, column=1, columnspan=2)

# Event loop
root.mainloop()