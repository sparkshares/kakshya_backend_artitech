# Generated by Django 4.2.8 on 2024-01-10 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectmaterial',
            name='sub_filepath',
            field=models.FileField(upload_to='subjectmaterials'),
        ),
    ]