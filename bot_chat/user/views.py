from django.shortcuts import render
from django.http import HttpResponse
from user.models import *
def index(request):
    # Web page to view user wise count
    rst_user = list(UserDetails.objects.values('vchr_user_name','int_count'))
    context ={"users":rst_user}
    return render(request,"index.html",context)
