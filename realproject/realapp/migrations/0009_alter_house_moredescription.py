# Generated by Django 4.2.2 on 2023-06-24 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realapp', '0008_house_moredescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='MoreDescription',
            field=models.TextField(default='', max_length=255),
        ),
    ]
