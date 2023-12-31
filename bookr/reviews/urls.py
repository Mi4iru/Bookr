
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books/', views.book_list, name='books_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('book-search/', views.book_search, name='book_search')
]