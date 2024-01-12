from rest_framework import serializers

from .models import (Pmid, Genes, Accession)

class PmidSerializer(serializers.ModelSerializer):

   class Meta:
        model = Pmid
        fields = "__all__"


class GenesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genes
        fields = "__all__"

class AccessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accession
        fields = "__all__"
