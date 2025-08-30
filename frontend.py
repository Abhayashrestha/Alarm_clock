import os
import datetime
import pygame
import tkinter as tk
from tkinter import messagebox

# Path to the alarm sound relative to this file
SOUND_FILE = os.path.join(os.path.dirname(__file__), "alarm.wav")


def play_sound():
    """Play the alarm sound once."""
    pygame.mixer.init()
    pygame.mixer.music.load(SOUND_FILE)
    pygame.mixer.music.play()


def check_time():
    """Check the current time against the alarm time."""
    current = datetime.datetime.now().strftime("%H:%M:%S")
    if current == alarm_time.get():
        play_sound()
        messagebox.showinfo("Alarm", "Time is up!")
    else:
        root.after(1000, check_time)


def set_alarm():
    """Start checking the time for the alarm."""
    messagebox.showinfo("Alarm", f"Alarm set for {alarm_time.get()}")
    root.after(1000, check_time)


root = tk.Tk()
root.title("Alarm Clock")

# Entry for the alarm time
alarm_time = tk.StringVar()
label = tk.Label(root, text="Set alarm (HH:MM:SS):")
label.pack(padx=10, pady=5)
entry = tk.Entry(root, textvariable=alarm_time)
entry.pack(padx=10, pady=5)

# Button to set the alarm
button = tk.Button(root, text="Set Alarm", command=set_alarm)
button.pack(padx=10, pady=10)

root.mainloop()

