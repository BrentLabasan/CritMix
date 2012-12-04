from critmixes.models import Critmix
from django.shortcuts import render_to_response, get_object_or_404
import soundcloud
# create a client object with your app credentials
client = soundcloud.Client(client_id='4d9fea6bff39bf127b10e87a2f478aea')
from django.utils.safestring import mark_safe
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    latest_critmix_list = Critmix.objects.all()
    return render_to_response('critmixes/index.html', {'latest_critmix_list': latest_critmix_list})

def detail(request, critmix_id):
    p = get_object_or_404(Critmix, pk=critmix_id)
    # get a tracks oembed data
    track_url = p.mix_url
    print "meow", p.jsonData
    meow = "b12a"
    embed_info = client.get('/oembed', url=track_url, show_comments='false')
    # print the html for the player widget
    print embed_info.html
    track = client.get('/resolve', url=track_url)
    print 'duration', track.duration
    return render_to_response('critmixes/detail.html', {'critmix': p, 'embed_info': embed_info.html, 'duration': track.duration, 'jsonData': p.jsonData})

def results(request, critmix_id):
    return HttpResponse("You're looking at the results of critmix %s." % critmix_id)

def vote(request, critmix_id):
    return HttpResponse("You're voting on critmix %s." % critmix_id)

def savecrits(request):
    results = {'success':False}
    if request.method == u'GET':
        GET = request.GET
        if GET.has_key(u'pk') and GET.has_key(u'jsonData'):
            pk = int(GET[u'pk'])
            txt = GET[u'jsonData']
            critmix = Critmix.objects.get(pk=pk)
            critmix.jsonData = txt
            critmix.save()
            print "HIYOOOOOOO"
            #print critmix.jsonData
            results = {'success':True}
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')