from django.shortcuts import render
from django.http import HttpResponse

def index(request, poll_id=None):
    return render(request, 'polls/index.html', {'name': 'UDE y Qwerty', 'poll_id': poll_id, 'show_short': True, 'query_param': request.GET.get('query')})