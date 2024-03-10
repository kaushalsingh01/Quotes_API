from rest_framework import serializers
from .models import Quote

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        # fields = ['id', 'quotes','given_by']
        exclude = ('id',)
