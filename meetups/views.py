from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('Hello world')
    meetups = [
        { 'title': 'A first meetup' },
        { 'title': 'A second meetup' }
    ]
    return render(request, 'meetups/index.html', {
        'show': True,
        'meetups': meetups
    })