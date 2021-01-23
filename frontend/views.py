from django.shortcuts import render
from django.shortcuts import redirect

def default_view(request, *args, **kwargs):
    return render(request, 'frontend/index.html')

def content_view(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        return render(request, 'frontend/content.html')
    else:
        return redirect('../')