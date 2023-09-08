from django.urls import path

from . import views

urlpatterns = [
    path('api/books/', views.BooksListView.as_view()),
    path('api/book/<int:pk>', views.BooksDetailView.as_view()),
    path('api/authors/', views.AuthorsListView.as_view()),
    path('api/author/<int:pk>', views.AuthorsDetailView.as_view()),
    path('api/libraties/', views.LibrariesListView.as_view()),
    path('api/library/<int:pk>', views.LibrariesDetailView.as_view()),
]
