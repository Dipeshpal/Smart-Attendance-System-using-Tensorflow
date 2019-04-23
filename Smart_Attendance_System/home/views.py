from django.shortcuts import render, redirect
from . models import Home
from django.contrib.auth.decorators import login_required
from . import forms
from .forms import DeleteNewForm
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404


def homepage(request):
    homeblog_list = Home.objects.all().order_by('-date')
    # print("Type: ", type(homeblog_list))
    # Pagination
    # Show 10 Post Per Page
    paginator = Paginator(homeblog_list, 10)

    page = request.GET.get('page')
    homeblog = paginator.get_page(page)
    return render(request, 'home/home.html', {'articles': homeblog})


def article_detail(request, slug):
    article = Home.objects.get(slug=slug)
    return render(request, 'home/article_detail.html', {'article': article})


@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = forms.CreateArticle(request.POST, request.FILES)
            if form.is_valid():
                # save article to db
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect('home:list')
        else:
            form = forms.CreateArticle()
        return render(request, 'home/article_create.html', {'form': form})
    else:
        return render(request, 'home/not_valid_user.html')


@login_required(login_url="/accounts/login/")
def article_delete(request, slug):
    if request.user.is_staff:
        Home.objects.get(slug=slug).delete()
        return render(request, 'home/article_delete.html')
    else:
        return render(request, 'home/not_valid_user.html')


@login_required(login_url="/accounts/login/")
def article_update(request, slug):
    instance = Home.objects.get(slug=slug)
    if request.user.is_staff:
        form = forms.EditPostForm(instance=instance)
        args = {'form': form}
        # The line below cause delete previous post when do not save
        return render(request, 'home/article_edit.html', args)
    else:
        return render(request, 'home/not_valid_user.html')
