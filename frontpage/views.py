from django.shortcuts import render_to_response
from libs.utils import RequiredGroup
   
@RequiredGroup('admuser_users')
def index(request):
    return render_to_response('layout.html')
