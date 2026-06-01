from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.CharField(max_length=100)

    image = models.ImageField(
        upload_to='products/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
    



class Report(models.Model):

    title = models.CharField(max_length=100)

    image = models.ImageField(
        upload_to='reports/images/',
        null=True,
        blank=True
    )

    pdf = models.FileField(
        upload_to='reports/pdfs/',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Profile(models.Model):

    name = models.CharField(max_length=100)

    profile_image = models.ImageField(
        upload_to='profiles/'
    )

    def __str__(self):
        return self.name


class Resume(models.Model):

    name = models.CharField(max_length=100)

    resume_pdf = models.FileField(
        upload_to='resumes/'
    )

    def __str__(self):
        return self.name