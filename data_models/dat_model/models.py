from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    author = models.CharField(max_length=100)
    is_bestselling = models.BooleanField(null=False, default=False)
    slug = models.SlugField(default='', null=False, unique=True, blank=True, db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            if not self.id:
                super().save(*args, **kwargs)

            self.slug = slugify(f"{self.title}-{self.id}")
            return super().save(update_fields=['slug'])

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
