# Generated by Django 5.0.6 on 2024-07-01 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_counted_views_post_created_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_date'], 'verbose_name': 'پست', 'verbose_name_plural': ' پست ها'},
        ),
    ]
