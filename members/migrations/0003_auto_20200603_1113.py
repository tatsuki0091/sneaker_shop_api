# Generated by Django 3.0.3 on 2020-06-03 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20200511_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mail_address',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]