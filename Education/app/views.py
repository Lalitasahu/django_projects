from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')
