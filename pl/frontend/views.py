from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'frontend/page1.html',{'today':datetime.today()})

#only will be available if the admin is logged in...unless will show some errors
@login_required(login_url='/admin')#login_url will take the user to that specific page if not logged in
def authorize(request):
    return render (request,'frontend/authorize.html',{})