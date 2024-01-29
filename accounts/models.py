from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    

class Dashboard(BaseModel):
    total_paid = models.IntegerField()
    total_requested = models.IntegerField()
    amount_to_be_paid = models.IntegerField()

    #GRAPH
    sponsors = models.IntegerField()
    students = models.IntegerField()


class Sponsors(BaseModel):
    full_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    sponsorship_amount = models.IntegerField(
        validators=[MinValueValidator(0),MaxValueValidator(50000000)]
    )
    amount_spend = models.IntegerField()
    STATUS_CHOICES = [
        ('barchasi','Barchasi'),
        ('yangi','Yangi'),
        ('moderatsiyada','Moderatsiyada'),
        ('tasdiqlangan','Tasdiqlangan'),
        ('bekor_qilingan','Bekor qilingan'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    


    def __str__(self) -> str:
        return self.full_name

    
class SponsorsFilter(BaseModel):
    sponsor = models.ForeignKey(Sponsors,on_delete=models.CASCADE)
    application_status = models.CharField(max_length=20,choices=Sponsors.STATUS_CHOICES,default='barchasi')
    STATUS_CHOICES_FOR_MONEY = [
        ('barchasi','Barchasi'),
        ('1_mln','1 000 000'),
        ('5_mln','5 000 000'),
        ('7_mln','7 000 000'),
        ('10_mln','10 000 000'),
        ('30_mln','30 000 000'),
        ('50_mln','50 000 000'),
    ]
    sponsorship_amount = models.CharField(max_length=20,
                                          choices=STATUS_CHOICES_FOR_MONEY,
                                          default='barchasi')
    created_at = models.DateField()
    

class AboutSponsor(BaseModel):
    sponsor = models.ForeignKey(Sponsors,on_delete=models.CASCADE)
    

class EditingIndividual(BaseModel):
    sponsor = models.ForeignKey(Sponsors,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    status = models.CharField(max_length=100,choices=Sponsors.STATUS_CHOICES)
    sponsorship_amount = models.IntegerField()
    CHOICE_PAYMENT_TYPE = [
        ('naqt',"naqt o'tkazma"),
        ('kredit_karta',"kredit karta o'tkazma")
    ]
    payment_type = models.CharField(max_length=40,choices=CHOICE_PAYMENT_TYPE,default='naqt')


class EditingLegalEntity(BaseModel):
    sponsor = models.ForeignKey(Sponsors,on_delete=models.CASCADE)
    editIndividual = models.ForeignKey(EditingIndividual,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    status = models.CharField(max_length=100,choices=Sponsors.STATUS_CHOICES)
    sponsorship_amount = models.IntegerField()
    payment_type = models.CharField(max_length=40,choices=EditingIndividual.CHOICE_PAYMENT_TYPE)
    organization_name = models.CharField(max_length=100)


class Students(BaseModel):
    full_name = models.CharField(max_length=255)
    TYPE_OF_STUDENT = [
        ('barchasi','Barchasi'),
        ('magistr','Magistr'),
        ('bakalavr','Bakalavr')
    ]
    type_of_student = models.CharField(max_length=20,choices=TYPE_OF_STUDENT,default='barchasi')
    university_name = models.CharField(max_length=100)
    allocated_amount = models.IntegerField()
    contract_amount = models.IntegerField()


class StudentFilter(BaseModel):
    student = models.ForeignKey(Students,on_delete=models.CASCADE)
    type_of_student = models.CharField(max_length=20,choices=Students.TYPE_OF_STUDENT,default='barchasi')
    university_name = models.CharField(max_length=100)


class AddStudent(BaseModel):
    student = models.ForeignKey(Students,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    university_name = models.CharField(max_length=100)
    type_of_student = models.CharField(max_length=100,choices=Students.TYPE_OF_STUDENT,default='barchasi')
    contract_amount = models.IntegerField()
    

class AboutStudent(BaseModel):
    student = models.ForeignKey(Students,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student)


class EditStudent(BaseModel):
    full_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    university_name = models.CharField(max_length=100)
    contract_amount = models.IntegerField()


class EditSponsor(BaseModel):
    sponsor = models.ForeignKey(Sponsors,on_delete=models.CASCADE)

    allocated_amount = models.IntegerField(
        validators=[MinValueValidator(0),MaxValueValidator(30000000)]
    )


class AddSponsor(BaseModel):
    sponsors = models.ForeignKey(Sponsors,on_delete=models.CASCADE,null=False)
    allocated_amount = models.IntegerField(
        validators=[MinValueValidator(0),MaxValueValidator(30000000)]
    )

    def __str__(self) -> str:
        return str(self.sponsors)
