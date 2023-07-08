import openai
from django.conf import settings

# Set up your OpenAI API credentials
openai.api_key = settings.CHAT_API

# Define the initial message and conversation
initial_message = {
    'role': 'system',
    'content': 'You are a helpful assistant that prompts users to tell stories.'
}
conversation = [initial_message]

# Define the user message
user_message = {
    'role': 'user',
    'content': 'Once upon a time, there was a brave knight.'
}
conversation.append(user_message)

# Send the API request
response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=conversation,
    max_tokens=50  # Set an appropriate value for the response length
)

# Extract and print the model-generated question
model_prompt = response['choices'][0]['message']['content']
print('Model Prompt:', model_prompt)
