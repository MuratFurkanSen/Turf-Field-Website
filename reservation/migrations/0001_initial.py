# Generated by Django 4.2.16 on 2024-10-06 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('field', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('reservation_date', models.DateTimeField()),
                ('field', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='field.field')),
                ('users', models.ManyToManyField(related_name='reservations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
