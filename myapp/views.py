from django.shortcuts import render,redirect
from django import forms
from django.views.generic import View
from myapp.models import Jobportal

# Create your views here.

class Jobform(forms.Form):
    username=forms.CharField()
    qualification=forms.CharField()
    age=forms.IntegerField()
    experience=forms.CharField()
    currenlty_working=forms.BooleanField()


class CreateJobportalView(View):
    def get(self,request,*args,**kwargs):
        form=Jobform()
        return render(request,"job-add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=Jobform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Jobportal.objects.create(**form.cleaned_data)
        # return render(request,"job-add.html",{"form":form})
        return redirect("jobadd")
    
class ListJobportalView(View):
    def get(self,request,*args,**kwargs):
        jobs=Jobportal.objects.all()
        return render(request,"job-list.html",{"jobs":jobs})

    
class jobDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Jobportal.objects.get(id=id)
        return render(request,"job-detail.html",{"job":qs})
    
class JobDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Jobportal.objects.get(id=id).delete()
        return redirect("joblist")
    
class JobUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Jobportal.objects.filter(id=id).update(currently_working=True)
        return redirect("joblist")
    

















