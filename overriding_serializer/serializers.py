from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Book, Publisher, Author

class PublisherModelSerializer(ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        request = kwargs.get('context', {}).get('request')
        str_fields = request.GET.get('publisher', '') if request else None
        fields = str_fields.split(',') if str_fields else None

        # Instantiate the superclass normally
        super(PublisherModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


    class Meta:
        model = Publisher
        fields = '__all__'



class AuthorModelSerializer(ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        request = kwargs.get('context', {}).get('request')
        str_fields = request.GET.get('authors', '') if request else None
        fields = str_fields.split(',') if str_fields else None

        # Instantiate the superclass normally
        super(AuthorModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


    class Meta:
        model = Author
        fields = '__all__'


class BookModelSerializer(ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        request = kwargs.get('context', {}).get('request')
        str_fields = request.GET.get('fields', '') if request else None
        fields = str_fields.split(',') if str_fields else None

        # Instantiate the superclass normally
        super(BookModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    authors = SerializerMethodField("get_author_serializer")
    publisher = SerializerMethodField("get_publisher_serializer")

    class Meta:
        model = Book
        fields = '__all__'

    def get_author_serializer(self, obj):
        request = self.context.get('request')
        serializer_context = {'request': request }
        authors = obj.authors.all()
        serializer = AuthorModelSerializer(authors, many=True, context=serializer_context)
        return serializer.data

    def get_publisher_serializer(self, obj):
        request = self.context.get('request')
        serializer_context = {'request': request }
        publisher = obj.publisher
        serializer = PublisherModelSerializer(publisher, context=serializer_context)
        return serializer.data