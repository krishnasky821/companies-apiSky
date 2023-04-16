# Generated by Django 4.0 on 2023-04-16 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=255, unique=True)),
                ('comp_headq', models.CharField(max_length=255)),
                ('how_old', models.CharField(max_length=255)),
                ('comp_no_emp', models.CharField(max_length=255)),
                ('comp_review', models.CharField(max_length=255)),
                ('open_jobs', models.CharField(max_length=255)),
                ('comp_services', models.CharField(max_length=255)),
                ('comp_desc', models.CharField(max_length=255)),
                ('comp_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.types')),
            ],
        ),
    ]
