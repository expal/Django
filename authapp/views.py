from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

from authapp.models import User


class CustomLoginView(TemplateView):
    template_name = 'authapp/login.html'
    extra_context = {
        'title': 'Авторизация'

    }


class CustomRegisterView(TemplateView):
    template_name = "authapp/register.html"
    extra_context = {
        'title': 'Регистрация'

    }

    def post(self, request, *args, **kwargs):
        try:
            if all(
                    (
                            request.POST.get('username'),
                            request.POST.get('email'),
                            request.POST.get('password1'),
                            request.POST.get('password2'),
                            request.POST.get('first_name'),
                            request.POST.get('last_name'),
                            request.POST.get('password1') == request.POST.get('password2'),

                    )
            ):
                new_user = User.objects.create(
                    username=request.POST.get('username'),
                    email=request.POST.get('email'),
                    first_name=request.POST.get('first_name'),
                    last_name=request.POST.get('last_name'),
                    age=request.POST.get('age') if request.POST.get('age') else 0,
                    avatar=request.POST.get('avatar')

                )
                new_user.set_password(request.POST.get('password1'))
                new_user.save()
                messages.add_message(request, messages.INFO, 'Пользователь зарегистрирован')
                return HttpResponseRedirect(reverse('authapp:login'))
            else:
                messages.add_message(
                    request,
                    messages.WARNING,
                    'Something wrong'
                )
                return HttpResponseRedirect(reverse('authapp:register'))
        except Exception as ex:
            messages.add_message(
                request,
                messages.WARNING,
                'Something wrong'
            )
            return HttpResponseRedirect(reverse('authapp:register'))


class CustomLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.INFO, _("See you later!"))
        return super().dispatch(request, *args, **kwargs)


class CustomEditView(TemplateView):
    template_name = 'authapp/edit.html'

    extra_context = {
        'title': "Edit profile"
    }

    def post(self, request, *args, **kwargs):
        if request.POST.get('username'):
            request.user.username = request.POST.get('username')

        if request.POST.get('first_name'):
            request.user.username = request.POST.get('first_name')

        if request.POST.get('last_name'):
            request.user.username = request.POST.get('last_name')

        if request.POST.get('age'):
            request.user.username = request.POST.get('age')

        if request.POST.get('email'):
            request.user.username = request.POST.get('email')

        if request.POST.get('password'):
            request.user.set_password(request.POST.get('password'))

        request.user.save()
        return HttpResponseRedirect(reverse('authapp:edit'))
