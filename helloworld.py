from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful SQL expert and DB administrator."},
        {
            "role": "user",
            "content": "given a sql table of 3 fields, name, date, weight, write a sql query to find out the maximum daily weight change of any person. Please only give the sql in one string. Please don't explain."
        }
    ]
)
#print(completion)
#print(completion.choices[0])
print(completion.choices[0].message.content)
