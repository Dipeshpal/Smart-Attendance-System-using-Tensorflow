from django.shortcuts import render

def disclaimer(request):
    return render(request, 'disclaimer/disclaimer.html')
