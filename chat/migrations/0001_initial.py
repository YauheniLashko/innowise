# Generated by Django 4.0.4 on 2022-05-04 11:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
                ('status', models.CharField(choices=[('In process', 'In process'), ('Frozen', 'Frozen'), ('Done', 'Done')], default='In process', max_length=10, verbose_name='Состояние')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Отправитель')),
            ],
            options={
                'ordering': ['-time_create'],
            },
        ),
    ]
