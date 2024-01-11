# Generated by Django 4.2.8 on 2024-01-10 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_title', models.CharField(max_length=200)),
                ('class_description', models.TextField()),
                ('audio_path', models.FileField(upload_to='media/class_records')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassRecordSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=200)),
                ('sub_description', models.TextField()),
                ('sub_code', models.CharField(blank=True, editable=False, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subm_title', models.CharField(max_length=200)),
                ('subm_description', models.TextField()),
                ('sub_filepath', models.FileField(upload_to='media/subjectmaterials')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sub_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjectmaterial', to='academics.subject')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectMaterialText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_text', models.TextField()),
                ('sub_mat_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='subjectmaterialtexts', to='academics.subjectmaterial')),
            ],
        ),
    ]