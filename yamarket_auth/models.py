from django.db import models


class Client(models.Model):
    username = models.CharField(verbose_name='Юзернейм', max_length=150)
    password = models.CharField(verbose_name='Пароль', max_length=150)
    uuid = models.CharField(verbose_name='Уникальный идентификатор', max_length=300)
    subscription = models.DateTimeField(verbose_name='Подписка')
    tg_username = models.CharField(verbose_name='Тег', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.username
