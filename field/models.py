from django.db import models
from datetime import datetime, timedelta
from facility.models import Facility

# Create your models here.
class DateTimeEntry(models.Model):
    date = models.DateTimeField()

    def create_future_entries(self):
        if DateTimeEntry.objects.last() is None:
            next_day = datetime.today() + timedelta(days=1)
        else:
            next_day = DateTimeEntry.objects.last().date
            next_day = datetime(next_day.year, next_day.month, next_day.day+1)

        str_day = next_day.strftime("%a")
        for i in range(24):
            date = next_day + timedelta(hours=i)
            instance = DateTimeEntry.objects.create(date=date)
            instance.save()
            for field in Field.objects.all():

                if i in map(int, field.schedule[str_day].split(',')):
                    DateTimeEntryShip.objects.create(field=field, date=instance)


    def delete_old_entries(self):
        previous_day = DateTimeEntry.objects.first().date.date()
        DateTimeEntry.objects.filter(date=previous_day).delete()
    def __str__(self):
        return str(self.date)


class Field(models.Model):
    # Field Related Info
    name = models.CharField(max_length=100)
    schedule = models.JSONField(default=dict)
    belonged_facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='fields')
    reservation_available_dates = models.ManyToManyField(DateTimeEntry, through='DateTimeEntryShip')


    def __str__(self):
        return f"{self.name}"


class DateTimeEntryShip(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    date = models.ForeignKey(DateTimeEntry, on_delete=models.CASCADE)
