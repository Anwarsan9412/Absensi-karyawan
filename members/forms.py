from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from home.models import Profile
from phone_field import PhoneField



class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    # profile_image = forms.FileField() # add this field
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password1','password2',)
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
    
    
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_login = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    # is_superuser = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_staff = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_active = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # date_joined = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # date_joined = forms.Text(max_length=10)
    
    class Meta:
        model = User
        fields = ('username',  'email','last_name','first_name')
        

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email',]


class ProfileUpdateForm(forms.ModelForm):
    PILIHAN =  [
        ('pria','Pria'),
        ('wanita','Wanita'),
    ]
    STATUS =  [
        ('belum','Belum'),
        ('sudah','Sudah'),
    ]
    DIVISIS =  [
        ('accounting','Accounting'),
        ('edp','EDP'),
        ('ic','IC'),
        ('hrd','HRD'),
        ('ga','GA'),
        ('development','Development'),
        ('virtual','Virtual'),
        ('finance','Finanace'),
    ]
    JABATAN =  [
        ('Manager','Manager'),
        ('Supervisor','Supervisor'),
        ('Senior Clerk','Senior Clerk'),
        ('Clerk','Clerk'),
    ]
    
    jenis_kelamin = forms.CharField(widget=forms.Select(choices=PILIHAN,attrs={'class': 'form-control'}))
    status_nikah  = forms.CharField(widget=forms.Select(choices=STATUS,attrs={'class': 'form-control'}))
    alamat        = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    divisi        = forms.CharField(widget=forms.Select(choices=DIVISIS,attrs={'class': 'form-control'}))
    jabatan       = forms.CharField(widget=forms.Select(choices=JABATAN,attrs={'class': 'form-control'}))
    # profile_pic   = forms.FileField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # profile_pic   = forms.forms.CharFiel( null=True ,blank=True, upload_to="profile_pics", default='profil.png')
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Profile
        fields = ['divisi','jabatan','jenis_kelamin','status_nikah','alamat','phone','profile_pic']

                
                
        
class PasswordChanginForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control','type': 'password'}))
    new_password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control','type': 'password'}))
    
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
      
      
      
# class SignUpForm(UserCreationForm):
#     username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control','type': 'password'}))
#     password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control','type': 'password'}))
    
    
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email','password1','password2')
        