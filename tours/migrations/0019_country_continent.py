# Generated by Django 3.2.3 on 2021-05-27 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0018_auto_20210518_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='continent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country_region', to='tours.region'),
        ),
    ]