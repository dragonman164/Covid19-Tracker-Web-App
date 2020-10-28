from django.shortcuts import render
from django.http import HttpResponse
import requests,json,time

x = requests.get(url='https://api.covid19api.com/summary').text
y = json.loads(x)

def index(request):
    params = {'TotalConfirmed':y['Global']['TotalConfirmed'],
    'TotalDeaths':y['Global']['TotalDeaths'],
    'TotalRecovered':y['Global']['TotalRecovered']}
    return render(request,'index.html',params)

def table(request):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    params = {'ListofCountries':y['Countries'],'time':current_time}
    return render(request,'tables.html',params)

def details(request):
    curr_country = request.GET.get('country','default')
    for elem in y['Countries']:
        if elem['Country']==curr_country:
            x = elem
            break
    params = {'Country':x}
    return render(request,'details.html',params)

def graphs(request):
    return render(request,'graphs.html')

    
def about(request):
    return render(request,'abouts.html')