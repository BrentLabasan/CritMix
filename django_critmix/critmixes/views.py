from critmixes.models import Critmix
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    latest_critmix_list = Critmix.objects.all()
    return render_to_response('critmixes/index.html', {'latest_critmix_list': latest_critmix_list})

def detail(request, critmix_id):
    p = get_object_or_404(Critmix, pk=critmix_id)
    return render_to_response('critmixes/detail.html', {'critmix': p})

def results(request, critmix_id):
    return HttpResponse("You're looking at the results of critmix %s." % critmix_id)

def vote(request, critmix_id):
    return HttpResponse("You're voting on critmix %s." % critmix_id)
