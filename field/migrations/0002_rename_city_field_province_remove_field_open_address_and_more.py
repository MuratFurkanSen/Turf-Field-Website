# Generated by Django 4.2.16 on 2024-11-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('field', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='field',
            old_name='city',
            new_name='province',
        ),
        migrations.RemoveField(
            model_name='field',
            name='open_address',
        ),
        migrations.AddField(
            model_name='field',
            name='building',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='field',
            name='indoor',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='field',
            name='neighborhood',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='field',
            name='street',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='field',
            name='reservation_hours',
            field=models.CharField(choices=[('00-01', '00-01'), ('01-02', '01-02'), ('02-03', '02-03'), ('03-04', '03-04'), ('04-05', '04-05'), ('05-06', '05-06'), ('06-07', '06-07'), ('07-08', '07-08'), ('08-09', '08-09'), ('09-10', '09-10'), ('10-11', '10-11'), ('11-12', '11-12'), ('12-13', '12-13'), ('13-14', '13-14'), ('14-15', '14-15'), ('15-16', '15-16'), ('16-17', '16-17'), ('17-18', '17-18'), ('18-19', '18-19'), ('19-20', '19-20'), ('20-21', '20-21'), ('21-22', '21-22'), ('22-23', '22-23'), ('23-24', '23-24')], max_length=100),
        ),
    ]
