# Generated by Django 4.1.5 on 2024-02-12 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_student_is_valid'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanctionappreciationtype',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.etablishment'),
        ),
    ]
