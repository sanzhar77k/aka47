# models.py

from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='authors/')  # Путь к папке с фотографиями авторов

    def __str__(self):
        return self.name


class MyBlogs(models.Model):
    CATEGORY_CHOICES = [
        ('Scandinavian Style', 'Скандинавский стиль'),
        ('Modern', 'Модерн'),
        ('Old Modern', 'Старый модерн'),
        ('Baroque', 'Барокко'),
    ]
    image = models.ImageField(upload_to='media/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  # Поле выбора категории
    title = models.CharField(max_length=50)
    small_description = models.CharField(max_length=100, default='Your default value here')
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Связь с моделью Author
    date = models.DateField()

    def __str__(self):
        return self.title






class Interiors(models.Model):
    InteriorName = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to='interiors/')
    second_image = models.ImageField(upload_to='interiors/', default='Your default value here')
    third_image = models.ImageField(upload_to='interiors/', default='Your default value here')
    short_description = models.CharField(max_length=255, default='Your default value here')
    location = models.CharField(max_length=50)
    completion_year = models.PositiveIntegerField(50)
    timline = models.CharField(max_length=15)
    about = models.CharField(max_length=50)
    description = models.CharField(max_length=255)


class Exteriors(models.Model):
    InteriorName = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to='interiors/')
    second_image = models.ImageField(upload_to='interiors/', default='Your default value here')
    third_image = models.ImageField(upload_to='interiors/', default='Your default value here')
    short_description = models.CharField(max_length=255, default='Your default value here')
    location = models.CharField(max_length=50)
    completion_year = models.PositiveIntegerField(50)
    timline = models.CharField(max_length=15)
    about = models.CharField(max_length=50)
    description = models.CharField(max_length=255)



class Comment(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    blog = models.ForeignKey('MyBlogs', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Comment by {self.name} on Blog {self.blog_id}'
    

