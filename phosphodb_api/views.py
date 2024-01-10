from django.shortcuts import render
from django.db import connection
from django.db.models import Prefetch
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from .models import Pmid
from .serializers import PmidSerializer


class PmidViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all pmids
    """
    queryset = Pmid.objects.all()
    
    @extend_schema(responses=PmidSerializer)
    def list(self, request):
        serializer = PmidSerializer(self.queryset,many = True)
        return Response(serializer.data)
