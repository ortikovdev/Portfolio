# Generated by Django 5.0.1 on 2024-05-24 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_alter_education_years'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='years',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='experience',
            name='years',
            field=models.CharField(max_length=10),
        ),
    ]