# Generated by Django 4.1.4 on 2023-01-31 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0017_writing_is_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writing',
            name='is_new',
        ),
    ]
