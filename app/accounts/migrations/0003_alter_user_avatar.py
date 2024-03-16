# Generated by Django 5.0.1 on 2024-03-01 05:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user_avatar', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('jpg', 'png', 'heic', 'jpeg'))]),
        ),
    ]