"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.notes_list, name='notes_list'),
    path('notes/<int:pk>/', views.notes_detail, name='notes_detail'),
    path('notes/create_notes/', views.notes_create, name='notes_create'),
    path('notes/<int:pk>/edit', views.notes_edit, name='notes_edit'),
    path('notes/<int:pk>/delete', views.notes_delete, name='notes_delete'),
    path('notes/results', views.search_result, name="search_result"),
    # path('notes/search_notes', views.search_notes, name='search_notes'),
    
    
 
]

