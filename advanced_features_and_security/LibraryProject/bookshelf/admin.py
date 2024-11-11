from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class BookAdmin(admin.ModelAdmin):
        list_display = ["title", "author", "publication_year"]
        list_filter = ["title", "author"]
        search_fields = ["title"]

admin.site.register(Book, BookAdmin)



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
