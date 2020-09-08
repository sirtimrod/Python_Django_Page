from django.db import models

class Human(models.Model):
    human_login = models.CharField('Логин пользователя', max_length=200)
    human_mail = models.CharField('Почта пользователя', max_length=250)
    human_password = models.TextField('Пароль пользователя')

    def __str__(self):
        return self.human_login

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
