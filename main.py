import json
from typing import List
from question import *
import gui.gui as gui
import backup as backup

jsonData = json.load(open('output.json', encoding="utf-8"))
LANGUAGES: List[str] = jsonData['languages']

questions: List[Question] = []


def loadQuestionFromInput(qId, inputLanguage):
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

    addQuestion(qId, inputLanguage, question, allAnswers, correctAnswer)


def addQuestion(qId, inputLanguage, question, allAnswers: List[str], correctAnswer, fromData=False):
    q = Question(qId, inputLanguage, question, allAnswers, correctAnswer)
    print('adding: ' + q.question)

    assert len([x for x in allAnswers if x != None and x != '']) == 3
    assert correctAnswer in allAnswers

    for language in LANGUAGES:
        if (fromData and language != inputLanguage) or not fromData:
            translated = q.translateQuestion(language)
            questions.append(translated)


def save():
    if not questions:
        return

    override = False
    for lang in LANGUAGES:
        if len([x for x in questions if x.language == lang]) != len(jsonData['all_questions'][lang]):
            override = True
            break

    if not override:
        return

    data = jsonData

    for x in questions:
        if x.language not in data['all_questions'].keys():
            data['all_questions'][x.language] = []

        questionData = {
            "question": x.question,
            "all_answers": x.allAnswers,
            "correct_answer": x.correctAnswer,
            "id": x.id
        }

        data['all_questions'][x.language].append(questionData)

    with open('output.json', 'w+', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)


def loadQuestionsFromData():
    for lan in jsonData['all_questions'].keys():
        for question in jsonData['all_questions'][lan]:

            addQuestion(
                question['id'],
                lan, question['question'],
                question['all_answers'],
                question['correct_answer'],
                fromData=False
            )
    save()


if __name__ == '__main__':
    backup.backup()
    gui.init()
