from django.shortcuts import render, redirect
from .models import UserReservation
from django.contrib.auth.decorators import login_required, user_passes_test


def is_manager(user):
    return user.groups.filter(name='manager').exists()


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def reservation_list(request):
    reservations = UserReservation.objects.filter(is_processed=False)
    return render(request, 'reserve_list.html', context={'reserve_list': reservations})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def reservation_close(request, pk):
    UserReservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:reservation_list')
