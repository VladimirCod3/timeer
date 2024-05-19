import tkinter as tk
from tkinter import messagebox
import time
from threading import Thread

def pomodoro_timer(work_time=25, short_break=5, long_break=15, cycles=4):
    for cycle in range(cycles):
        set_timer(work_time * 60, f"Работа: Цикл {cycle + 1}. Сосредоточьтесь!")
        set_timer(long_break * 60 if cycle == cycles - 1 else short_break * 60, "Перерыв. Время чилануть")
    messagebox.showinfo("Завершено", "Таймер закончил работу!")

def set_timer(seconds, message):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = "{:02d}:{:02d}".format(mins, secs)
        label.config(text=time_format)
        message_label:(text==message) # type: ignore
        root.update_idletasks()
        time.sleep(1)
        seconds -= 1

def start_thread():
    if not getattr(start_thread, "running", False):
        start_thread.running = True
        t = Thread(target=pomodoro_timer)
        t.start()

root = tk.Tk()
root.title("Таймер Помидор")
window_width = 450
window_height = 150
root.geometry(f"{window_width}x{window_height}")

canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack(fill="both", expand=True)
root.update_idletasks()


label = tk.Label(root, text="00:00", font=("Helvetica", 48), bg="white", fg="black")
label.place(relx=0.5, rely=0.3, anchor="center")

start_button = tk.Button(root, text="Старт", command=start_thread)
start_button.place(relx=0.5, rely=0.7, anchor="center")
root.mainloop()

start_thread.running = False


