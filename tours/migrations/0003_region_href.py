# Generated by Django 3.2.1 on 2021-05-13 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_category_category_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='href',
            field=models.URLField(blank=True),
        ),
    ]