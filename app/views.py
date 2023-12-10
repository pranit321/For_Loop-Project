from django.shortcuts import render

# Create your views here.

def for_loop(request):
    d ={'name' : 'PRANIT'}
    return render(request,'forloop.html',d)