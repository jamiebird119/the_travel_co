# Generated by Django 3.2.1 on 2021-05-14 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0009_alter_tour_site_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=3000, null=True),
        ),
    ]