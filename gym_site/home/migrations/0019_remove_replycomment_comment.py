# Generated by Django 4.2.7 on 2023-12-04 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_replycomment_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='replycomment',
            name='comment',
        ),
    ]
