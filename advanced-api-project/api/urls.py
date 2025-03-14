from django.urls import path
from .views import BookListView, BookDetailView, UpdateView, BookDeleteView, BookCreateView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('books/update/<int:pk>/', UpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    path('books/create', BookCreateView.as_view(), name='book-create')
]