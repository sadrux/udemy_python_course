# Generated by Django 2.0.5 on 2018-08-08 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='placeholder.png', upload_to='img'),
        ),
    ]