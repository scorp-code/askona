# Generated by Django 4.1.6 on 2023-02-10 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sayt', '0011_like_dislike_like_like_like_user_delete_dislike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
    ]
