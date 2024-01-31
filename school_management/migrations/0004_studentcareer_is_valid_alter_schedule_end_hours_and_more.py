# Generated by Django 4.1.5 on 2024-01-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0003_alter_studentdocument_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcareer',
            name='is_valid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='end_hours',
            field=models.CharField(choices=[('07h', '07h'), ('08h', '08h'), ('09h', '09h'), ('10h', '10h'), ('11h', '11h'), ('12h', '12h'), ('13h', '13h'), ('14h', '14h'), ('15h', '15h'), ('16h', '16h'), ('17h', '17h')], max_length=15),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_hours',
            field=models.CharField(choices=[('07h', '07h'), ('08h', '08h'), ('09h', '09h'), ('10h', '10h'), ('11h', '11h'), ('12h', '12h'), ('13h', '13h'), ('14h', '14h'), ('15h', '15h'), ('16h', '16h'), ('17h', '17h')], max_length=15),
        ),
    ]
