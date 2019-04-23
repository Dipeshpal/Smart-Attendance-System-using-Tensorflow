from django.shortcuts import render


def contact_us(request):
    return render(request, 'contact_us/contact_us.html')
