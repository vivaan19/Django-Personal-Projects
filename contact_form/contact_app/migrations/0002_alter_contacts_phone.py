# Generated by Django 3.2.8 on 2022-01-02 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
