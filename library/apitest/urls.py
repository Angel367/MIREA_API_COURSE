from django.urls import path

from . import views

urlpatterns = [
    path('api/contacts/', views.ContactsListView.as_view()),
    path('api/contact/<int:pk>', views.ContactsDetailView.as_view()),
    path('api/phone_numbers/', views.PhoneNumbersListView.as_view()),
    path('api/phone_number/<int:pk>', views.PhoneNumbersDetailView.as_view()),
]
