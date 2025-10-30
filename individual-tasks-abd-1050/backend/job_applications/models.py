from django.db import models

# Create your models here.

class Resume(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    address = models.TextField()
    def __str__(self):
        return self.name



class Skill(models.Model):
    resume = models.ForeignKey(Resume ,null=True, related_name = 'skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    skill_level = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

class EducationHistory(models.Model):
    resume = models.ForeignKey(Resume ,null=True, related_name = 'education_history', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)

class Job(models.Model):
    resume = models.ForeignKey(Resume ,null=True, related_name = 'job_history', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    




    
    