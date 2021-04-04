import json
from typing import List
from datetime import datetime
from question import *
import gui.gui as gui
import backup as backup

jsonData = json.load(open('output.json', encoding="utf-8"))
LANGUAGES: List[str] = jsonData['languages']

questions: List[Question] = []


def loadQuestionFromInput(inputLanguage):
    question = input("Question: ")
    answer1 = input("Answer 1: ")
    answer2 = input("Answer 2: ")
    answer3 = input("Answer 3: ")

    allAnswers = [answer1, answer2, answer3]

    correctAnswer = ""

    while correctAnswer not in allAnswers:
        correctAnswer = input("Correct Answer: ")
        if correctAnswer in allAnswers:
            break
        print("Correct Answer must be in allAnswers!")

    addQuestion(inputLanguage, question, allAnswers, correctAnswer)


def addQuestion(inputLanguage, question, allAnswers, correctAnswer, fromData=False):
    q = Question(inputLanguage, question, allAnswers, correctAnswer)
    print('adding: ' + q.question)

    for language in LANGUAGES:
        if (fromData and language != inputLanguage) or not fromData:
            translated = q.translateQuestion(language)
            questions.append(translated)


def save():
    data = jsonData
    """ data = {}
    data['all_questions'] = {} """

    for x in questions:
        if not x.language in data['all_questions'].keys():
            data['all_questions'][x.language] = []

        questionData = {
            "question": x.question,
            "all_answers": x.allAnswers,
            "correct_answer": x.correctAnswer
        }

        data['all_questions'][x.language].append(questionData)

    with open('output.json', 'w+', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)


def loadQuestionsFromData():
    for lan in jsonData['all_questions'].keys():
        for question in jsonData['all_questions'][lan]:

            addQuestion(
                lan, question['question'],
                question['all_answers'],
                question['correct_answer'],
                fromData=False
            )
    save()


def main():
    inputLanguage = input("Input Language: ")

    assert inputLanguage in LANGUAGES

    while True:
        loadQuestionFromInput(inputLanguage)

        if 'q' in input('Continue (any key) of quit(q): '):
            save()
            break


def start_gui():
    gui.init()


if __name__ == '__main__':
    backup.backup()
    start_gui()
