from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    if request.method == "POST":
        url = request.POST.get('url')
        # get the HTML of target site
        response = requests.get(url)
        if response.status_code == 200:
            return HttpResponse(HttpResponse("get data success!"))
        return HttpResponse(HttpResponse(f"URL submitted: {url} but fetch data error"))
    return render(request, 'form.html')