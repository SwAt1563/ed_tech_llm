
from django.urls import path
from .views import ChatAPIView

app_name = 'llm'
urlpatterns = [
    path('chat/', ChatAPIView.as_view(), name='chat_with_openai'),
]
