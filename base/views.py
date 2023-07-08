from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import openai
from django.conf import settings
from .serializers import *

class ChatCompletionView(APIView):
    def post(self, request, format=None):
        # Set up your OpenAI API credentials
        openai.api_key = settings.CHAT_API

        # Define the initial message and conversation
        initial_message = {
            'role': 'system',
            'content': 'You are a helpful assistant that prompts users to tell stories.'
        }
        conversation = [initial_message]

        # Get user message from the request data
        user_message = {
            'role': 'user',
            'content': request.data.get('content')  # Assuming 'content' is the key for the user message
        }
        conversation.append(user_message)

        # Send the API request
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=conversation,
            max_tokens=50  # Set an appropriate value for the response length
        )

        # Extract the model-generated prompt
        model_prompt = response['choices'][0]['message']['content']

        # Serialize the response
        serializer = ChatCompletionSerializer(data={'model_prompt': model_prompt})
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)
