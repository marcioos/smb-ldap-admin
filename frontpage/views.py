from django.template import RequestContext
from django.shortcuts import render_to_response
from libs.utils import RequiredGroup
from libs.Logger import debug


@RequiredGroup('admuser_users')
def index(request):
    return render_to_response('layout.html')


@RequiredGroup('admuser_creators')
def add_user(request):
    return Tabs.add_user(request)


def tab_dispatcher(request, **kw):
    return getattr(Tabs, kw['tab'])(request)


class Tabs:
    '''holds tab views'''

    @staticmethod
    @RequiredGroup('admuser_users')
    def add_user(request):
        ou_list = [(0, 'cpd'), (1, 'administrativo'), (2, 'diretoria')]
        context = RequestContext(
            request, 
            {'ou_list': ou_list}
        )
        return render_to_response('tabs/add_user.html', context)
