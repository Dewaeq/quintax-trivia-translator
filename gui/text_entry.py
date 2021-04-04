import tkinter as tk

class TextEntry():
    def __init__(self, text: str):
        self.label = tk.Label(text=text)
        self.label.pack()

        self.entry = tk.Entry(width=50)
        self.entry.pack()