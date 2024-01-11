from django.db import models
from django.db import models
from django.db import transaction
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Add the user to the group

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, password2=None, role=0):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name
        )

        user.role = role
        user.set_password(password)

        with transaction.atomic():
            user.save(using=self._db)

            teachergroup, created = Group.objects.get_or_create(name='Teacher')
            studentgroup, created = Group.objects.get_or_create(name='Student')

            if role == User.STUDENT:
                
                Student.objects.create(user=user)
                user.groups.add(studentgroup)
            elif role == User.TEACHER:
                Teacher.objects.create(user=user)
                user.groups.add(teachergroup)

            elif role == User.ADMIN:
                # Do nothing for admin users
                pass
    
        return user
    def create_superuser(self, email, name, password=None):
        """
        Creates and saves a superuser with the given email, and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            role = User.ADMIN
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    STUDENT = 0
    TEACHER = 1
    ADMIN = 2  
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (ADMIN, 'Admin'), 
    )    
    role = models.IntegerField(default=STUDENT, choices=ROLE_CHOICES)


    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        if self.is_admin:
            return True
        if self.role == User.TEACHER:
            # Define teacher specific permissions
            return perm in ['some_teacher_permission']
        return False

    def has_module_perms(self, app_label):
        if self.is_admin:
            return True
        if self.role == User.TEACHER:
            # Define which app labels a teacher has access to
            return app_label in ['app_label_for_teachers']
        return False

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    def __str__(self):
        return self.user.name
    
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')

    def __str__(self):
        return self.user.name