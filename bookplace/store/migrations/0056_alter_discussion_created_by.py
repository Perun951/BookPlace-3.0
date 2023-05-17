# Generated by Django 4.2 on 2023-05-17 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0055_remove_discussion_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discussion', to=settings.AUTH_USER_MODEL),
        ),
    ]
