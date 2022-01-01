from django import views
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic.base import RedirectView, TemplateView
from .forms import StudentsRegistration
from django.http import HttpResponse
from .models import User
from django.views import View

# Create your views here.
class home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentsRegistration()
        stud = User.objects.all()
        context = {'std': stud, 'form':fm}
        return context
    
    def post(self, request):
        fm = StudentsRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            pss = fm.cleaned_data['password']
            reg = User(name=name, email=email, password=pss)

            reg.save()
            fm = StudentsRegistration()
            return HttpResponseRedirect('/')


class delete(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        uid = kwargs['uid']
        User.objects.get(pk=uid).delete()
        return super().get_redirect_url(*args, **kwargs)


class update(View):
    def get(self, request, uid):
        dt = User.objects.get(pk=uid)
        fm = StudentsRegistration(instance=dt)
        return render(request, 'update.html', {'form':fm})
    
    def post(self, request, uid):
        dt = User.objects.get(pk=uid)
        fm = StudentsRegistration(request.POST, instance=dt)
        if fm.is_valid():
            fm.save()
        return redirect('home')        

