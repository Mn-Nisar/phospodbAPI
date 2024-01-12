from django.shortcuts import render
from django.db import connection
from django.db.models import Prefetch
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema

from .models import (Pmid, Genes, Accession,ExpCondition)
from .serializers import (PmidSerializer,GenesSerializer, AccessionSerializer)


class PmidViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all pmids
    """
    queryset = Pmid.objects.all()
    
    @extend_schema(responses=PmidSerializer)
    def list(self, request):
        serializer = PmidSerializer(self.queryset,many = True)
        return Response(serializer.data)


class PmidViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all pmids
    """
    queryset = Pmid.objects.all()
    
    @extend_schema(responses=PmidSerializer)
    def list(self, request):
        serializer = PmidSerializer(self.queryset,many = True)
        return Response(serializer.data)
            
# class GenesViewSet(viewsets.ViewSet):
#     """
#     A simple Viewset for Genes
#     """
#     queryset = Genes.objects.all()

#     def retrieve(self, request, pk):
#         serializer = GenesSerializer(
#             Genes.objects.filter(gene_symbol=pk)
#             .prefetch_related(Prefetch("gene_symbol_acc"))
#             .select_related("exp_condition"),
#             many=True,
#         )

#         data = Response(serializer.data)
#         return data


class AccessionViewSet(viewsets.ViewSet):
    """
    A simple Viewset for Accession
    """
    queryset = Accession.objects.all()

    @action(detail=False, methods=['get'], url_path=r"gene_symbol/(?P<gene_symbol>[\w,]+)/all")
    def get_condition_by_gene(self, request, gene_symbol=None):
        gene_symbol = gene_symbol.split(',')
        print(gene_symbol)
        serializer = AccessionSerializer(self.queryset.filter(gene_symbol__in=gene_symbol),
            many=True)
        data = Response(serializer.data)
        return data