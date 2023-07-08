from rest_framework import serializers

class ChatCompletionSerializer(serializers.Serializer):
    model_prompt = serializers.CharField()
