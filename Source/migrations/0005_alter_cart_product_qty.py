# Generated by Django 4.2.1 on 2023-10-04 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Source', '0004_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Product_qty',
            field=models.IntegerField(),
        ),
    ]
