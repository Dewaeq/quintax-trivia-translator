import tkinter as tk
import main


class TextEntry():
    def __init__(self, text: str):
        self.label = tk.Label(text=text)
        self.label.pack()

        self.entry = tk.Entry(width=50)
        self.entry.pack()


class GUI():

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("700x500")

        self.label = tk.Label(text="Quintax Trivia Question Handler")
        self.label.pack()

        self.question = TextEntry("Question")
        self.answer1 = TextEntry("Answer1")
        self.answer2 = TextEntry("Answer2")
        self.answer3 = TextEntry("Answer3")
        self.correctAnswer = TextEntry("Correct Answer")

        self.submit = tk.Button(text="Add", command=lambda: submit(self))
        self.submit.pack()

        self.save = tk.Button(text="Save", command=lambda: save())
        self.save.pack()

        self.window.mainloop()
        
    def clear(self):
        self.question.entry.delete(0, tk.END)
        self.answer1.entry.delete(0, tk.END)
        self.answer2.entry.delete(0, tk.END)
        self.answer3.entry.delete(0, tk.END)
        self.correctAnswer.entry.delete(0, tk.END)


def save():
    main.save()


def submit(gui: GUI):
    allAnswers = [gui.answer1.entry.get(), gui.answer2.entry.get(),
                  gui.answer3.entry.get()]
    main.addQuestion('en', gui.question.entry.get(),
                     allAnswers, gui.correctAnswer.entry.get())
    gui.clear()


gui = GUI()
