# Generated by Django 4.1.4 on 2023-01-14 04:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0013_category_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': '이미 존재하는 유저이름 입니다.'}, max_length=15, unique=True, validators=[django.core.validators.RegexValidator(inverse_match=True, regex='[^a-zA-Z0-9-_가-힣]')], verbose_name='유저이름'),
        ),
    ]
