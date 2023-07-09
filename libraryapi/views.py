from rest_framework.response import Response
from rest_framework import generics, status
from django.db.models import Q

from .serializers import BookSerializer
from main.models import Book

# Create your views here.
class FindBook(generics.GenericAPIView):
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        key = request.query_params.get('key')
        if key:
            books = Book.objects.filter(Q(title__icontains=key) | Q(author__icontains=key)| Q(category__icontains=key))
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_201_CREATED)