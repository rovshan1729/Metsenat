from rest_framework import serializers
from . import models


class AddSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AddSponsor
        fields = [
            'id',
            'sponsors',
            'allocated_amount',
            'created_at',
            'updated_at',
        ]
        


class EditSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EditSponsor
        fields = [
            'id',
            'sponsor',
            'allocated_amount',
            'created_at',
            'updated_at',
        ]



class EditStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutStudent
        fields = [
            'id',
            'full_name',
            'phone_number',
            'iniversity_name',
            'contract_amount',
            'created_at',
            'updated_at',
        ]


class AboutStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutStudent
        fields = '__all__'


class AddStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AddStudent
        fields = [
            'id',
            'full_name',
            'phone_number',
            'university_name',
            'type_of_student',
            'contract_amount',
            'created_at',
            'updated_at',
        ]


class StudentFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentFilter
        fields = [
            'id',
            'type_of_student',
            'university_name',
            'created_at',
            'updated_at',
        ]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Students
        fields = [
            'id',
            'full_name',
            'type_of_student',
            'allocated_amount',
            'contract_amount',
            'created_at',
            'updated_at',
        ]


class EditingIndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EditingIndividual
        fields = [
            'id',
            'full_name',
            'phone_number',
            'status',
            'sponsorship_amount',
            'payment_type',
            'created_at',
            'updated_at',
        ]


class EditingLegalEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EditingLegalEntity
        fields = [
            'id',
            'full_name',
            'phone_number',
            'status',
            'sponsorship_amount',
            'payment_type',
            'organization_name',
            'created_at',
            'updated_at',
        ]


class AboutSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutSponsor
        fields = '__all__'


class SponsorsFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SponsorsFilter
        fields = [
            'id',
            'application_status',
            'sponsorship_amount',
            'created_at',
            'updated_at',
        ]


class SponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sponsors
        fields = [
            'id',
            'full_name',
            'phone_number',
            'sponsorship_amount',
            'amount_spend',
            'status',
            'created_at',
            'updated_at',
        ]


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dashboard
        fields = [
            'id',
            'total_paid',
            'total_requested',
            'amount_to_be_paid',
            'sponsors',
            'students',
            'created_at',
            'updated_at',
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