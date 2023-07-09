from django.db import models
from django.conf import settings
from django.utils import timezone


class Book(models.Model):
    '''Store information about a book'''
    
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.FloatField()
    availability = models.IntegerField()
    # cover = models.ImageField(upload_to='covers/')
    rating = models.FloatField(null=True)
    def __str__(self):
        return self.title


class LibraryAdmin(models.Model):
    '''Extending CustomUser model to perform CRUD operations on Book model'''

    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Student(models.Model):
    ''' Extending CustomUser model. This model is be used to add relation with Book model and store information regarding books issued by student. '''

    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    books_issued = models.ManyToManyField(Book,through="Record")

    def __str__(self):
        return self.user.email


class Record(models.Model):
    '''Intermediate model to store info about transaction that takes place when student issues a book'''

    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    date_issued = models.DateField(default=timezone.now)


class BookRatings(models.Model):
    user = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    rating = models.FloatField()