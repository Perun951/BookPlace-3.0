# Generated by Django 4.1.6 on 2023-02-24 23:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_alter_product_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pdf',
            field=models.FileField(default=django.utils.timezone.now, upload_to='pdfs/'),
            preserve_default=False,
        ),
    ]
