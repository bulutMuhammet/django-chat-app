# mysite/urls.py
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
]

