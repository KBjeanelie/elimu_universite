# Generated by Django 4.1.5 on 2024-01-23 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0003_student_allergy_student_birthday_place_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
    ]