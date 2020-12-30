from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield  import MultiSelectField

# Create your models here.


class car(models.Model):

	STATE_CHOICES = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
	)


	YEAR_CHOICE = []
	for r in range(2000 , (datetime.now().year+1)):
		YEAR_CHOICE.append((r,r))

	FEATURES_CHOICES = (
		('Cruise Control', 'Cruise Control'),
		('Audio Interface', 'Audio Interface'),
		('Airbags', 'Airbags'),
		('Air Conditioning', 'Air Conditioning'),
		('Seat Heating', 'Seat Heating'),
		('Alarm System', 'Alarm System'),
		('ParkAssist', 'ParkAssist'),
		('Power Steering', 'Power Steering'),
		('Reversing Camera', 'Reversing Camera'),
		('Direct Fuel Injection', 'Direct Fuel Injection'),
		('Auto Start/Stop', 'Auto Start/Stop'),
		('Wind Deflector', 'Wind Deflector'),
		('Bluetooth Handset', 'Bluetooth Handset'),
	)

	DOOR_CHOICES = (
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
		('6', '6'),
	)


	car_title = models.CharField(max_length=255)
	state = models.CharField(choices=STATE_CHOICES,max_length=100)
	city = models.CharField(max_length=100)
	color = models.CharField(max_length=100)
	model = models.CharField(max_length=100)
	year = models.IntegerField(('year'), choices=YEAR_CHOICE)
	condition = models.CharField(max_length=100)
	price = models.IntegerField()
	description = RichTextField()
	car_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
	car_photo1 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
	car_photo2 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
	car_photo3 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
	car_photo4 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
	features = MultiSelectField(choices=FEATURES_CHOICES)
	body_style = models.CharField(max_length=100)
	engine = models.CharField(max_length=100)
	transmission = models.CharField(max_length=100)
	interior = models.CharField(max_length=100)
	miles = models.IntegerField()
	doors = models.CharField(choices=DOOR_CHOICES,max_length=10)
	passengers = models.IntegerField()
	vin_no = models.CharField(max_length=100)
	milage = models.IntegerField()
	fuel_type = models.CharField(max_length=50)
	no_of_owners = models.IntegerField()
	isfeatured = models.BooleanField(default=False)
	created_date = models.DateTimeField(default=datetime.now(), blank=True)


	def __str__(self):
		return self.car_title
