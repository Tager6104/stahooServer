# Generated by Django 2.1.8 on 2019-04-08 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stahooServer', '0002_auto_20190408_0853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partialoperation',
            old_name='user',
            new_name='to_user',
        ),
    ]
