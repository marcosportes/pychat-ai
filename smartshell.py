import openai
import subprocess
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def smartshell(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Write a shell command that does the following: {text}",
        temperature=0.9,
        max_tokens=2048,
        n=1,
        stop=None
    )
    return response['choices'][0]['text'].strip()

def execute_shell_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True)
        print(result)
    except subprocess.CalledProcessError as e:
        print(e)

command_description = input("Enter a description for the shell command: ")
command = smartshell(command_description)
print(f"Genereted command: {command}")
execute_shell_command(command)