from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.template import loader
from time import time, ctime
from .models import Member
from dj_project.signals import my_sygnal

class MemberView(View):
    def get(self, request):
        now = ctime(time())
        my_sygnal.send(self.__class__, now=now)
        template = loader.get_template('get.html')
        context = {
            'time': now
		}        
        return HttpResponse(template.render(context, request))
