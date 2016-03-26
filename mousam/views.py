from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from mousam.forms import InfoForm
import json
from urllib.request import urlopen, Request
#import request

# Create your views here.
def index(request):
	def address(query):
	    query = query.replace(' ','%20')
	    url = 'http://maps.googleapis.com/maps/api/geocode/json?address=' + query
	    json_obj = urlopen(url).read()
	    everything = json.loads(json_obj.decode('utf-8'))
	    latitude = (everything['results'][0]['geometry']['location']['lat'])
	    longitude = (everything['results'][0]['geometry']['location']['lng'])
	    return [str(latitude), str(longitude)]


	def weather(query):
	    api_key = 'ec65392a85759266d8e5c851fb6f5f34'
	    latitude = query[0]
	    longitude = query[1]
	    date = query[2]
	    time = query[3]
	    time = time + ':00:00'
	    url = 'https://api.forecast.io/forecast/'+ api_key + '/' + latitude + ',' + longitude + ',' + str(date) + 'T' + time
	    req = Request(url, headers={'User-Agent' : "Magic Browser"})
	    json_obj = urlopen(req).read()
	    everything = json.loads(json_obj.decode('utf-8'))
	    return (everything['currently']['temperature'],everything['currently']['apparentTemperature'])

	everything = {}
	information =[]
	a=[]
	if request.POST:
		form = InfoForm(request.POST)
		print('posted?')
		if form.is_valid():
			print ('13')
			personalinfo_dict = form.cleaned_data
			address_destination = personalinfo_dict.get('address')
			day = personalinfo_dict.get('day')
			gender = personalinfo_dict.get('gender')
			time = personalinfo_dict.get('time')
			a = address(address_destination)
			a.append(day)
			a.append(time)
			output_data = weather(a)
			actual_temperature = output_data[0]
			feel_temperature = output_data[1]
			request.session["actual_t"] = actual_temperature
			request.session["feel_t"] = feel_temperature
			request.session["gender_t"] = gender
			request.session["time_h"] = time
			#return HttpResponseRedirect('result/')

			return result_page(request)
		else:
			print (form.errors)
	else:
		form = InfoForm()



	context_dict = {'form': form}
	return render(request, 'Bastra/index.html', context_dict)


def result_page(request):
	actual_temperature = request.session.get("actual_t")
	feel_temperature = request.session.get("feel_t")
	gender = request.session.get("gender_t")
	time = request.session["time_h"] 
	if gender == '1':
		gender = 'Male'
	elif gender =='2':
		gender = 'Female'

	feel = int(feel_temperature)
	if gender.lower() == 'male':
		if feel <= 32:
			pic_name = 'men_32_'
		elif feel <=50:
			pic_name = 'men_50_'
		elif feel <=70:
			pic_name = 'men_70_'
		elif feel <= 86:
			pic_name = 'men_86_'
		elif feel > 86:
			pic_name = 'men_87_'
	elif gender.lower() == 'female': 
		if feel <= 32:
			pic_name = 'women_32_'
		elif feel <=50:
			pic_name = 'women_50_'
		elif feel <=70:
			pic_name = 'women_70_'
		elif feel <= 86:
			pic_name = 'women_86_'
		elif feel > 86:
			pic_name = 'women_87_'
	if request.session.test_cookie_worked():
		print (">>>> TEST COOKIE WORKED!")
		request.session.delete_test_cookie()
	time = time + '00'
	pic_name_1 = pic_name + '1.jpg'
	pic_name_2 = pic_name + '2.jpg'
	pic_name_3 = pic_name + '3.jpg'
	mydict = {'actual': actual_temperature, 'feel': feel_temperature, 'gender': gender, 'pic_name1': pic_name_1, 'pic_name2': pic_name_2,'pic_name3': pic_name_3, 'time': time}
	return render(request, 'Bastra/clothes.html', mydict)

