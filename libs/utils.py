class RequiredGroup(object):
    '''decorator to make the permission check inside any view'''

    def __init__(self, required_group):
        self.required_group = required_group

    def __call__(self, view):
        def wrapped_view(request):
            if 'REMOTE_USER' in request.META.keys():
                if request.META['REMOTE_USER'] in self.required_group:
                    return view(request)
                else:
                    return False
            else:
                return view(request)
        return wrapped_view
