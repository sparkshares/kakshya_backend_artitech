# Generated by Django 4.2.8 on 2024-01-13 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0005_assignmenttransactiontext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmenttext',
            name='a_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='assignmenttexts', to='assignments.assignment'),
        ),
    ]
