# Generated by Django 4.2.1 on 2023-05-16 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathsapi', '0005_alter_trail_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='img',
            field=models.CharField(max_length=300),
        ),
    ]
