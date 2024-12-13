from tkinter import ttk
import tkinter as tk

from tkinter import messagebox
import pyttsx3 



engine = pyttsx3.init()

def play_text():
    text = text_entry.get()
    if text.strip():
        engine.say(text)
        newVoiceRate = 300
        engine.setProperty('rate',newVoiceRate)
        engine.runAndWait()
    else:
        messagebox.showwarning("تحذير", "الرجاء إدخال نص لتشغيله!")

def set_text():
    text_entry.delete(0, tk.END)

def exit_app():
    root.destroy()


root = tk.Tk()
root.title("Text to Speech")


label = tk.Label(root, text="Enter text:", font=("Arial", 14))
label.pack(pady=10)

text_entry = tk.Entry(root, font=("Arial", 14), width=30)
text_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

play_button = tk.Button(button_frame, text="Play", font=("Arial", 12), bg="lightgreen", command=play_text)
play_button.grid(row=0, column=0, padx=10)

set_button = tk.Button(button_frame, text="Set", font=("Arial", 12), bg="lightblue", command=set_text)
set_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(button_frame, text="Exit", font=("Arial", 12), bg="lightcoral", command=exit_app)
exit_button.grid(row=0, column=2, padx=10)


root.mainloop()