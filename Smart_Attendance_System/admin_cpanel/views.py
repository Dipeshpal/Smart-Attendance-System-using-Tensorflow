from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms


@login_required(login_url="/accounts/login/")
def admin_cpanel(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = forms.UploadFile(request.POST, request.FILES)
            if form.is_valid():
                # save article to db
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect('face_recognition:face_recognition')
        else:
            form = forms.UploadFile()
        return render(request, 'admin_cpanel/admin_cpanel.html', {'form': form})
    else:
        return render(request, 'admin_cpanel/not_valid_user.html')
