# Generated by Django 4.1.5 on 2023-02-05 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='posts',
            new_name='post',
        ),
    ]
