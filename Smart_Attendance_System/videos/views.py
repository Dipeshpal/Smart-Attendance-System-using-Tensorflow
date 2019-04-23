from django.shortcuts import render

def videos_page(request):
    return render(request, 'videos/videos_page.html')
