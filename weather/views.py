from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        raw_data = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=519b6615a2d88c800b2359ccdefd3609').read()
        json_data = json.loads(raw_data)
        data = {
            'city': city,
            'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp']),
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),
        }

        return render(request, 'index.html', data)

    else:
        return render(request, 'index.html')