from django.db import models

# Create your models here.

# class Person(models.Model):
#     SHIRT_SIZES = {
#         "S": "Small",
#         "M": "Medium",
#         "L": "Large",
#     }

#     first_name = models.CharField(max_length=30, verbose_name= "First Name") 
#     last_name = models.CharField(max_length=30, verbose_name="Last Name") 
#     shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default= "M")



# class Runner(models.Model):
#     MedalType = models.TextChoices("MedalType", "Gold Silver Bronze")
#     name = models.CharField(max_length=60, primary_key= True)
#     medal = models.CharField(blank=True, max_length=30, choices=MedalType)    


# one-to=one relationship

def get_default_husband():
    husband, created = Husband.objects.get_or_create(name= "John", age = 30, wealth = 10)
    return husband.id

class Husband(models.Model):
    name = models.CharField(max_length= 55)
    age = models.IntegerField()
    wealth = models.IntegerField(default= 10)

class Wife(models.Model):
    husband = models.OneToOneField(Husband, on_delete=models.SET_DEFAULT, default= get_default_husband)
    name = models.CharField(max_length=50)
    age = models.IntegerField()    


# many to one relationship    

class Manufacturer(models.Model):
    name = models.CharField(max_length=90)
    origin = models.CharField(max_length=50)


class Car(models.Model):
    colors = {"B": "Black",
              "W": "White",
              "S": "Silver",}
    
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    car_model = models.CharField(max_length=50)
    color = models.CharField(max_length=1, choices=colors, default="W")


# many-to-many

class Author(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

class Book(models.Model):
    author = models.ManyToManyField(Author)
    name = models.CharField(max_length=30)




# extra fields on many to many relationship


class Course(models.Model):
    title = models.CharField(max_length=50)
    students = models.ManyToManyField('Student', through='Enrollment', related_name='courses_taken')

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=50)
    courses = models.ManyToManyField('Course', through='Enrollment', related_name='students_enrolled')


class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)
