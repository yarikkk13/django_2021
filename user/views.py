from django.shortcuts import render
from rest_framework import status
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
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)


class RetrieveDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            data = UserModel.objects.get(pk=pk)
        except Exception as e:
            return Response('not found')
        serializer = UserSerializer(data)
        return Response(serializer.data)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            data = UserModel.objects.get(pk=pk)
        except Exception as e:
            return Response('not found')
        data.delete()
        return Response('delete')

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        body = self.request.data
        try:
            data = UserModel.objects.get(pk=pk)
        except Exception:
            return Response('Not Found', status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(data, data=body, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_202_ACCEPTED)
