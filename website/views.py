from django.shortcuts import render
from website.models import ParsedData
from website.utils import parse_website

def parse_and_display(request):
    website_url = 'https://cinematica.kg'
    parse_website(website_url)
    parsed_data = ParsedData.objects.all()

    return render(request, 'myapp/display_data.html', {'parsed_data': parsed_data})

