from critmixes.models import Critmix
from django.shortcuts import render_to_response, get_object_or_404
import soundcloud
# create a client object with your app credentials
client = soundcloud.Client(client_id='4d9fea6bff39bf127b10e87a2f478aea')
from django.utils.safestring import mark_safe
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson

def home(request):
    #latest_critmix_list = Critmix.objects.all()
    return render_to_response('site/index.html')

def about(request):
    #latest_critmix_list = Critmix.objects.all()
    return render_to_response('site/about.html')

def getasongcritiqued(request):
    #latest_critmix_list = Critmix.objects.all()
    return render_to_response('site/getasongcritiqued.html')
    