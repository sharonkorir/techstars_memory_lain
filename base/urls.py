from django.urls import path
from .views import *

urlpatterns = [
    path('chat/', ChatCompletionView.as_view(), name='chat_completion'),
]