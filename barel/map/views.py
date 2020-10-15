from django.shortcuts import render


def default_map(request):
    mapbox_access_token = "pk.eyJ1Ijoia2hhbjc0NSIsImEiOiJjam4wcjFtczcxYWVnM2xsbGg2ZndmdHY5In0.nZavo8g8QcIlR4Pf4s4qjg"
    return render(request, 'default.html',
                  {'mapbox_access_token': mapbox_access_token})
