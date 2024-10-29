from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    class Meta:
        model = Book
        list_display = ["title", "author", "publication_year"]

admin.site.register(Book, BookAdmin)