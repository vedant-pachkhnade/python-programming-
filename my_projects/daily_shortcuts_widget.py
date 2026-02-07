import tkinter as tk
import time
import os

# ---------- DELAY ----------
time.sleep(15)   # seconds after startup

# ---------- SHORTCUT LIST ----------
shortcuts = [
    "Ctrl + Shift + Esc → Task Manager",
    "Alt + Tab → Switch Apps",
    "Win + E → File Explorer",
    "Win + L → Lock PC",
    "Ctrl + Shift + T → Reopen Closed Tab",
    "Win + Shift + S → Screenshot",
    "Alt + F4 → Close App"
]

# ---------- STORE LAST INDEX ----------
data_file = os.path.join(os.path.expanduser("~"), "shortcut_index.txt")

if os.path.exists(data_file):
    with open(data_file, "r") as f:
        index = int(f.read().strip())
else:
    index = 0

shortcut = shortcuts[index % len(shortcuts)]

with open(data_file, "w") as f:
    f.write(str(index + 1))

# ---------- WIDGET ----------
root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)

screen_width = root.winfo_screenwidth()
x = screen_width - 340
y = 60
root.geometry(f"320x90+{x}+{y}")

frame = tk.Frame(root, bg="#1e1e1e", bd=2)
frame.pack(fill="both", expand=True)

title = tk.Label(
    frame,
    text="⌨ Shortcut Tip",
    bg="#1e1e1e",
    fg="white",
    font=("Segoe UI", 11, "bold")
)
title.pack(pady=(10, 4))

label = tk.Label(
    frame,
    text=shortcut,
    bg="#1e1e1e",
    fg="#dcdcdc",
    font=("Segoe UI", 10),
    wraplength=280,
    justify="center"
)
label.pack(pady=(0, 10))

# ---------- AUTO CLOSE ----------
root.after(10000, root.destroy)
root.mainloop()
