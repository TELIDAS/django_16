# Generated by Django 4.0.4 on 2022-05-28 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dorama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]