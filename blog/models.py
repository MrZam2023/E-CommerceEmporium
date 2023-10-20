from django.db import models

class Post(models.Model):

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    TYPE_IPHONE = (
        ('Apple', 'Apple'),
        ('Samsung', 'Samsung'),
        ('Huawei', 'Huawei'),
        ('Honor', 'Honor')
    )


    title = models.CharField(max_length=100, verbose_name='Название модели', null=True)
    image = models.ImageField(upload_to='', verbose_name='Загрузите фотографию')
    description = models.TextField(blank=True, null=True, verbose_name='Описание товара')
    type_iphone =models.CharField(max_length=100, choices=TYPE_IPHONE, verbose_name='Выберите модель')
    cost = models.PositiveIntegerField(verbose_name='Укажите цену', null=True)
    director = models.CharField(max_length=100, verbose_name='Укажите название модели')
    number_of_page =models.IntegerField(null=True, verbose_name='Укажите кол-во товара')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return (f'Название телефона {self.title}\n'
                f'Цена {self.cost}')

