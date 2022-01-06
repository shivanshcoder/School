from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, User
from django.db.models.deletion import CASCADE
from faker import Faker
# Create your models here.

"""
    Authentication User Models
"""


class AuthUser(AbstractUser):
    class UserType(models.TextChoices):
        TEACHER = 'T', 'Teacher'
        STUDENT = 'S', 'Student'
        PARENT = 'P', 'Parent'

    last_name = None
    first_name = None

    # ! Not Needed i guess
    user_type = models.CharField(max_length=2, choices=UserType.choices)


"""
    * Profile Models
"""

class BaseUser(models.Model):

    class Meta:
        abstract = True

    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHERS = 'O', 'Others'

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    profile_pic_uri = models.ImageField(blank=True)
    referal_source = models.ForeignKey('ReferalSource', on_delete=CASCADE, null=True)
    gender = models.CharField(max_length=2, choices=Gender.choices)
    is_verified = models.BooleanField('Verification Status', default=False)
    phone = models.CharField(max_length=16, blank=True, unique=True, null=True)

    def seed_func(self, faker):
        import random
        self.username = faker.user_name() + str(int(random.random()*100))
        self.first_name = faker.first_name()
        self.last_name = faker.last_name()
        self.gender = faker.random_element(self.Gender).value
        self.referal_source = faker.random_element(ReferalSource.objects.all())

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




class Parent(BaseUser, AuthUser):
    pass
    # user = models.OneToOneField(
    #     AuthUser, on_delete=CASCADE, related_name='parent_profile')

    # def seed_func(self, faker):
    #     super().seed_func(faker)
        # self.username = faker.user_name()

        # _user = AuthUser.objects.create_user(
        #     f'parent_{faker.user_name()}', f'parent_{faker.email()}', 'pass123')
        # _user.user_type = 'P'
        # _user.save()
        # self.user = _user


class Teacher(BaseUser, AuthUser):
    
    pass
    # user = models.OneToOneField(
    #     AuthUser, on_delete=CASCADE, related_name='teacher_profile')

    # def seed_func(self, faker):
    #     super().seed_func(faker)
    #     self.username = faker.user_name()

        # _user = AuthUser.objects.create_user(
        #     f'teacher_{faker.user_name()}', f'teacher_{faker.email()}', 'pass123')
        # _user.user_type = 'T'
        # _user.save()
        # self.user = _user


class Student(BaseUser, AuthUser):

    # user = models.OneToOneField(
    #     AuthUser, on_delete=CASCADE, related_name='school_profile')
    is_verified = None
    phone = None
    referal_source = None

    dob = models.DateField(blank=True)
    school_class = models.ForeignKey('SchoolClass', on_delete=CASCADE)
    parent_id = models.ForeignKey(Parent, on_delete=CASCADE, related_name='kids')

    def seed_func(self, faker):
        super().seed_func(faker)
        # self.username = faker.user_name()

        self.parent_id = faker.random_element(Parent.objects.all())
        self.school_class = faker.random_element(SchoolClass.objects.all())
        
        self.dob = faker.date()

"""
    * Referenced Extra models
"""

class TitleModel(models.Model):

    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title
    def seed_func(self, faker):
        self.title = faker.text()[:255]

    class Meta:
        abstract = True

class SchoolClass(TitleModel):
    pass
    

class ReferalSource(TitleModel):
    pass
