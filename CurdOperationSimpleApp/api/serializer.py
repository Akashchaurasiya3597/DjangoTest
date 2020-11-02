from CurdOperationSimpleApp.models import Studentdatabase
from rest_framework.serializers import ModelSerializer


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Studentdatabase
        fields = '__all__'
