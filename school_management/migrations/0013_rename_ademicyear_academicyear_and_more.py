# Generated by Django 4.1.5 on 2023-11-08 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0012_studentcareer_schedule_sanctionappreciation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdemicYear',
            new_name='AcademicYear',
        ),
        migrations.RenameField(
            model_name='academicyear',
            old_name='statut',
            new_name='status',
        ),
        migrations.AlterField(
            model_name='subject',
            name='type',
            field=models.CharField(choices=[('obligatory', 'Obligatory'), ('secondary', 'Secondary')], max_length=12),
        ),
    ]