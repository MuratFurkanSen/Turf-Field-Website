# Generated by Django 4.2.16 on 2024-12-15 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_have_shoes', models.BooleanField()),
                ('province', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('building', models.CharField(max_length=100)),
                ('indoor', models.CharField(max_length=100)),
                ('maps_location', models.CharField(max_length=100)),
            ],
        ),
    ]
