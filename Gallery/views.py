from django.shortcuts import render

# Create your views here.
def Gallery(request):
    return render(request, 'layout.html')