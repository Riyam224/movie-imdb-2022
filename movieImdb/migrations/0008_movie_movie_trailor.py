# Generated by Django 4.0.4 on 2022-04-23 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieImdb', '0007_alter_movie_category_alter_movie_langauge_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_trailor',
            field=models.URLField(default=1, verbose_name='movie trailor'),
            preserve_default=False,
        ),
    ]
