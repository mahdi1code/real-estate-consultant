
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("Customer.urls")),
    path('API',include("API.urls")),
]
