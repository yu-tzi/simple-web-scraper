from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests

# Create your views here.
def index(request):
    if request.method == "POST":
        url = request.POST.get('url')
        try:
            # get the HTML of target site
            response = requests.get(url)
            if response.status_code == 200:
                html = BeautifulSoup(response.text, 'html.parser')
                # get p element in the html
                contents = html.find_all('p')
                # convert p into text
                texts = [p.get_text() for p in contents]
                renderContent = '\n'.join(texts)
                return render(request, 'index.html', { 'renderContent': renderContent})
        except:
            # when sth go wrong
            return render(request, 'index.html', { 'renderContent': 'somthing went wrong :( \nplz try another url'})
    return render(request, 'index.html')