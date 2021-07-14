from django.urls import path
# from .views import MyView
from .views import UserCreateListView, RetrieveDeleteView

urlpatterns = [
    path('', UserCreateListView.as_view(), name='user_list_create'),
    # потрібна, щоб автоматично формувати документацію
    path('/<int:pk>', RetrieveDeleteView.as_view(),
         name='user_retrieve_delete'),
    # path('/test', TestApi.as_view())
]
