# Generated by Django 4.0.3 on 2022-04-02 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iPizza', '0002_discount_remove_menu_new_menu_is_new_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='discount',
            field=models.CharField(default=1, max_length=10, verbose_name='Скидка'),
            preserve_default=False,
        ),
    ]
