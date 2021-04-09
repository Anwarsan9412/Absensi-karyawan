from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from .forms import  EditProfileForm, PasswordChanginForm, UserUpdateForm,ProfileUpdateForm, SignUpForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView
from django.contrib import messages



from home.models import Profile


def profile(request):
    return render(request, 'registration/user_profile.html',{})

def profileUpdate(request):
   
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, ('Your profile was successfully updated!'))
            return redirect('members-profile')
        else:
            pass
            # messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
                
    return render(request, 'registration/upd_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


# class ShowProfilPageView(DetailView):
#     model = Profile
#     template_name = 'registration/user_profile.html'
    
#     def get_context_data(self, *args, **kwargs):
#         users = Profile.objects.all()
#         context = super(ShowProfilPageView, self).get_context_data(*args, **kwargs)
        
#         page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        
#         context["page_user"] = page_user
#         return context  
    
    

class PasswordsChangeView(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PasswordChanginForm
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('password-success')
    
def password_success(request):
    return render(request, 'registration/password_success.html',{})

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
    # def get_context_data(self, *args, **kwargs):
    #     u_form = EditProfileForm()
    #     p_form = ProfileUpdateForm()
    #     context = super(UserRegisterView, self).get_context_data(*args, **kwargs)
        
    # #     # page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        
    #     # context["page_user"] = page_user
    #     # context["u_form"] = u_form
    #     context["p_fform"] = p_form
    #     return context  
    
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'registration/register.html',{'form':form})
    