# Generated by Django 4.1.5 on 2024-01-19 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='label',
            field=models.CharField(max_length=50),
        ),
    ]
