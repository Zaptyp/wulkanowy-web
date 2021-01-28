from django.shortcuts import render
from django.shortcuts import redirect

def default_view(request, *args, **kwargs):
    request.session['has_session'] = True
    return render(request, 'frontend/index.html')

def content_view(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        return render(request, 'frontend/content.html')
    else:
        return redirect('../')

def account_manager_view(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        return render(request, 'frontend/account-manager.html')
    else:
        return redirect('../')