from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

# Home Model
class Comment(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    image = models.ImageField(upload_to="assets/comment")
    comment = models.CharField(max_length=200)
    def __str__(self):
        return self.name


   

class Team(models.Model):
    image =  models.ImageField(upload_to="assets/team")
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    twitter_link = models.CharField(max_length=200)
    facebook_link = models.CharField(max_length=200)
    instagram_link = models.CharField(max_length=200)
    linkedin_link = models.CharField(max_length=200)

    def __str__(self):
        return self.title



class CourseCategory(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='assets/course')

    def __str__(self):
        return self.title


class Statistic(models.Model):
    baxtli_mijozlar = models.CharField(max_length=20)
    loyihalar = models.CharField(max_length=20)
    qollab_quvvatlash = models.CharField(max_length=20)
    mehnatkashlar = models.CharField(max_length=20)
    def __str__(self):
       return "statistics"



class Asosiy_Malumotlar(models.Model):
    text = RichTextField()
    image = models.ImageField(upload_to="Asosiy_Malumotlar")



class Fleshcardlar(models.Model):
    question = models.CharField(max_length=60)
    answer = models.CharField(max_length=110)



