from rest_framework import generics
from .models import NoteModel
from .serializers import NoteSerializer



class NoteList(generics.ListCreateAPIView):
    queryset = NoteModel.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NoteModel.objects.all()
    permission_classes = []
    serializer_class = NoteSerializer