
from src.response import saveResponse
from src.question import readQuestions

if __name__ == '__main__':
    for i in range(1, len(readQuestions())+1):
        saveResponse(i)
