# Generated by Django 4.2.7 on 2023-12-03 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_post_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]