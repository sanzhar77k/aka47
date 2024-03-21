# Generated by Django 5.0.1 on 2024-03-05 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_myblogs_small_description_alter_myblogs_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interiors',
            old_name='timline',
            new_name='timeline',
        ),
        migrations.RemoveField(
            model_name='exteriors',
            name='second_image',
        ),
        migrations.RemoveField(
            model_name='exteriors',
            name='short_description',
        ),
        migrations.RemoveField(
            model_name='exteriors',
            name='third_image',
        ),
        migrations.RemoveField(
            model_name='interiors',
            name='second_image',
        ),
        migrations.RemoveField(
            model_name='interiors',
            name='short_description',
        ),
        migrations.RemoveField(
            model_name='interiors',
            name='third_image',
        ),
        migrations.AlterField(
            model_name='exteriors',
            name='main_image',
            field=models.ImageField(upload_to='exteriors/'),
        ),
        migrations.AlterField(
            model_name='interiors',
            name='completion_year',
            field=models.PositiveIntegerField(),
        ),
        migrations.CreateModel(
            name='ExteriorImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='exterior_images/')),
                ('description', models.CharField(default='Your default value here', max_length=255)),
                ('exterior', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.exteriors')),
            ],
        ),
        migrations.CreateModel(
            name='InteriorImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='interior_images/')),
                ('description', models.CharField(default='Your default value here', max_length=255)),
                ('interior', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.interiors')),
            ],
        ),
    ]