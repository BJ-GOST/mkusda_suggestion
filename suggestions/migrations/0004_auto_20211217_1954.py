# Generated by Django 3.0.7 on 2021-12-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0003_auto_20211217_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='site',
            field=models.CharField(default='propossed mission site', max_length=250),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='contact',
            field=models.IntegerField(default=254734567890),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='field',
            field=models.CharField(default='site conference', max_length=250),
        ),
    ]
