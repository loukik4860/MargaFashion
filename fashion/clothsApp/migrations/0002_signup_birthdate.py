# Generated by Django 4.0.4 on 2022-05-31 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='Birthdate',
            field=models.DateField(null=True),
        ),
    ]
