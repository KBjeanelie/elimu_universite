# Generated by Django 4.1.5 on 2024-01-19 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('educational_content', '0001_initial'),
        ('user_account', '0001_initial'),
        ('school_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_account.teacher'),
        ),
        migrations.AddField(
            model_name='file',
            name='inFolder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educational_content.folder'),
        ),
        migrations.AddField(
            model_name='ebook',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_account.teacher'),
        ),
        migrations.AddField(
            model_name='ebook',
            name='career',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school_management.career'),
        ),
        migrations.AddField(
            model_name='ebook',
            name='sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school_management.sector'),
        ),
        migrations.AddField(
            model_name='book',
            name='sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_management.sector'),
        ),
    ]
