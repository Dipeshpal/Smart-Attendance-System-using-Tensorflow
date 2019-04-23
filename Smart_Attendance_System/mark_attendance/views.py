from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from . import trigger


@login_required(login_url="/accounts/login/")
def mark_attendance(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = forms.UploadFile(request.POST, request.FILES)
            if form.is_valid():
                # save article to db
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                print("Calling Check Image -")
                trigger.start2()
                return render(request, 'mark_attendance/success.html')
        else:
            form = forms.UploadFile()
        return render(request, 'mark_attendance/mark_attendance.html', {'form': form})
    else:
        return render(request, 'mark_attendance/not_valid_user.html')


@login_required(login_url="/accounts/login/")
def mark_attendance_success(request):
    return render(request, 'mark_attendance/success.html')


@login_required(login_url="/accounts/login/")
def camera_attendance(request):
    # trigger.start_camera_attendance()
    trigger.start()
    return render(request, 'mark_attendance/success.html')
