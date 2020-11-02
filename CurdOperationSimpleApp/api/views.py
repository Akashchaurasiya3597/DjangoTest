from CurdOperationSimpleApp.models import Studentdatabase
from .serializer import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from django.core.mail import send_mail


class StudentViewSet(ModelViewSet):
    queryset = Studentdatabase.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        msg = " New Enquiry Received From Sri Hari Mobile App.\n Customer Name- {},\n Contact- {},\n Village- {} "
        response = super(StudentViewSet, self).create(request, args, *kwargs)

        send_mail('testing Received. ', msg, 'akashchaurasiya3597@gmail.com', ['aaakash1431@gmail.com'])

        return response