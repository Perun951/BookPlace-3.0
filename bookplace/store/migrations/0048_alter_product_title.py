# Generated by Django 4.2 on 2023-05-03 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0047_alter_product_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]
