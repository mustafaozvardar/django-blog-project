# Generated by Django 5.0 on 2023-12-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_article_image_alter_article_contet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Add Image'),
        ),
    ]
