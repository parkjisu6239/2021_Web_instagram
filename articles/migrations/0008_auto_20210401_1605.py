# Generated by Django 3.1.7 on 2021-04-01 07:05

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20210401_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='image/article_image'),
        ),
    ]
