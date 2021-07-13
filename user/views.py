from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView
from .models import UserModel
from .serializers import UserSerializer


# Create your views here.

# class MyView(APIView):
#     def get(self, *args, **kwargs):
#         return Response('hello from get')
#
#     def post(self, *args, **kwargs):
#         return Response('hello from post')
#
#     def put(self, *args, **kwargs):
#         return Response('hello from put')
#
#     def patch(self, *args, **kwargs):
#         return Response('hello from patch')
#
#     def delete(self, *args, **kwargs):
#         return Response('hello from delete')
#
#
# class MyViewSecond(APIView):
#     def get(self, *args, **kwargs):
#         return Response('Ok')


class UserCreateListView(APIView):
    def get(self, *args, **kwargs):
        qs = UserModel.objects.all()
        serializer = UserSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        body = self.request.data
        serializer = UserSerializer(data=body)
