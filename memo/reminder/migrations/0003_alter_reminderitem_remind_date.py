# Generated by Django 4.2.2 on 2023-06-29 20:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0002_reminderitem_remind_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminderitem',
            name='remind_date',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]