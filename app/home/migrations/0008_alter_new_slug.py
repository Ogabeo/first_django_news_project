# Generated by Django 5.0.2 on 2024-03-11 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_linkedin_ads_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='slug'),
        ),
    ]