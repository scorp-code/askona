# Generated by Django 4.1.6 on 2023-02-09 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sayt', '0008_alter_dislike_user_alter_like_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dislike',
            name='user',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
    ]
