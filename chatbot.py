import openai
import random

# Set your OpenAI API key
openai.api_key = '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'

# Define responses for the chatbot
GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "what's up", "hey"]
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting_response(text):
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def generate_response(user_input):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=user_input,
      temperature=0.7,
      max_tokens=100
    )
    return response.choices[0].text.strip()

# Lead Management
leads = []

def add_lead(name, email, phone):
    leads.append({"name": name, "email": email, "phone": phone})

print("Bot: Hello! How can I assist you today?")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Bot: Goodbye!")
        break
    elif user_input.lower() == 'show leads':
        print("Bot: Here are the leads:")
        for lead in leads:
            print(lead)
    else:
        if greeting_response(user_input) is not None:
            print("Bot:", greeting_response(user_input))
        else:
            response = generate_response(user_input)
            print("Bot:", response)
            # Example: If the user expresses interest, extract lead information
            if 'interested' in user_input.lower():
                print("Bot: Can you please provide your name, email, and phone number?")
                name = input("You: Name: ")
                email = input("You: Email: ")
                phone = input("You: Phone: ")
                add_lead(name, email, phone)
                print("Bot: Thank you! Your information has been added to our leads.")
