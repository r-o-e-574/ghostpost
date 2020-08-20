"""django_ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from ghostpost import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('createpost/', views.create_post, name="createpost"),
    path('boasts/', views.boast_view, name="boasts" ),
    path('roasts/', views.roast_view, name="roasts" ),
    path('upvote/<int:upvote_id>/', views.upvotes_view, name="upvote"),
    path('downvote/<int:downvote_id>/', views.downvotes_view, name="downvote"),
    path('sortbyvote/', views.sortbyvote_view, name="sortbyvote"),
    path('admin/', admin.site.urls),
]
