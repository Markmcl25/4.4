from django.urls import path
from .views import politics_view, sports_view, technology_view, create_article_view
from django.shortcuts import render  # Import render for the success page

urlpatterns = [
    path('politics/', politics_view, name='politics'),
    path('sports/', sports_view, name='sports'),
    path('technology/', technology_view, name='technology'),
    path('create/', create_article_view, name='create_article'),
    path('success/', lambda request: render(request, 'success.html'), name='success'),  # Simple success page
]
