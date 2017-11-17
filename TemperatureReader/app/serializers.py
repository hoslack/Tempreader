from rest_framework import serializers
from .models import Data


class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        pandas_index = ['id']
        pandas_scatter_coord = ['time_read']
        pandas_scatter_location = ['temperature']
        fields = '__all__'

























