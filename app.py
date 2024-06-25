import streamlit as st
import openai
from openai import OpenAI
# Define the list of questions
questions = [
    "What is the name of your business?",
    "What do you sell or what service do you provide?",
    "What is your business's main goal?",
    "What are the important beliefs or principles of your business?",
    "How did you come up with the idea for your business?",
    "Who do you want to sell to?",
    "How does your product or service help your customers?",
    "Who else is selling similar products or services?",
    "What makes your product or service special compared to others?",
    "What’s currently popular or changing in your business area?",
    "How will you let people know about your product or service?",
    "What ways will you use to promote your business (like social media, emails, online ads)?",
    "How will you attract your first customers?",
    "How will you make sure customers come back?",
    "Where will your business be located?",
    "What are the main activities you need to do to make your product or deliver your service?",
    "Who will you need to work with to get supplies or help for your business?",
    "What tools or technology do you need for your business?",
    "How are you funding your business right now?",
    "What are your guesses about how much money you'll make and spend?",
    "How much money do you expect to make in the next 1-3 years?",
    "What will be your major costs?",
    "How much do you need to sell to cover your costs?",
    "What do you hope to achieve in the next year?",
    "What are your big plans for the next 3-5 years?",
    "How will you know if you are successful?",
    "What are the biggest problems you might face?",
    "How will you deal with these problems?",
    "Are there any rules or laws you need to follow for your business?",
    "How will you make sure you are following these rules?"
]

# Function to send data to GPT API and receive a response
def send_to_gpt(text):
    client = OpenAI(api_key='')
    prompt = "Using the gathered information, please generate a Comprehensive Business Strategy and Business Model Canvas for a fictional company."
    messages=[
              {"role": "system", "content": "You are a helpful assistant."},
              {"role": "user", "content": f"{text}\n{prompt}"}]

    response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-3.5-turbo-1106" depending on availability
            messages=messages,
            temperature=0
        )
    response_message = response.choices[0].message.content
    return response_message

# Collect answers from the user
answers = {}
for question in questions:
    answer = st.text_input(label=question, key=question)
    answers[question] = answer

# Display a submit button
if st.button('Submit Answers'):
    # Format the answers for the GPT API
    formatted_text = "\n".join([f"{q}: {a}" for q, a in answers.items() if a])  # Filter out empty answers
    # Send the formatted text to the GPT API
    result = send_to_gpt(formatted_text)
    # Display the result
    st.write(result)