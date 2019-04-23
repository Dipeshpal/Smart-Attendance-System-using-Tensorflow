from django.shortcuts import render, redirect
from django.contrib.auth import login, update_session_auth_hash
from . forms import RegistrationForm, EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            login(request, user)
            return redirect('home:list')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def profile_view(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile/')
        else:
            return redirect('/accounts/change_password/')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


@login_required
def apply(request):
    return render(request, 'accounts/apply.html')