from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *

# Create your views here.


class ContactsListView(APIView):
    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(instance=contacts, many=True)
        return Response(serializer.data)


class ContactsDetailView(APIView):
    def get(self, request, pk):
        contact = Contact.objects.get(pk=pk)
        serializer = ContactSerializer(instance=contact)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        contact = Contact.objects.get(pk=pk)
        serializer = ContactSerializer(instance=contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        contact = Contact.objects.get(pk=pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhoneNumbersListView(APIView):
    def get(self, request):
        phone_numbers = PhoneNumber.objects.all()
        serializer = PhoneNumberSerializer(instance=phone_numbers, many=True)
        return Response(serializer.data)


class PhoneNumbersDetailView(APIView):
    def get(self, request, pk):
        phone_number = PhoneNumber.objects.get(pk=pk)
        serializer = PhoneNumberSerializer(instance=phone_number)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = PhoneNumberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        phone_number = PhoneNumber.objects.get(pk=pk)
        serializer = PhoneNumberSerializer(instance=phone_number, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        phone_number = PhoneNumber.objects.get(pk=pk)
        phone_number.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
