from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Article

@permission_required('myapp.can_create', raise_exception=True)
def create_article(request):
    # Logic for creating an article
    if request.method == 'POST':
        # Handle form submission
        ...
    return render(request, 'myapp/create_article.html')

@permission_required('myapp.can_edit', raise_exception=True)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # Logic for editing an article
    ...
    return render(request, 'myapp/edit_article.html')
