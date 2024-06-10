from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Clipboard, ClipboardItem
from .serializers import ClipboardSerializer, ClipboardItemSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ClipboardViewSet(ModelViewSet): 
    permission_classes = [IsAuthenticated]
    serializer_class = ClipboardSerializer

    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
    def get_queryset(self):
        return Clipboard.objects.filter(user_id=self.request.user.id)
    
class ClipboardItemViewSet(ModelViewSet):
    serializer_class = ClipboardItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ClipboardItem.objects.filter(clipboard_id=self.kwargs['clipboard_pk'])
    
    def get_serializer_context(self):
        return {'clipboard_id': self.kwargs['clipboard_pk']}
    

