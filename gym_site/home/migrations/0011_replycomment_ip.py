# Generated by Django 4.2.7 on 2023-12-03 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_replycomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='replycomment',
            name='ip',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
