# Generated by Django 4.2 on 2023-05-22 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_customer_verificat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='Sample_User_Icon.png', null=True, upload_to='uploads/profile_images/'),
        ),
    ]
