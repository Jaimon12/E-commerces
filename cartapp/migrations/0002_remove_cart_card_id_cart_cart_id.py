# Generated by Django 4.2.6 on 2023-10-17 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='card_id',
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(default='12:30:00', max_length=250, unique=True),
            preserve_default=False,
        ),
    ]
