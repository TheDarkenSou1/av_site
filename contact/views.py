from django.shortcuts import render, redirect
from .models import UserContact
from django.contrib.auth.decorators import login_required, user_passes_test
from manager.views import is_manager


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def contact_list(request):
    contacts = UserContact.objects.filter(is_processed=False)
    return render(request, 'contact_list.html', context={'contact_list': contacts})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def contact_close(request, pk):
    UserContact.objects.filter(pk=pk).update(is_processed=True)
    return redirect('contact_list')
