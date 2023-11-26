# Generated by Django 4.1.3 on 2023-11-26 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_comment_ip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='email',
            new_name='subject',
        ),
        migrations.AddField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(default=1),
        ),
    ]