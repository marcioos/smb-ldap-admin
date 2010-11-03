from django.shortcuts import render_to_response
from libs.utils import RequiredGroup
   
@RequiredGroup('admuser_users')
def index(request):
    return render_to_response('layout.html')

@RequiredGroup('admuser_users')
def add_user(request):
    return render_to_response('add_user.html')

def action_dispatcher(request, **kw):
    return globals()[kw['action']](request)
