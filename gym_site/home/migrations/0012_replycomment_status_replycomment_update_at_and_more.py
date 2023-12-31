# Generated by Django 4.2.7 on 2023-12-03 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_replycomment_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='replycomment',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='New', max_length=10),
        ),
        migrations.AddField(
            model_name='replycomment',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='replycomment',
            name='comment',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='replycomment',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]
