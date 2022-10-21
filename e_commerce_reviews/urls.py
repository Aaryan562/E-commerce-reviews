from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('reviews_app.urls')),
    path('admin/', admin.site.urls)
]
