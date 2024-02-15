# Generated by Django 4.1.5 on 2024-02-15 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_etablishment_month'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financialcommitment',
            name='school',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='school',
        ),
        migrations.RemoveField(
            model_name='repayment',
            name='school',
        ),
        migrations.RemoveField(
            model_name='spend',
            name='school',
        ),
        migrations.AddField(
            model_name='financialcommitment',
            name='academic_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.academicyear'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='academic_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.academicyear'),
        ),
        migrations.AddField(
            model_name='repayment',
            name='academic_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.academicyear'),
        ),
        migrations.AddField(
            model_name='spend',
            name='academic_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.academicyear'),
        ),
    ]
