from django.db import models

# Create your models here.
HOUR_CHOICES = tuple(
    (f'{str(i).zfill(2)}-{str(i+1).zfill(2)}', f'{str(i).zfill(2)}-{str(i+1).zfill(2)}') for i in range(24)
)

TURKEY_CITIES = (
    ('empty', ''),
    ('adana', 'Adana'),
    ('adiyaman', 'Adıyaman'),
    ('afyonkarahisar', 'Afyonkarahisar'),
    ('agri', 'Ağrı'),
    ('amasya', 'Amasya'),
    ('ankara', 'Ankara'),
    ('antalya', 'Antalya'),
    ('artvin', 'Artvin'),
    ('aydın', 'Aydın'),
    ('balikesir', 'Balıkesir'),
    ('bilecik', 'Bilecik'),
    ('bingol', 'Bingöl'),
    ('bitlis', 'Bitlis'),
    ('bolu', 'Bolu'),
    ('burdur', 'Burdur'),
    ('bursa', 'Bursa'),
    ('canakkale', 'Çanakkale'),
    ('cankiri', 'Çankırı'),
    ('corum', 'Çorum'),
    ('denizli', 'Denizli'),
    ('diyarbakir', 'Diyarbakır'),
    ('edirne', 'Edirne'),
    ('elazig', 'Elazığ'),
    ('erzincan', 'Erzincan'),
    ('erzurum', 'Erzurum'),
    ('eskisehir', 'Eskişehir'),
    ('gaziantep', 'Gaziantep'),
    ('giresun', 'Giresun'),
    ('gumushane', 'Gümüşhane'),
    ('hakkari', 'Hakkari'),
    ('hatay', 'Hatay'),
    ('igdir', 'Iğdır'),
    ('isparta', 'Isparta'),
    ('istanbul', 'İstanbul'),
    ('izmir', 'İzmir'),
    ('kahramanmaras', 'Kahramanmaraş'),
    ('karabuk', 'Karabük'),
    ('karaman', 'Karaman'),
    ('kars', 'Kars'),
    ('kastamonu', 'Kastamonu'),
    ('kayseri', 'Kayseri'),
    ('kirikkale', 'Kırıkkale'),
    ('kirklareli', 'Kırklareli'),
    ('kirsehir', 'Kırşehir'),
    ('kocaeli', 'Kocaeli'),
    ('konya', 'Konya'),
    ('kutahya', 'Kütahya'),
    ('malatya', 'Malatya'),
    ('manisa', 'Manisa'),
    ('mardin', 'Mardin'),
    ('mersin', 'Mersin'),
    ('mugla', 'Muğla'),
    ('mus', 'Muş'),
    ('nevsehir', 'Nevşehir'),
    ('nigde', 'Niğde'),
    ('ordu', 'Ordu'),
    ('osmaniye', 'Osmaniye'),
    ('rize', 'Rize'),
    ('sakarya', 'Sakarya'),
    ('samsun', 'Samsun'),
    ('siirt', 'Siirt'),
    ('sinop', 'Sinop'),
    ('sivas', 'Sivas'),
    ('sanliurfa', 'Şanlıurfa'),
    ('sirnak', 'Şırnak'),
    ('tekirdag', 'Tekirdağ'),
    ('tokat', 'Tokat'),
    ('trabzon', 'Trabzon'),
    ('tunceli', 'Tunceli'),
    ('usak', 'Uşak'),
    ('van', 'Van'),
    ('yalova', 'Yalova'),
    ('yozgat', 'Yozgat'),
    ('zonguldak', 'Zonguldak'),
)

class Field(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, choices=TURKEY_CITIES, default="empty")
    district = models.CharField(max_length=100)
    open_address = models.CharField(max_length=100)
    maps_location = models.URLField()
    reservation_hours = models.CharField(max_length=100, choices=HOUR_CHOICES) # "Starting Hours" 9,10,11
    is_have_shoes = models.BooleanField()

    def __str__(self):
        return f"{self.id} - {self.name}"