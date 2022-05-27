# Generated by Django 4.0.4 on 2022-05-26 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('In process', 'In Process'), ('Frozen', 'Frozen'), ('Done', 'Done')], default='In process', max_length=10, verbose_name='Состояние'),
        ),
    ]
