from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import trigger


@login_required(login_url="/accounts/login/")
def face_recognition(request):
    # return render(request, 'face_recognition/face_recognition.html')
    if request.user.is_staff:
        return render(request, 'face_recognition/face_recognition.html')
    else:
        return render(request, 'face_recognition/not_valid_user.html')


@login_required(login_url="/accounts/login/")
def training(request):
    # return render(request, 'face_recognition/face_recognition.html')
    if request.user.is_staff:
        trigger.start()
        return render(request, 'face_recognition/training.html')
    else:
        return render(request, 'face_recognition/not_valid_user.html')

