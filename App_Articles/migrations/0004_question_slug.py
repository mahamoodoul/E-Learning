# Generated by Django 3.1.5 on 2021-01-23 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Articles', '0003_question_question_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(blank=True, max_length=264, unique=True),
        ),
    ]
