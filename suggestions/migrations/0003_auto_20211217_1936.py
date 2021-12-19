# Generated by Django 3.0.7 on 2021-12-17 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0002_auto_20211201_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestion',
            name='text',
        ),
        migrations.AddField(
            model_name='suggestion',
            name='contact',
            field=models.IntegerField(default=25470000000),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='field',
            field=models.CharField(default='somewhere', max_length=250),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='transport',
            field=models.IntegerField(default=1500),
        ),
    ]
