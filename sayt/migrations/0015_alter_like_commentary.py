# Generated by Django 4.1.6 on 2023-02-10 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sayt', '0014_rename_maqsad_product_maqsad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='commentary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='sayt.comment'),
        ),
    ]
