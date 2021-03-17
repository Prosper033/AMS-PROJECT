from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from AMSapp.service_provider import ams_service_provider


@login_required(redirect_field_name='next')
def profile_view(request):
    user_id = request.user.id
    account_holder = ams_service_provider.account_holder_management_service().get_details_by_user(user_id)

    context = {
        'account_holder': account_holder

    }
    return render(request, 'profile.html', context)
