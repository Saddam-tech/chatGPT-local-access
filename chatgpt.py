import openai
import os

# Set your API key

openai.api_key = "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"

# Define your prompt
while True:

    prompt = input("Type your question: ")

    if prompt:

        if prompt.lower() == "stop":
            break
        # Call the OpenAI API to generate a response
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}])
        print(completion.choices[0].message.content)

