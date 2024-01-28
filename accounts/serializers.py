from rest_framework import serializers
from . import models


class AddSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AddSponsor
        fields = [
            'sponsors',
            'allocated_amount',
        ]
        


class EditSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EditSponsor
        fields = [
            'sponsor',
            'allocated_amount',
        ]



class EditStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutStudent
        fields = [
            'full_name',
            'phone_number',
            'iniversity_name',
            'contract_amount',
        ]


class AboutStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutStudent
        fields = '__all__'


class AddStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AddStudent
        fields = [
            'full_name',
            'phone_number',
            'university_name',
            'type_of_student',
            'contract_amount',
        ]


class StudentFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentFilter
        fields = [
            'type_of_student',
            'university_name',
        ]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Students
        fields = [
            'full_name',
            'type_of_student',
            'allocated_amount',
            'contract_amount',
        ]


class EditingIndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EditingIndividual
        fields = [
            'full_name',
            'phone_number',
            'status',
            'sponsorship_amount',
            'payment_type',
        ]


class EditingLegalEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EditingLegalEntity
        fields = [
            'full_name',
            'phone_number',
            'status',
            'sponsorship_amount',
            'payment_type',
            'organization_name',
        ]


class AboutSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutSponsor
        fields = '__all__'


class SponsorsFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SponsorsFilter
        fields = [
            'application_status',
            'sponsorship_amount',
            'created_at',
        ]


class SponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sponsors
        fields = [
            'full_name',
            'phone_number',
            'sponsorship_amount',
            'amount_spend',
            'status',
        ]


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dashboard
        fields = [
            'total_paid',
            'total_requested',
            'amount_to_be_paid',
            'sponsors',
            'students',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ['username','email','password']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        user = models.CustomUser(
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user