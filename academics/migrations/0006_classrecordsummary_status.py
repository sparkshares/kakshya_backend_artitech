# Generated by Django 4.2.8 on 2024-01-11 07:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0005_subjectenrolled'),
    ]

    operations = [
        migrations.AddField(
            model_name='classrecordsummary',
            name='status',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
