from django.shortcuts import render
from django.views.generic import  TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UserHome(TemplateView):
    template_name = 'projects/user_home.html'


class Hello2View(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
