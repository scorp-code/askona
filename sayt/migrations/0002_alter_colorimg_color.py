# Generated by Django 4.1.6 on 2023-02-06 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colorimg',
            name='color',
            field=models.CharField(max_length=128),
        ),
    ]
