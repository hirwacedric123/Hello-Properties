# Generated by Django 4.2.2 on 2023-06-26 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realapp', '0012_car_moredescription_landplot_moredescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='carModel',
            field=models.CharField(default='', max_length=255),
        ),
    ]