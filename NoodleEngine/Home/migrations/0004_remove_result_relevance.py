# Generated by Django 4.1.7 on 2023-06-04 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_result_created_result_html_result_relevance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='relevance',
        ),
    ]
