# Generated by Django 5.0.1 on 2024-03-07 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_ads'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='linkedin',
            new_name='link',
        ),
    ]