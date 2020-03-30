from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
# Create your views here.
def Login(request):
    
    return render(request,'core/index.html')