# Generated by Django 3.1.6 on 2022-04-08 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('wikipedia', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField(blank=True, null=True)),
                ('summary', models.TextField(blank=True)),
                ('category', models.CharField(blank=True, choices=[('AV', 'Aventure'), ('TR', 'Thriller'), ('FS', 'Fantastique'), ('RM', 'Romance'), ('HR', 'Horreur'), ('SF', 'Science-fiction')], max_length=30)),
                ('stock', models.IntegerField(blank=True, default=0)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
            ],
        ),
    ]
