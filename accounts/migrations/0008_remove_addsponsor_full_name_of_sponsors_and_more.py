# Generated by Django 5.0.1 on 2024-01-29 07:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_editstudent_alter_studentfilter_university_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addsponsor',
            name='full_name_of_sponsors',
        ),
        migrations.RemoveField(
            model_name='editsponsor',
            name='full_name',
        ),
        migrations.AlterField(
            model_name='sponsors',
            name='sponsorship_amount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50000000)]),
        ),
    ]