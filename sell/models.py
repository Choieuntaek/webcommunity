from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Create your models here.

class User(AbstractUser):
    username = models.CharField(verbose_name='유저이름', error_messages={"unique": "이미 존재하는 유저이름 입니다."}, unique=True,
                                max_length=15, validators=[
            RegexValidator(regex='[^a-zA-Z0-9-_가-힣]', inverse_match=True)])
    level = models.IntegerField(blank=True, null=True)


class Category(models.Model):
    title = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    level = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class Writing(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.subject


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    writing = models.ForeignKey(Writing, on_delete=models.CASCADE)
    content = models.TextField()
    level = models.IntegerField(blank=True, null=True)
    reply_id = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)


class Writingip(models.Model):
    ip = models.CharField(max_length=30)
    writing = models.ForeignKey(Writing, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.ip


class Ip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return self.ip
