from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "profile.html"

    def get_object(self):
        return self.request.user.profile
    
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ["bio", "location", "website"]
    template_name = "profile_edit.html"
    success_url = reverse_lazy("profile")
    
    def get_object(self):
        return self.request.user.profile