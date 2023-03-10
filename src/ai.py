import openai
from os import getenv
from dotenv import load_dotenv

load_dotenv('.env')


def getResponse(question: str) -> str:
    openai.api_key = getenv('API_KEY')
    print(f'[pensando]: {question}')
    response = openai.Completion.create(
        engine=getenv('ENGINE'),
        prompt=question, n=1,
        max_tokens=int(getenv('MAX_TOKENS'))
    )

    response_content = response.choices[0].text

    return response_content
