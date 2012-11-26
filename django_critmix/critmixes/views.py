from critmixes.models import Critmix
from django.shortcuts import render_to_response, get_object_or_404
import soundcloud

client = soundcloud.Client(client_id='4d9fea6bff39bf127b10e87a2f478aea')

def index(request):
    latest_critmix_list = Critmix.objects.all()
    return render_to_response('critmixes/index.html', {'latest_critmix_list': latest_critmix_list})

def detail(request, critmix_id):
    p = get_object_or_404(Critmix, pk=critmix_id)
    #print "p is", p
    # get a tracks oembed data
    #track_url = 'http://soundcloud.com/forss/flickermood'
    embed_info = client.get('/oembed', url=p)

    # print the html for the player widget
    #print embed_info.html

    return render_to_response('critmixes/detail.html', {'critmix': p, 'embed_info': embed_info.html})

def results(request, critmix_id):
    return HttpResponse("You're looking at the results of critmix %s." % critmix_id)

def vote(request, critmix_id):
    return HttpResponse("You're voting on critmix %s." % critmix_id)
