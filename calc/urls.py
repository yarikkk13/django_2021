from django.urls import path
from .views import mathematics, home


urlpatterns = [
    path('', home),
    path('/<int:a>/<str:symbol>/<int:b>', mathematics)
]
