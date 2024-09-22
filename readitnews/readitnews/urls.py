"""
URL configuration for readitnews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import politics_view, create_article_view

urlpatterns = [
    path('politics/', politics_view, name='politics'),
    path('sports/', sports_view, name='sports'),
    path('technology/', technology_view, name='technology'),
    path('create/', create_article_view, name='create_article'),
]