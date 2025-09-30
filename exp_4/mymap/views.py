from django.shortcuts import render

def map(request):
    return  render(request,"map.HTML")

def mangal(request):
    return render(request, "mangal.html")
def hotbreads(request):
    return render(request, "hotbreads.html")
def marriage(request):
    return render(request, "marriage.html")
def tskrishna(request):
    return render(request, "tskrishna.html")
def aadhar(request):
    return render(request, "aadhar.html")


# Create your views here.

