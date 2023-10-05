# api/urls.py
from django.urls import path
from .views import UserCreateView, UserLoginView, MessageCreateView, MessageList
# from telegram_bot_project.telegram_bot import send_welcome

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('send_message/', MessageCreateView.as_view(), name='send_message'),
    path('message_list/', MessageList.as_view(), name='message_list')

]
