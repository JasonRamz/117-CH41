from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=286)
    year = models.IntegerField()
    image = models.ImageField(upload_to='projects_images/')
    repository= models.URLField()
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return f"{self.name} - ({self.year})"
    

class Experience(models.Model):
    entity = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=160)
    period = models.CharField(max_length=128)
    skill = models.ManyToManyField(Skill)

    def __str__(self):
        return f"{self.title} at {self.entity}"