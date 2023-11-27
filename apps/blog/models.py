from django.db import models
from django_resized.forms import ResizedImageField

# Create your models here.
class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок новости"
    )
    descriptions = models.TextField(
        verbose_name="Описание новости"
    )
    image = ResizedImageField(
        force_format="WEBP",
	    quality=100,
        upload_to="image/"
    )
    create = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания новости",
        blank=True, null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"