#!/usr/bin/python

# $Id: recorder.wsgi.default 2882 2009-12-09 00:30:45Z marlon $

import os, sys

baseDir = '/home/marcio/codes/admuser';

### SET PATH HERE ###

sys.path.insert(0, baseDir)
sys.path.insert(1, baseDir + '/..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
