from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
import uuid

# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
        default=None,
        help_text="Обязательное поле. Не более 30 символов. Только буквы, цифры и @/./+/-/_.",
        validators=[AbstractUser.username_validator],
        error_messages={
            'unique': "Пользователь с таким именем пользователя уже существует.",
        },
    )
    profile_image = models.ImageField(
        upload_to = "profile_image/",
        verbose_name="Фотография профиля",
        blank = True, null = True,
        default = "profile_image/no_image.png"
    )
    biography = models.TextField(
        verbose_name="Биография",
        blank=True, null=True
    )
    phone = models.CharField(
        max_length=100,
        verbose_name="Номер телефона",
        blank=True, null=True
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name='Facebook',
        blank=True, null=True
    )
    twitter = models.URLField(
        verbose_name='Twitter',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name='Instagram',
        blank=True, null=True
    )
    telegram = models.URLField(
        max_length=255,
        verbose_name='Telegram',
        blank=True, null=True
    )

    def save(self, *args, **kwargs):
        # Если значение username не установлено, генерировать значение по умолчанию
        if not self.username:
            base_username = f"user-{slugify(self.first_name)}-{slugify(self.last_name)}"[:25]
            self.username = f"{base_username}-{str(uuid.uuid4())[:4]}"

        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username 
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        