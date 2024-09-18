import os

from groq import Groq
def res(prompt):
    prompt = "Being a latest job market analyst, Please answer this query: " + prompt
    client = Groq(
        api_key=("key"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )

    return (chat_completion.choices[0].message.content)