# Generated by Django 5.1.4 on 2025-01-07 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoProject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
