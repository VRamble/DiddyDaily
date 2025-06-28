from openai import OpenAI

client=OpenAI()

response=client.responses.create(
    model="gpt-4.1",
    input='''This is a test of getting a response from gpt from a python script. I am testing the open ai api. Limit your reponses to four sentences.'''
)

print(response.output_text)