# from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
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
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        body = self.request.data
        serializer = UserSerializer(data=body)
        # if not serializer.is_valid():
        #     return Response(serializer.errors)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class RetrieveDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = get_object_or_404(UserModel, pk=pk)
        # try:
        #     data = UserModel.objects.get(pk=pk)
        # except Exception as e:
        #     return Response('not found')
        serializer = UserSerializer(data)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        body = self.request.data
        try:
            data = UserModel.objects.get(pk=pk)
        except Exception:
            return Response('Not Found', status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(data, data=body)
        serializer.is_valid(raise_exception=True)
        # if not serializer.is_valid():
        #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            data = UserModel.objects.get(pk=pk)
        except Exception as e:
            return Response('not found', status.HTTP_404_NOT_FOUND)
        data.delete()
        return Response('delete', status.HTTP_204_NO_CONTENT)

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



# class TestApi(APIView):
#     def get(self, *args, **kwargs):
#         qs = UserModel.objects.all()
#         lt = self.request.query_params.get('lt', None)
#         if lt:
#             qs = qs.filter(age__lt=lt)
#         serializer = UserSerializer(qs, many=True)
#         return Response(serializer.data)
