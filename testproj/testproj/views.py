from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext
from models import *
from model_forms import *
from django.utils import simplejson
import json
from django.shortcuts import render_to_response

def create_group(request):
    if request.method == 'POST':
        form = BaseGroupForm(request.POST)
        if form.is_valid():
            mygroup = MyGroup()
            mygroup.name = form.cleaned_data['name']
            mygroup.save()
            return HttpResponse(json.dumps({'result': 'group_created'}))
        else:
            return render_to_response("group.html", {'form': form},
                                      RequestContext(request))
    else:
        mygroup = MyGroup()
        form = BaseGroupForm(instance=mygroup)
        return render_to_response("group.html", {'form': form},
                                  RequestContext(request))

def create_new(request):
    group = MyGroup.objects.get(pk='1')
    if group is None:
        raise Http404
    if request.method == 'POST':
        form = BaseModelForm(request.POST)
        if form.is_valid():
            mymodel = MyModel()
            mymodel.my_id = form.cleaned_data['my_id']
            mymodel.name  = form.cleaned_data['name']
            mymodel.group = group
            mymodel.save()
            return HttpResponse(json.dumps(
                                  {'result': 'valid', 
                                   'errors': str(form._errors)})
                               )
        else:
            return HttpResponse(json.dumps(
                                  {'result': 'invalid', 
                                   'errors': str(form._errors)})
                               )
    else:
        form = BaseModelForm()
        return render_to_response("home.html", {'form': form},
                                  RequestContext(request))
