from rest_framework import serializers

from .models import (Pmid,)

class PmidSerializer(serializers.ModelSerializer):

   class Meta:
        model = Pmid
        fields = "__all__"
