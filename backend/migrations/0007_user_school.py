# Generated by Django 4.1.5 on 2024-02-10 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_ebook_school_event_school_financialcommitment_school_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.etablishment'),
        ),
    ]
