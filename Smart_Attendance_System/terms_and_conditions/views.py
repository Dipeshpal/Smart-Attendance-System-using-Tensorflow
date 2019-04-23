from django.shortcuts import render


def terms_and_conditions(request):
    return render(request, 'terms_and_conditions/terms_and_conditions.html')
