# Generated by Django 4.2.16 on 2024-11-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('field', '0004_datetimeentry_remove_field_reservation_hours_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='schedule',
            field=models.JSONField(default=dict),
        ),
    ]