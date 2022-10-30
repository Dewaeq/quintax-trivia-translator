import tkinter as tk
import tkinter.font as tkFont
import main
import json
from gui.text_entry import TextEntry

inputLanguage = 'en'
qId = -1


class GUI():

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("700x500")

        self.label = tk.Label(
            text="Quintax Trivia Question Handler", font=tkFont.Font(size=16))
        self.label.pack()

        self.question = TextEntry("Question")
        self.answer1 = TextEntry("Answer1")
        self.answer2 = TextEntry("Answer2")
        self.answer3 = TextEntry("Answer3")
        self.correctAnswer = TextEntry("Correct Answer")

        self.submit = tk.Button(text="Add", font=tkFont.Font(
            size=16), bg='#6FCF97', fg='#FFFFFF', width=70, command=lambda: submit(self))
        self.submit.pack(pady=(400, 10), padx=20)

        self.save = tk.Button(text="Save", font=tkFont.Font(
            size=16), bg='#56CCF2', fg='#FFFFFF', width=70, command=lambda: save())
        self.save.pack(pady=(0, 10), padx=20)

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
