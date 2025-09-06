from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

def home_page(request):
    return render(request,'home.html')

'''def about_page(request):
    context = {
        "info": "Welcome to Akshay's Profile page.",
    }
    return render(request,'pages/about.html',context)'''

class AboutPageView(TemplateView):  
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context["info"] = "Akshay's Vlog"
        return context