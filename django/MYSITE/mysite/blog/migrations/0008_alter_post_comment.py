# Generated by Django 5.0.7 on 2024-07-30 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.IntegerField(default=0),
        ),
    ]
