from django.shortcuts import render_to_response
from libs.utils import RequiredGroup


@RequiredGroup('admuser_users')
def index(request):
    return render_to_response('layout.html')


def tab_dispatcher(request, **kw):
    return getattr(TabContainer, kw['tab'])(request)


class TabContainer:
    '''holds tab views'''

    @staticmethod
    @RequiredGroup('admuser_users')
    def add_user(request):
        return render_to_response('tabs/add_user.html')
