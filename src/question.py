
def readQuestions() -> dict:
    import json
    questions = json.load(open('questions.json', 'r'))
    return questions


def getQuestion(index: int = 1) -> str:
    question = readQuestions().get(str(index))
    return index, question
