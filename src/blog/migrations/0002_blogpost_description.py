# Generated by Django 3.1.6 on 2022-04-08 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]