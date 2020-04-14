# Generated by Django 3.0.3 on 2020-03-29 06:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mail_address', models.CharField(max_length=200)),
                ('prefecture', models.IntegerField()),
                ('address1', models.TextField()),
                ('address2', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
                ('insert_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]