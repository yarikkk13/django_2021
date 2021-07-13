from django.urls import path
# from .views import MyView
from .views import UserCreateListView

urlpatterns = [
    path('', UserCreateListView.as_view(), name = 'car_list_create') #потрібна, щоб автоматично формувати документацію
]
