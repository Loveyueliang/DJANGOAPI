import requests
from django.shortcuts import HttpResponseRedirect, HttpResponsePermanentRedirect


# Create your views here.
def get_bing_wallpaper(request, ):
    bing_url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    res = requests.get(bing_url).json()
    bing_wallpaper_url = "https://cn.bing.com" + res['images'][0]['url']
    return HttpResponsePermanentRedirect(bing_wallpaper_url)
