# Generated by Django 4.2.7 on 2023-12-04 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_replycomment_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='replycomment',
            old_name='comment',
            new_name='comment_id',
        ),
    ]
