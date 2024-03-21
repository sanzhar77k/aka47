from django.db import models
from django.utils import timezone
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class Author(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='authors/')

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
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=50)
    small_description = models.CharField(max_length=100, default='Your default value here')
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.title



class Interiors(models.Model):
    InteriorName = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to='interiors/')
    location = models.CharField(max_length=50)
    completion_year = models.PositiveIntegerField()
    timeline = models.CharField(max_length=15)
    about = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if self.main_image:
            self.main_image = self.compress_image(self.main_image)
        super().save(*args, **kwargs)

    def compress_image(self, image):
        img = Image.open(image)
        img_io = BytesIO()

        # Определяем формат изображения (JPEG, PNG, JPG)
        format = img.format if img.format in ['JPEG', 'PNG', 'JPG'] else 'JPEG'

        # Сжимаем изображение до определенного размера
        img.save(img_io, format=format, quality=70)
        new_image = InMemoryUploadedFile(
            img_io, None, image.name, f'image/{format.lower()}', img_io.getbuffer().nbytes, None
        )

        return new_image


class InteriorImage(models.Model):
    interior = models.ForeignKey(Interiors, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='interior_images/')
    description = models.CharField(max_length=255, default='Your default value here')

    def save(self, *args, **kwargs):
        if self.image:
            self.image = self.compress_image(self.image)
        super().save(*args, **kwargs)

    def compress_image(self, image):
        img = Image.open(image)
        img_io = BytesIO()

        # Определяем формат изображения (JPEG, PNG, JPG)
        format = img.format if img.format in ['JPEG', 'PNG', 'JPG'] else 'JPEG'

        # Сжимаем изображение до определенного размера
        img.save(img_io, format=format, quality=70)
        new_image = InMemoryUploadedFile(
            img_io, None, image.name, f'image/{format.lower()}', img_io.getbuffer().nbytes, None
        )

        return new_image


class Exteriors(models.Model):
    InteriorName = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to='exteriors/')
    location = models.CharField(max_length=50)
    completion_year = models.PositiveIntegerField(50)
    timline = models.CharField(max_length=15)
    about = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if self.main_image:
            self.main_image = self.compress_image(self.main_image)
        super().save(*args, **kwargs)

    def compress_image(self, image):
        img = Image.open(image)
        img_io = BytesIO()

        # Определяем формат изображения (JPEG, PNG, JPG)
        format = img.format if img.format in ['JPEG', 'PNG', 'JPG'] else 'JPEG'

        # Сжимаем изображение до определенного размера
        img.save(img_io, format=format, quality=70)
        new_image = InMemoryUploadedFile(
            img_io, None, image.name, f'image/{format.lower()}', img_io.getbuffer().nbytes, None
        )

        return new_image


class ExteriorImage(models.Model):
    exterior = models.ForeignKey(Exteriors, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='exterior_images/')
    description = models.CharField(max_length=255, default='Your default value here')

    def save(self, *args, **kwargs):
        if self.image:
            self.image = self.compress_image(self.image)
        super().save(*args, **kwargs)

    def compress_image(self, image):
        img = Image.open(image)
        img_io = BytesIO()

        # Определяем формат изображения (JPEG, PNG, JPG)
        format = img.format if img.format in ['JPEG', 'PNG', 'JPG'] else 'JPEG'

        # Сжимаем изображение до определенного размера
        img.save(img_io, format=format, quality=70)
        new_image = InMemoryUploadedFile(
            img_io, None, image.name, f'image/{format.lower()}', img_io.getbuffer().nbytes, None
        )

        return new_image


class Comment(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    blog = models.ForeignKey('MyBlogs', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Comment by {self.name} on Blog {self.blog_id}'
