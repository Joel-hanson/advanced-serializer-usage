from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from .serializers import BookModelSerializer
from .models import Book
# Create your views here.

class BookModelViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing books.
    """
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    authentication_classes = [SessionAuthentication]
