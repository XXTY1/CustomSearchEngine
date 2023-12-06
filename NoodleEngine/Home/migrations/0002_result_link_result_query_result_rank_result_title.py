# Generated by Django 4.1.7 on 2023-06-04 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='link',
            field=models.TextField(default='', unique=True),
        ),
        migrations.AddField(
            model_name='result',
            name='query',
            field=models.TextField(default='', unique=True),
        ),
        migrations.AddField(
            model_name='result',
            name='rank',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='result',
            name='title',
            field=models.TextField(default='', max_length=500),
        ),
    ]