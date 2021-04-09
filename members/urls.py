from django.urls import path
from .views import PasswordsChangeView,UserRegisterView
from django.contrib.auth import views as auth_views
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/',UserRegisterView.as_view(), name='members-register'),
    # path('register/',views.register, name='members-register'),
    # path('edit_profile/',UserEditView.as_view(), name='edit-profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success', views.password_success, name='password-success'),
    # path('<int:pk>/profile/', ShowProfilPageView.as_view(), name='members-profile'),
    path('profile/', views.profile, name='members-profile'),
    path('edit_profile/', views.profileUpdate, name='edit-profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    