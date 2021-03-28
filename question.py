from textblob import TextBlob

class Question:
    def __init__(self, language, question, allAnswers, correctAnswer):
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

        return Question(toLanguage, newQuestion, newAnswers, newCorrectAnswer)


def translateString(text, toLanguage):
    b = TextBlob(text)
    return b.translate(to=toLanguage).string

