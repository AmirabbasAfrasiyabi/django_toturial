# Generated by Django 5.0.8 on 2024-08-10 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_rename_active_comment_approach_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approach',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='massage',
            new_name='body',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='updated_date',
        ),
    ]