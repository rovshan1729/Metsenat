from . import serializers
from . import models
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination




#ADD SPONSOR
class AddSponsorListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.AddSponsor.objects.all()
    serializer_class = serializers.AddSponsorSerializer


#EDIT STUDENT'S SPONSOR
class EditSponsorListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.EditSponsor.objects.all()
    serializer_class = serializers.EditSponsorSerializer


class EditSponsorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.EditSponsor.objects.all()
    serializer_class = serializers.EditSponsorSerializer


#EDIT STUDENT
class EditStudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.EditStudent.objects.all()
    serializer_class = serializers.EditStudentSerializer


class EditStudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.EditStudent.objects.all()
    serializer_class = serializers.EditStudentSerializer
    

#ABOUT STUDENT
class AboutStudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.AddStudent.objects.all()
    serializer_class = serializers.AboutStudentSerializer


class AboutStudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AddStudent.objects.all()
    serializer_class = serializers.AboutStudentSerializer


#ADD STUDENT
class AddStudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.AddStudent.objects.all()
    serializer_class = serializers.AddStudentSerializer


class AddStudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AddStudent.objects.all()
    serializer_class = serializers.AddStudentSerializer


#STUDENT'S FILTER
class StudentFilterListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.StudentFilter.objects.all()
    serializer_class = serializers.StudentFilterSerializer


class StudentFilterRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudentFilter.objects.all()
    serializer_class = serializers.StudentFilterSerializer



#STUDENTS
class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Students.objects.all()
    serializer_class = serializers.StudentSerializer
    pagination_class = PageNumberPagination
    page_size = 10


class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Students.objects.all()
    serializer_class = serializers.StudentSerializer


#EDITING SPONSOR
class EditingIndividualListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.EditingIndividual.objects.all()
    serializer_class = serializers.EditingIndividualSerializer


class EditingIndividualRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.EditingIndividual.objects.all()
    serializer_class = serializers.EditingIndividualSerializer


class EditingLegalEntityListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.EditingLegalEntity.objects.all()
    serializer_class = serializers.EditingLegalEntitySerializer


class EditingLegalEntityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.EditingLegalEntity.objects.all()
    serializer_class = serializers.EditingLegalEntitySerializer



#ABOUT SPONSOR
class AboutSponsorListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.AboutSponsor.objects.all()
    serializer_class = serializers.AboutSponsorSerializer
    pagination_class = PageNumberPagination
    page_size = 10


class AboutSponsorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AboutSponsor.objects.all()
    serializer_class = serializers.AboutSponsorSerializer


#SPONSOR'S FILTER
class SponsorsFilterListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.SponsorsFilter.objects.all()
    serializer_class = serializers.SponsorsFilterSerializer


class SponsorsFilterRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SponsorsFilter.objects.all()
    serializer_class = serializers.SponsorsFilterSerializer


#SPONSORS
class SponsorsListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Sponsors.objects.all()
    serializer_class = serializers.SponsorsSerializer


class SponsorsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Sponsors.objects.all()
    serializer_class = serializers.SponsorsSerializer


#DASHBOARD
class DashboardListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Dashboard.objects.all()
    serializer_class = serializers.DashboardSerializer


class DashboardRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Dashboard.objects.all()
    serializer_class = serializers.DashboardSerializer


class UserLogoutView(generics.DestroyAPIView):
        permission_classes = [IsAuthenticated]
        
        def destroy(self, request, *args, **kwargs):
            try:
                request.user.auth_token.delete()
                return Response({'message':'Successfully logged out.'},status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class UserLoginView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer

    def login(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = models.CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'message':'Login Successfull!','token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class RegisterUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
