# Generated by Django 4.0.4 on 2022-06-01 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.DateField(null=True),
        ),
    ]
