# Generated by Django 4.0.3 on 2022-04-10 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_recommendation_delivery_recommendation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment',
            field=models.IntegerField(verbose_name='Оплата'),
        ),
    ]
