from django.contrib.auth.models import AbstractUser
from django.db import models


class RoleChoices(models.TextChoices):

    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class User(AbstractUser):
    """Модель пользователя."""

    email = models.EmailField(max_length=254, unique=True)
    role = models.CharField(verbose_name='Роль пользователя', max_length=10,
                            choices=RoleChoices.choices,
                            default=RoleChoices.USER)
    bio = models.TextField(verbose_name='Биография', blank=True)
    confirmation_code = models.CharField(verbose_name='Код подтверждения',
                                         max_length=100, blank=True, null=True)

    class Meta:
        ordering = ('username',)

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        """Проверка прав администратора."""
        return self.role == RoleChoices.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        """Проверка прав модератора."""
        return self.role == RoleChoices.MODERATOR

    @property
    def is_user(self):
        """Проверка стандартных прав."""
        return self.role == RoleChoices.USER
