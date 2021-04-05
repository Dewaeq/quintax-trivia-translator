from ctypes import string_at
from textblob import TextBlob
from textblob.exceptions import NotTranslated
from typing import List

class Question:
    def __init__(self, id: int, language: str, question: str, allAnswers: List[str], correctAnswer: string_at):
        self.id = id
        self.language = language
        self.question = question
        self.allAnswers = allAnswers
        self.correctAnswer = correctAnswer

    def translateQuestion(self, toLanguage):
        if toLanguage == self.language:
            return self
                
        newQuestion = translateString(self.question, toLanguage)
        newAnswers = []
        
        for answer in self.allAnswers:
            newAnswer = translateString(answer, toLanguage)
            newAnswers.append(newAnswer)
        newCorrectAnswer = translateString(self.correctAnswer, toLanguage)

        assert newCorrectAnswer in newAnswers

        return Question(self.id, toLanguage, newQuestion, newAnswers, newCorrectAnswer)


def translateString(text, toLanguage):
    b = TextBlob(text)
    try: 
        b = b.translate(to=toLanguage)
    except:
        pass
    return b.string

