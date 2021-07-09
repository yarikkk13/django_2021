from django.urls import path

from .views import home, add_user, delete_user

urlpatterns = [
    path('', home),
    path('/create/<int:id>/<str:name>', add_user),
    path('/delete/<int:id>', delete_user)
]
