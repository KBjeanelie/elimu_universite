# Generated by Django 4.1.5 on 2024-02-21 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0028_studentdocument_school_teacherdocument_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='documenttype',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
