from django.shortcuts import render
from .models import City, Country
# Create your views here.


def pie_chart(request):
    labels = []
    data = []

    queryset = City.objects.order_by('-population')
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)

    return render(request, 'cities/pie_chart.html', {
        'labels': labels,
        'data': data,
    })
