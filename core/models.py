from django.db import models

# Create your models here.
class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=225, null=False)
    school_address = models.CharField(max_length=225, null=False)
    phone_number = models.CharField(max_length=225, null=False)
    manager_name = models.CharField(max_length=225, null=False)
    PRIMARY = 'primary'
    SECONDARY = 'secondary'
    HIGH_SCHOOL = 'high_school'
    SCHOOL_TYPES = [
        (PRIMARY, 'Primary'),
        (SECONDARY, 'Secondary'),
        (HIGH_SCHOOL, 'High School'),
    ]

    school_type = models.CharField(
        max_length=20,
        choices=SCHOOL_TYPES,
        default=PRIMARY,
        null=False
    )

    BOYS = 'boys'
    GIRLS = 'girls'
    MIXED = 'mixed'
    GENDER_CHOICES = [
        (BOYS, 'Boys'),
        (GIRLS, 'Girls'),
        (MIXED, 'Mixed')
    ]
    school_gender_type = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default=MIXED,
        null=False
    )

    def __str__(self):
        return f"{self.school_name}, {self.school_address}, {self.phone_number}, {self.manager_name}, {self.school_type}, {self.school_gender_type}, {self.school_city}"


class Classroom(models.Model):
    class_id = models.AutoField(primary_key=True)
    grade = models.CharField(max_length=225, null=False)
    section = models.CharField(max_length=225, null=False)
    num_chairs = models.IntegerField(null=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.grade} - {self.section} - {self.num_chairs} chairs - School: {self.school}"


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=225, null=False)
    last_name = models.CharField(max_length=225, null=False)
    date_of_birth = models.DateField(null=False)
    email = models.EmailField(null=False, unique=True)
    city = models.CharField(max_length=225, null=False)
    ID_number = models.CharField(max_length=225, unique=True, null=False)
    address = models.CharField(max_length=225, null=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    classroom = models.ManyToManyField(Classroom)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.date_of_birth} - {self.email} - {self.city} - {self.ID_number} - {self.address}"
