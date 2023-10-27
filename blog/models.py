from django.db import models
from blog.constants import TYPE_IPHONE


class Hashtag(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Хэштег'
        verbose_name_plural = 'Хэштеги'


class Post(models.Model):
    hashtag = models.ManyToManyField(Hashtag)

    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='',)
    description = models.TextField(blank=True, null=True, )
    type_iphone =models.CharField(max_length=100, choices=TYPE_IPHONE, )
    cost = models.PositiveIntegerField(null=True)
    director = models.CharField(max_length=100)
    number_of_page =models.IntegerField(null=True,)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return (f'Название телефона {self.title}\n'
                f'Цена {self.cost}')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'