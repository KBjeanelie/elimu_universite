# Generated by Django 4.1.5 on 2024-01-19 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagementProfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(blank=True, max_length=50)),
                ('firstname', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('tel', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, choices=[('pointe_noire', 'Pointe Noire'), ('brazzaville', 'Brazzaville')], max_length=17)),
                ('sex', models.CharField(blank=True, choices=[('masculin', 'Masculin'), ('feminin', 'Féminin')], max_length=10)),
                ('email', models.CharField(blank=True, max_length=120, unique=True)),
                ('bio', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=255, unique=True)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('firstname', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('tel', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, choices=[('pointe_noire', 'Pointe Noire'), ('brazzaville', 'Brazzaville')], max_length=17)),
                ('sex', models.CharField(blank=True, choices=[('masculin', 'Masculin'), ('feminin', 'Féminin')], max_length=10)),
                ('email', models.CharField(blank=True, max_length=120, unique=True)),
                ('bithday', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=20)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='student_pics')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(blank=True, max_length=50)),
                ('firstname', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('tel', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, choices=[('pointe_noire', 'Pointe Noire'), ('brazzaville', 'Brazzaville')], max_length=17)),
                ('sex', models.CharField(blank=True, choices=[('masculin', 'Masculin'), ('feminin', 'Féminin')], max_length=10)),
                ('bithday', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=120, unique=True)),
                ('status', models.CharField(blank=True, max_length=20)),
                ('last_diploma', models.CharField(blank=True, choices=[('Doctorat', 'Doctorat'), ('Master', 'Master'), ('Licence', 'Licence'), ('DUT', 'DUT'), ('Baccalauréat', 'Baccalauréat')], max_length=20)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='teacher_pics')),
                ('type_of_counter', models.CharField(blank=True, max_length=20)),
                ('start_of_contrat', models.DateField(blank=True, null=True)),
                ('end_of_contrat', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_manager', models.BooleanField(default=False)),
                ('is_accountant', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('management_profil', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_account.managementprofil')),
                ('student', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_account.student')),
                ('teacher', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_account.teacher')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
