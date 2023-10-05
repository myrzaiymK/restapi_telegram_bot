from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import User, Message
from .serializers import UserSerializer, UserLoginSerializer, MessageSerializer, MessageListSerializer, TokenSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import login


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserLoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=self.request.data, context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)



class MessageCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = MessageSerializer(data=self.request.data, context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_201_CREATED)


class MessageList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageListSerializer(messages, many=True)
        return Response(serializer.data)



class TokenGenerate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer_class = TokenSerializer(data=self.request.data, context={'request': self.request})
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        return Response(serializer_class.data, status=status.HTTP_201_CREATED)


