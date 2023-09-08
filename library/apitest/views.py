from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *

# Create your views here.


class BooksListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(instance=books, many=True)
        return Response(serializer.data)


class BooksDetailView(APIView):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(instance=book)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorsListView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(instance=authors, many=True)
        return Response(serializer.data)


class AuthorsDetailView(APIView):
    def get(self, request, pk):
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(instance=author)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(instance=author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = Author.objects.get(pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LibrariesListView(APIView):
    def get(self, request):
        libraries = Library.objects.all()
        serializer = LibrarySerializer(instance=libraries, many=True)
        return Response(serializer.data)


class LibrariesDetailView(APIView):
    def get(self, request, pk):
        library = Library.objects.get(pk=pk)
        serializer = LibrarySerializer(instance=library)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        library = Library.objects.get(pk=pk)
        serializer = LibrarySerializer(instance=library, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        library = Library.objects.get(pk=pk)
        library.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
