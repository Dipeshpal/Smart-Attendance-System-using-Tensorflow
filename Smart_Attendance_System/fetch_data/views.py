from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import trigger


@login_required(login_url="/accounts/login/")
def fetch_data(request):
    # return render(request, 'fetch_data/fetch_data.html')
    if request.POST:
        roll_no = request.POST['term']
        enrollment_no, name, total_days, total_present_days, percentage = trigger.start(roll_no)
        enrollment_no = str(enrollment_no)
        total_days = str(total_days)
        total_present_days = str(total_present_days)
        percentage = str(percentage)
        data = {'data': '1',
                'name': name,
                'enrollment_no': enrollment_no,
                'total_days': total_days,
                'total_present_days': total_present_days,
                'percentage': percentage,
               }
        return render(request, 'fetch_data/fetch_data_result.html', data)
    else:
        return render(request, 'fetch_data/fetch_data.html')



