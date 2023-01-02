from django.shortcuts import render

# Create your views here.
def if_elif(request):
    d={'a':12,'b':40,'c':10}
    return render(request,'if_elif.html',d)