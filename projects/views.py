import uuid

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render

from .models import Project
from .serializers import ProjectSerializer
from django.http import Http404


class Hello2View(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class UserHome(TemplateView):
    template_name = 'projects/user_home.html'


class ProjectView(TemplateView):
    template_name = 'projects/projects.html'

    def get(self, request, *args, **kwargs):
        projects = Project.objects.filter(user=request.user)
        return render(request, self.template_name, {'projects': projects})


class ApiProjectListView(APIView):
    permission_classes = (IsAuthenticated,)

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
