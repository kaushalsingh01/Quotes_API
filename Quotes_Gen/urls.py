from django.urls import path
from .views import quotesviewset

urlpatterns = [
    path('', quotesviewset),
]
