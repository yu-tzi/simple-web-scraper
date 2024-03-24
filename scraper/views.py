from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests

# Create your views here.
def index(request):
    if request.method == "POST":
        url = request.POST.get('url')
        # get the HTML of target site
        response = requests.get(url)
        if response.status_code == 200:
            html = BeautifulSoup(response.text, 'html.parser')
            # get p element in the html
            contents = html.find_all('p')
            # convert p into text
            texts = [p.get_text() for p in contents]
            renderContent = '<br>'.join(texts)
            return HttpResponse(f"Scraped text: {renderContent}")
        return HttpResponse(HttpResponse(f"URL submitted: {url} but fetch data error"))
    return render(request, 'form.html')