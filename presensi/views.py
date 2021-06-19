from os import pardir
from django import http
from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from home.models import Post, Category, MenuPresensi, MasterPresensi, Profile
from django.views.generic import CreateView
from django.views import View
from crequest.middleware import CrequestMiddleware
from django.contrib import messages
from home.forms import PresensiForm
import datetime
from django.urls import reverse_lazy

from django.views.generic.base import TemplateView
from django.core.paginator import Paginator


def absens(request):
    
    return render(request, 'presensi/absen_hadir.html', {})
 
    

def CatPresensiView(request, cats):
    # https://stackoverflow.com/questions/37104604/adding-a-django-model-instance-without-a-form-button-only
    current_request = CrequestMiddleware.get_request()
    user = current_request.user.id
    userr = str(current_request.user.username)
    profiles = Profile.objects.get(user_id=user)
    
    # presensi = MasterPresensi.objects.get(namaa_id=user)
        
    category_posts = MenuPresensi.objects.filter(name=cats)
    categor = MenuPresensi.objects.get(slug__iexact=cats)
    linkk = MenuPresensi.objects.values("slug").distinct()
    
    masterPresensi = MasterPresensi.objects.filter(namaa_id=user)
    
    # createPresensi = MasterPresensi.objects.create()
    # createPresensi.save()
    now = datetime.datetime.now().strftime('%H:%M:%S')
    now1 = datetime.datetime.now().date()
        
    if request.method == 'POST':
        exis = MasterPresensi.objects.filter(namaa_id=request.user, tanggal=f'{now1}').exists()
        if exis:
            nul = MasterPresensi.objects.filter(namaa_id=request.user,tanggal=f'{now1}',jam_pulang=None)
            if nul:
                obj = MasterPresensi.objects.filter(namaa_id=request.user,tanggal=f'{now1}').update(jam_pulang=f'{now}')
                return HttpResponseRedirect('/presensi/data-kehadiran/')
        else:
            obj = MasterPresensi.objects.create(namaa_id=request.user, tanggal=f'{now1}')
            obj.save()
            return HttpResponseRedirect('/presensi/data-kehadiran/')
        
            
            
    p = Paginator(MasterPresensi.objects.filter(namaa_id=request.user),5)
    page = request.GET.get('page')
    presensi_list = p.get_page(page)
    nums = "a" * presensi_list.paginator.num_pages
    

    context = {
        'heading' : '',
        'cats': cats.title(),
        'category_posts': category_posts,
        'linkk':linkk,
        'categor':categor,
        'presensi' : masterPresensi,
        'presensi_list': presensi_list,
        'nums' : nums
        
    }
    if request.method == 'POST':
        context['heading'] = 'ABSEN BERHASIL'
        
    if cats == 'data-kehadiran':      
        return render(request, 'presensi/data_kehadiran.html', context)
    else:
        return render(request, 'presensi/absen_hadir.html', context)
       
    

class AddAbsenView(TemplateView):
    template_name = 'presensi/data_kehadiran.html'
    
    def get_context_data(self):
        context = {
        'heading': 'Presensi'
        }
        return context
        
    
class AddAbsen(View):
    now = datetime.datetime.now().strftime('%H:%M:%S')
    now1 = datetime.datetime.now().date()
    now = datetime.datetime.now().strftime('%H:%M:%S')
    now1 = datetime.datetime.now().date()
        
    
    template_name = 'presensi/modal.html'
    context = {
        'heading': 'Presensi'
        }
            
    def post(self, request):
        obj = MasterPresensi.objects.create(namaa_id=request.user, tanggal=f'{self.now1}')
        obj.save()
        # if request.method == 'POST':
        #     exis = MasterPresensi.objects.filter(namaa_id=request.user, tanggal=f'{self.now1}').exists()
  
        #     if exis:
        #         nul = MasterPresensi.objects.filter(namaa_id=request.user,tanggal=f'{self.now1}',jam_pulang=None)
        #         if nul:
        #             obj = MasterPresensi.objects.filter(namaa_id=request.user,tanggal=f'{self.now1}').update(jam_pulang=f'{now}')
        #     else:
        #         obj = MasterPresensi.objects.create(namaa_id=request.user, tanggal=f'{self.now1}')
        #         obj.save()
        
        
        self.context['Heading'] = 'Absen Berhasil'
        return render(request, self.template_name, self.context)
        


    
    