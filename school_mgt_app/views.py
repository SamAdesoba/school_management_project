from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from school_mgt_app.models import SchoolAdmin
from school_mgt_app.serializer import SchoolAdminSerializer


class SchoolAdminViewSet(ModelViewSet):
    queryset = SchoolAdmin.objects.all()
    serializer_class = SchoolAdminSerializer
