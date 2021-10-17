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
        'count': [0, 1, 2],
    })


def pie_list(request):

    labels = []
    data = []

    queryset = City.objects.order_by('-population')
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)
    my_graphs = [
        {'name': '1', 'labels': labels, 'data': data},
        {'name': '2', 'labels': labels, 'data': data},
    ]
    context = {
        'graphs': my_graphs
    }

    return render(request, 'cities/chart_list.html', context=context)
