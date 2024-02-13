# Generated by Django 4.1.5 on 2024-02-10 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_academicyear_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='documenttype',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.etablishment'),
        ),
        migrations.AddField(
            model_name='groupsubject',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.etablishment'),
        ),
        migrations.AddField(
            model_name='level',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.etablishment'),
        ),
        migrations.AddField(
            model_name='sanctionappreciation',
            name='academic_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.academicyear'),
        ),
        migrations.AddField(
            model_name='sector',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.etablishment'),
        ),
        migrations.AlterField(
            model_name='etablishment',
            name='currency',
            field=models.CharField(choices=[('F CFA', 'F CFA')], max_length=50),
        ),
    ]