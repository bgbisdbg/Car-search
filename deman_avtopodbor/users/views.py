from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from common.views import TitleMixin
from users.forms import UserLoginForm, UserRegistrationForm


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = "Авторизация"





class UserRegistrationView(TitleMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    title = 'Регистрация'

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)  # Перенаправляем на страницу авторизации