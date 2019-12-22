from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import FormView

from apps.retirees.forms import RetiredForm, SearchRetiredForm
from apps.retirees.models import Retired


class Retireds(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = SearchRetiredForm()
        retireds = Retired.objects.all()

        return render(
            request,
            'retirees/retired.html',
            {'retireds': retireds, 'form': form}
        )

    def post(self, request, *args, **kwargs):
        form = SearchRetiredForm(request.POST)

        if form.is_valid():
            search = form.cleaned_data.get('search')
            retireds = Retired.objects.filter(
                Q(first_name__icontains=search)
                | Q(last_name__icontains=search)
            )
        else:
            retireds = Retired.objects.all()

        return render(
            request,
            'retirees/retired.html',
            {'retireds': retireds, 'form': form}
        )


@user_passes_test(lambda user: user.is_superuser)
def add_retired(request):
    if request.method == 'GET':
        form = RetiredForm()

    if request.method == 'POST':
        form = RetiredForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('retireds')

    return render(
        request,
        'retirees/add_retired.html',
        {'form': form}
    )


class CreateUser(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = '/'


def create_user(request):
    if request.method == 'GET':
        form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('retireds')

    return render(
        request,
        'registration/register.html',
        {'form': form}
    )
