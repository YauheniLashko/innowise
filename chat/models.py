from django.contrib.auth.models import User
from django.db import models


class Ticket(models.Model):

    class SetStatus(models.TextChoices):
        IN_PROCESS = "In process"
        FROZEN = 'Frozen'
        DONE = "Done"

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(max_length=500, verbose_name="Описание")
    status = models.CharField(max_length=10, choices=SetStatus.choices,
                              default=SetStatus.IN_PROCESS, verbose_name="Состояние")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Отправитель')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']


class Message(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    message_text = models.TextField(verbose_name="Сообщение")
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Отправитель")

    def __str__(self):
        return self.message_text
