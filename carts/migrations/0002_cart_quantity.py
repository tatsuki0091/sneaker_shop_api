# Generated by Django 3.0.3 on 2020-07-20 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]