from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    private = models.BooleanField(default=False)
    user_id = models.ForeignKey('auth.User', related_name='questions')

    def __str_(self):
        return self.title

class Answer(models.Model):
    body = models.TextField()
    question_id = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    user_id = models.ForeignKey('auth.User', related_name='answers')


    def __str__(self):
        return self.body

class Tenant(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    api_key = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name


class History(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    count = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.count
