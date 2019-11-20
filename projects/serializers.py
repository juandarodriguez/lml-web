import json
from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'json_data', 'uuid', 'user']


class ProjectMetaDataSerializer(serializers.ModelSerializer):
    classes = serializers.SerializerMethodField('extractClasses')

    def extractClasses(self, project):
        json_data_dict = json.loads(project.json_data)

        classes = []

        for _class in json_data_dict:
            classes.append(_class)

        return classes

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'uuid', 'user', 'classes']