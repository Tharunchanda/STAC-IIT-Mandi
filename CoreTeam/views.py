from django.shortcuts import render
from .models import MemberDetail

# Create your views here.

def CoreTeam(request):
    members = MemberDetail.objects.all()
    return render(request, 'coreTeam.html', {'team_member': members})

def moreInfo(request):
    return render(request, 'website/moreInfo.html')