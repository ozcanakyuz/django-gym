# Generated by Django 4.2.7 on 2023-12-03 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_contactformmessage_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(default=1),
        ),
    ]
