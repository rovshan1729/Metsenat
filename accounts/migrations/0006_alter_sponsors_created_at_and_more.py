# Generated by Django 5.0.1 on 2024-01-28 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_editingindividual_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsors',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sponsorsfilter',
            name='created_at',
            field=models.DateField(),
        ),
    ]