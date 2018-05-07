from django.shortcuts import render

# Create your views here.

from djang.http import HttpResponse
def test(request, *args, **kwargs):
    return HttpResponse('Okk')
