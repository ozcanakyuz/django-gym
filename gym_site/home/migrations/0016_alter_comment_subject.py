# Generated by Django 4.2.7 on 2023-12-04 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_comment_subject_delete_replycomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]