from django.urls import path
from relationship_app.views import list_books, LibraryDetailView
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView
from . import views
urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
     path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Login view
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Logout view
    path('register/', views.register, name='register'),  # Registration view
    path('admin/', views.admin_view, name='admin_view'),  # Admin view
    path('librarian/', views.librarian_view, name='librarian_view'),  # Librarian view
    path('member/', views.member_view, name='member_view'),  # Member view
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
]