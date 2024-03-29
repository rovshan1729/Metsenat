# Generated by Django 5.0.1 on 2024-01-28 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_sponsors_status_sponsorsfilter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=255)),
                ('type_of_student', models.CharField(choices=[('barchasi', 'Barchasi'), ('magistr', 'Magistr'), ('bakalavr', 'Bakalavr')], default='barchasi', max_length=20)),
                ('university_name', models.CharField(max_length=100)),
                ('allocated_amount', models.IntegerField()),
                ('contract_amount', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AboutSponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.sponsors')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EditingIndividual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
                ('status', models.CharField(choices=[('yangi', 'Yangi'), ('moderatsiyada', 'Moderatsiyada'), ('tasdiqlangan', 'Tasdiqlangan'), ('bekor_qilingan', 'Bekor qilingan')], max_length=100)),
                ('sponsorship_amount', models.IntegerField()),
                ('payment_type', models.CharField(choices=[('naqt', "naqt o'tkazma"), ('kredit_karta', "kredit karta o'tkazma")], default='naqt', max_length=40)),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.sponsors')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EditingLegalEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
                ('status', models.CharField(choices=[('yangi', 'Yangi'), ('moderatsiyada', 'Moderatsiyada'), ('tasdiqlangan', 'Tasdiqlangan'), ('bekor_qilingan', 'Bekor qilingan')], max_length=100)),
                ('sponsorship_amount', models.IntegerField()),
                ('payment_type', models.CharField(choices=[('naqt', "naqt o'tkazma"), ('kredit_karta', "kredit karta o'tkazma")], max_length=40)),
                ('organization_name', models.CharField(max_length=100)),
                ('editIndividual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.editingindividual')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.sponsors')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentFilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type_of_student', models.CharField(choices=[('barchasi', 'Barchasi'), ('magistr', 'Magistr'), ('bakalavr', 'Bakalavr')], default='barchasi', max_length=20)),
                ('university_name', models.CharField(default='barchasi', max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.students')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
