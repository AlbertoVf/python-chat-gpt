
from .question import getQuestion
from .ai import getResponse


def time():
    import datetime
    import re

    d = re.sub(r":|\.|-|\s", '_', str(datetime.datetime.now()), 0)
    return d


def saveResponse(indexQuestion: int = 1):
    index, question = getQuestion(indexQuestion)
    response = getResponse(question)

    with open(f'Chat/Question_{index}-{time()}.md', 'w') as f:
        f.write(f'# {question}\n')
        f.write(response)
