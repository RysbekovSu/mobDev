from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    email = models.EmailField(max_length=100, unique=True, db_index=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.URLField(max_length=200, unique=True, db_index=True, default="no")
    level = models.CharField(max_length=100, db_index=True)
    rate = models.IntegerField(db_index=True)
    price = models.IntegerField( db_index=True)
    description = models.CharField(max_length=400, db_index=True)
    insta = models.CharField(max_length=100, db_index=True)
    tel = models.CharField(max_length=100, db_index=True)
    num = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name



class Liked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'teacher'], name='unique_user_teacher')
        ]

    def __str__(self):
        return f'{self.user.username} likes {self.teacher.name}'

class Article(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    photo = models.URLField(max_length=200, unique=True, db_index=True)
    quote = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField(unique=True, db_index=True)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Words(models.Model):
    word = models.CharField(max_length=100, unique=True, db_index=True)
    translation = models.CharField(max_length=100, unique=True, db_index=True)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.word
