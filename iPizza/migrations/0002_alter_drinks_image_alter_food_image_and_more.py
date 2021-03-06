# Generated by Django 4.0.3 on 2022-04-05 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iPizza', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinks',
            name='image',
            field=models.ImageField(upload_to='image/drinks/', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(upload_to='image/food/', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='image',
            field=models.ImageField(upload_to='image/pizza/', verbose_name='Фотография'),
        ),
    ]
