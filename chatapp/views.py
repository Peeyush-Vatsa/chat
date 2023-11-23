from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Message

# Create your views here.
def index(request):
    if request.method == 'GET':
        if not request.session.get('name'):
            return redirect('auth')
        messages = Message.objects.all().order_by('-timestamp')[:20]
        messages = reversed(messages)
        return render(request, 'chatapp/index.html', {'messages': messages, 'name': request.session['name']})
    else:
        return HttpResponse("Invalid request")

def auth(request):
    if request.method == 'GET':
        return render(request, 'chatapp/auth.html')
    elif request.method == 'POST':
        name = request.POST['name']
        request.session['name'] = name
        return redirect('index')