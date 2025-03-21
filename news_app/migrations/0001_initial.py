# Generated by Django 5.1.7 on 2025-03-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('url_to_image', models.URLField(blank=True, max_length=500, null=True)),
                ('tag', models.CharField(max_length=50)),
                ('published_at', models.DateTimeField()),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
            ],
        ),
    ]
