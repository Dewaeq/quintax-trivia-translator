import tkinter as tk
import tkinter.font as tkFont

class TextEntry():
    def __init__(self, text: str):
        self.label = tk.Label(text=text, font=tkFont.Font(size=13))
        self.label.pack()

        self.entry = tk.Entry(font=tkFont.Font(size=14),width=150)
        self.entry.pack(pady=15, ipady=7)