# Generated by Django 4.2.7 on 2023-12-04 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_remove_replycomment_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='replycomment',
            name='comment',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.comment'),
            preserve_default=False,
        ),
    ]
