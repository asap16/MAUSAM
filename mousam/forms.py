from django import forms
import datetime
import floppyforms as forms
#from django.contrib.gis.db import models
#from django.contrib.gis.geos import Point
#from location_field.models.spatial import LocationField
#import googlemaps

#gmaps = googlemaps.Client(key='AIzaSyCNDgVBQOjrDHLXOwS9UQLfOS-eZ57nUGo')


class DatePicker(forms.DateInput):
    #template_name = 'index.html'

    class Media:
        js = (
            'js/jquery.min.js',
            'js/jquery-ui.min.js',
        )
        css = {
            'all': (
                'css/jquery-ui.css',
            )
        }

class InfoForm(forms.Form):
	CHOICES = (('1', 'Male',), ('2','Female'))
	gender = forms.ChoiceField(widget=forms.RadioSelect, choices = CHOICES)
	address = forms.CharField(max_length = 255)
	day = forms.DateField(widget=DatePicker,initial=datetime.date.today)
	#day = forms.DateField(initial=datetime.date.today)
	CHOICES_time = (('01','01'),('02','02'),('30','03'),('04','04'),('05','05'),('06','06'),('07','07'),('08','08'),('09','09'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),
					('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21','21'),('22','22'),('23','23'),('24','24'))
	time = forms.ChoiceField(widget=forms.Select, choices = CHOICES_time)

	class Meta:
		fields = ('address', 'day', 'gender', 'time')
	

