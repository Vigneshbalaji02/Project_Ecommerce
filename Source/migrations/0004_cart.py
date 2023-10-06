# Generated by Django 4.2.1 on 2023-10-03 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Source', '0003_catagory_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_qty', models.ImageField(upload_to='')),
                ('created_at', models.DateField(auto_now=True)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Source.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]