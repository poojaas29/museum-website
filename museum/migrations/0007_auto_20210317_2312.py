# Generated by Django 3.1.7 on 2021-03-17 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0006_auto_20210317_2258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='username',
            new_name='usernamed',
        ),
    ]
