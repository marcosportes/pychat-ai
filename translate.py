import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def read_file(file):
    with open(file, 'r', encoding='utf-8') as file:
        return file.read()

language_source = "english"
language_target = "portuguese"

def translate(text, language_source, language_target):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Translate the following complete text from {language_source} to {language_target}: {text}",
        temperature=1.0,
        max_tokens=2048,
        n=1,
        stop=None
    )
    return response['choices'][0]['text'].strip()

file = 'article-example.txt'
text = read_file(file)
print(translate(text, language_source, language_target))