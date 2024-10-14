from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import requests
# Create your views here.

def index(request):
    return render(request, 'index.html')

def search(request):
    if request.method == 'POST':
        search = request.POST['search'] 
        url = 'https://www.bing.com/search?q='+search
        res = requests.get(url)
        soup = bs(res.text, 'lxml') 
        result_listings = soup.find_all('li',class_='b_algo')
        search_results = []
        
        for result in result_listings:
            heading_tag = result.find('h2').text 
            link = result.find('a').get('href')
            body = result.find('p').text
            
            search_results.append((heading_tag, link,body))
            print(body)
        
        context = {
            'search_results':search_results
        }
        return render(request, 'search.html', context)
    return render(request, 'search.html',)