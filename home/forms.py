from django import forms
from .models import Post, Category
from django.forms import ModelChoiceField

choices = Category.objects.all().values_list('name','name')


choice_list = []

for choice in choices:
    choice_list.append(choice)    
   

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','category','body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Input Title'}),
            # 'author': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Input Title', 'value': '', 'id':'aut','type':'hidden' }),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'','id':'anwar', 'type':'hidden'}),
            'category': forms.Select(choices=choice_list ,attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            # 'updated': forms.DateField(attrs={'class':'form-control'}),
            # 'publish': forms.DateTimeField(attrs={'class':'form-control'}),
            
        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'value':'Input Title'}),
            # 'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            # 'updated': forms.DateField(attrs={'class':'form-control'}),
            # 'publish': forms.DateTimeField(attrs={'class':'form-control'}),
            
        }
        

