from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .validators import validate_year

User = get_user_model()


class TimeStampedModel(models.Model):
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='дата публикации',
    )

    class Meta:
        abstract = True
        ordering = ['-pub_date']


class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр', max_length=200)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.slug


class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.slug


class Title(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=100,
    )
    year = models.IntegerField(
        validators=[validate_year],
        verbose_name='Год выпуска'
    )
    description = models.TextField(verbose_name='Описание', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, related_name='titles',
                                 verbose_name='Категория')
    genre = models.ManyToManyField(Genre, blank=True, verbose_name='Жанр')

    class Meta:
        ordering = ('-year',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE,
                                 verbose_name='Жанр')
    title_id = models.ForeignKey(Title, on_delete=models.CASCADE,
                                 verbose_name='Название')

    def __str__(self):
        return f'{self.title_id}={self.genre_id}'


class Review(TimeStampedModel):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='reviews',
                               verbose_name='автор комментария',)
    title = models.ForeignKey(Title, on_delete=models.CASCADE,
                              related_name='reviews',
                              verbose_name='произведение',)

    score = models.SmallIntegerField(verbose_name='оценка',
                                     validators=[MinValueValidator(1),
                                                 MaxValueValidator(10)])
    text = models.TextField(verbose_name='текст')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_name_author_and_title'
            )
        ]

    def __str__(self):
        return self.text


class Comment(TimeStampedModel):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='автор комментария',)
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='отзыв на произведение')
    text = models.TextField(verbose_name='текст')

    def __str__(self):
        return self.text
