from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

cities = (
    ('pointe_noire', "Pointe Noire"),
    ('brazzaville', "Brazzaville")
)

sexes = (
    ('masculin', 'Masculin'),
    ('feminin', 'Féminin')
)


# Represent an objet of Student and his profil info
class Student(models.Model):
    
    registration_number = models.CharField(max_length=255, unique=True)
    
    lastname = models.CharField(max_length=50, null=True, blank=True)
    
    firstname = models.CharField(max_length=50, null=True, blank=True)
    
    address = models.CharField(max_length=50, null=True, blank=True)
    
    tel = models.CharField(max_length=20, blank=True)
    
    city = models.CharField(max_length=17, choices=cities, blank=True)
    
    sex = models.CharField(max_length=10, choices=sexes, blank=True)
    
    email = models.CharField(max_length=120, unique=True, blank=True)
    
    bithday = models.DateField(null=True, blank=True)
    
    nationality = models.CharField(max_length=20, blank=True)
    
    picture = models.ImageField(upload_to="student_pics", blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"Matricule : {self.registration_number} - {self.lastname} {self.firstname}"


# Represent an objet of Teacher and his profil info
class Teacher(models.Model):
    
    lastname = models.CharField(max_length=50, blank=True)
    
    firstname = models.CharField(max_length=50, blank=True)
    
    address = models.CharField(max_length=50, blank=True)
    
    tel = models.CharField(max_length=20, blank=True)
    
    city = models.CharField(max_length=17, choices=cities, blank=True)
    
    sex = models.CharField(max_length=10, choices=sexes, blank=True)
    
    bithday = models.DateField(blank=True, null=True)
    
    nationality = models.CharField(max_length=20, blank=True)
    
    email = models.CharField(max_length=120, unique=True, blank=True)
    
    status = models.CharField(max_length=20, blank=True)
    
    last_diploma = models.CharField(max_length=20, blank=True)
    
    picture = models.ImageField(upload_to="teacher_pics", blank=True, null=True)
    
    type_of_counter = models.CharField(max_length=20, blank=True)
    
    start_of_contrat = models.DateField(blank=True, null=True)
    
    end_of_contrat = models.DateField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"Enseignant : {self.lastname} - {self.firstname}"



# Represent an objet of team manager and his profil info
class ManagementProfil(models.Model):

    lastname = models.CharField(max_length=50, blank=True)
    
    firstname = models.CharField(max_length=50, blank=True)
    
    address = models.CharField(max_length=50, blank=True)
    
    tel = models.CharField(max_length=20, blank=True)
    
    city = models.CharField(max_length=17, choices=cities, blank=True)
    
    sex = models.CharField(max_length=10, choices=sexes, blank=True)
    
    email = models.CharField(max_length=120, unique=True, blank=True)
    
    bio = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    updated_at = models.DateTimeField(auto_now=True, null=True)



class UserManager(BaseUserManager):
    def create_user(self, username, password=None,):
        """
        Creates and saves a User with the given username, password.
        """
        user = self.model(username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_student_user(self, username, student, password=None,):
        """
        Creates and saves a User with the given username, password.
        """
        user = self.model(username=username, student=student)

        user.set_password(password)
        user.is_student = True
        user.save(using=self._db)
        return user
    
    def create_teacher_user(self, username, teacher, password=None,):
        """
        Creates and saves a User with the given username, password.
        """
        user = self.model(username=username, teacher=teacher)

        user.set_password(password)
        user.is_teacher = True
        user.save(using=self._db)
        return user
    
    def create_manager_user(self, username, manager_profil, password=None,):
        """
        Creates and saves a User with the given username, password.
        """
        user = self.model(username=username, management_profil = manager_profil)

        user.set_password(password)
        user.is_manager = True
        user.save(using=self._db)
        return user
    
    def create_accountant_user(self, username, manager_profil, password=None,):
        """
        Creates and saves a User with the given username, password.
        """
        user = self.model(username=username, management_profil = manager_profil)

        user.set_password(password)
        user.is_accountant = True
        user.save(using=self._db)
        return user

    

    def create_superuser(self, username, password=None):
        """
        Creates and saves a superuser with the given email, and password.
        """
        user = self.create_user(password=password,username=username)
        user.is_admin = True
        user.save(using=self._db)
        return user


#  Custom User Model
class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length=255, unique=True,)
    
    student = models.OneToOneField(Student, unique=True, on_delete=models.DO_NOTHING, null=True, blank=True)
    
    teacher = models.OneToOneField(Teacher, unique=True, on_delete=models.DO_NOTHING, null=True, blank=True)
    
    management_profil = models.OneToOneField(ManagementProfil, unique=True, on_delete=models.CASCADE, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    
    is_admin = models.BooleanField(default=False)
    
    is_manager = models.BooleanField(default=False)
    
    is_accountant = models.BooleanField(default=False)
    
    is_student = models.BooleanField(default=False)
    
    is_teacher = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'


    def __str__(self):
        return f"Utilisateur : {self.username}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
