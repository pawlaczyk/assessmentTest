"""AssessmentTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

# one_step - na razie opuszaczamy weryfikację email
from django_registration.backends.one_step.views import RegistrationView

from core.views import IndexTemplateView
from users.forms import CustomUserForm

#do rejestracji po emailu
#https://django-registration.readthedocs.io/en/3.0/activation-workflow.html

urlpatterns = [
    path('admin/', admin.site.urls),

    # custom version of registration provided by django
    path("accounts/register",
        RegistrationView.as_view(
            form_class=CustomUserForm,
            success_url="/",
        ), name="django_registration_register"),
    
    path("accounts/",
        include("django_registration.backends.one_step.urls")),

    # login urls provided by django
    path("accounts/",
        include("django.contrib.auth.urls")),
    
    # urle z aplikacji `users`
    path("api/",
        include("users.api.urls")),
    
    # login url for the browser API
    path("api-auth/",
        include("rest_framework.urls")),

    # login enpoints to use by rest
    path("api/rest-auth/",
        include("rest_auth.urls")),

    # registration endpoint to use via rest
    path("api/rest-auth/registration",
        include("rest_auth.registration.urls")),

    # wszystkie inne adresy
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")
]
