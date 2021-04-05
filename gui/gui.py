import tkinter as tk
import main
import json
from gui.text_entry import TextEntry

inputLanguage = 'en'
qId = -1


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

    def start(self):
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

    global qId
    qId += 1

    allAnswers = [gui.answer1.entry.get(), gui.answer2.entry.get(),
                  gui.answer3.entry.get()]
    main.addQuestion(qId, inputLanguage, gui.question.entry.get(),
                     allAnswers, gui.correctAnswer.entry.get())
    gui.clear()


def init():
    jsonData = json.load(open('output.json', encoding="utf-8"))

    lastIds = [jsonData['all_questions'][x][-1]['id']
               for x in jsonData['all_questions']]
    
    assert lastIds.count(lastIds[0]) == len(lastIds)

    global qId
    qId = lastIds[0]

    gui = GUI()
    gui.start()
