import uuid

from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect


from django.contrib.auth.models import User


from django.shortcuts import render

from .models import Project
from .serializers import ProjectSerializer, ProjectMetaDataSerializer
from django.http import Http404


class Hello2View(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class RedirectToProjectView(TemplateView):

    def get(self, request, *args, **kwargs):
        try:
            token_key = request.GET.get("token")
            token = Token.objects.get(key=token_key)
        except ObjectDoesNotExist:
            return redirect('/')
        login(request, token.user, backend='allauth.account.auth_backends.AuthenticationBackend')
        return redirect('project')


class ProjectView(LoginRequiredMixin, TemplateView):
    template_name = 'projects/projects.html'
    learningml_url = settings.LEARNING_ML_URL

    def get(self, request, *args, **kwargs):
        projects = Project.objects.filter(user=request.user)
        return render(request, self.template_name, {
            'projects': projects,
            'learningml_url': self.learningml_url
        })


class ApiProjectListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        projects = Project.objects.filter(user=request.user)
        serializer = ProjectMetaDataSerializer(projects, many=True)
        return Response(serializer.data)


    def post(self, request):
        data = request.data
        data['user'] = request.user.id
        data['uuid'] = str(uuid.uuid1())

        print(data)
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiProjectDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = request.user
        project = self.get_object(pk)

        serializer = ProjectSerializer(project, data=request.data)

        if user != project.user:
            return Response(["No puedes modificar un proyecto que no es tuyo"],
                            status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = request.user

        project = self.get_object(pk)
        if user != project.user:
            return Response(["No puedes eliminar un proyecto que no es tuyo"],
                            status=status.HTTP_403_FORBIDDEN)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
