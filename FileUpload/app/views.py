"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import *
from FileUpload import settings
import os

def files(request):
    files = File.objects.all()
    return render_to_response('app/files.html', 
                              context_instance = RequestContext(request,  { 'files' : files }))

def add(request):
    if request.method == "GET":
        form = FileForm()
        return render(request, 'app/addFile.html', { 'form' : form })
    elif request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect('/files')

def deleteFile(request, i):
    file = File.objects.get(id = i)
    file.delete()
    os.remove(settings.MEDIA_ROOT + file.upload.name)

    return HttpResponseRedirect('/files')

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'year':datetime.now().year,
        })
    )
