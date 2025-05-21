from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError


def validate_image_name(value):
    if not value.endswith(('.jpg', '.jpeg', '.png')):
        raise ValidationError(
            f"{value} is not a valid image file. Please upload a .jpg, .jpeg, or .png file."
        )
    return value


def validate_email(value):
    if not value.endswith('@gmail.com'):
        raise ValidationError(
            f"{value} is not a valid email address. Please use an @gmail.com email."
        )
    return value

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=100)
    content = models.TextField()
    image_name = models.CharField(max_length=255, validators=[validate_image_name])
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(default='', null=False, unique=True, blank=True, db_index=True)
    tags = models.ManyToManyField('Tag')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if empty
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(validators=[validate_email])

    def save(self, *args, **kwargs):
        self.email = self.email_address.lower()
        super().save(*args, **kwargs)


class Tag(models.Model):
    caption = models.CharField(max_length=30)