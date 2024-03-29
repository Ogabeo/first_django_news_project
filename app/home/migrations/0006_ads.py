# Generated by Django 5.0.1 on 2024-03-07 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_new_author_alter_new_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_At', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='adss_images/')),
                ('linkedin', models.CharField(max_length=150)),
                ('position', models.CharField(choices=[('one', 'ONE'), ('two', 'TWO')], max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
