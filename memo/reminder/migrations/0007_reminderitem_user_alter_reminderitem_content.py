# Generated by Django 4.2.2 on 2023-07-09 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reminder', '0006_reminderitem_title_alter_reminderitem_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminderitem',
            name='user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reminderitem',
            name='content',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Content'),
        ),
    ]