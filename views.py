from django.shortcuts import render, redirect
from AmazonParser.forms import SearchBarForm, DeleteHistoryForm
from utils.script import *
from AmazonParser.models import Product
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
class HomeViews(TemplateView):
    template_name='AmazonParser/home/home.html'
    template_if_valid='AmazonParser/selected_product.html'
    def get(self, request):
        form=SearchBarForm()
        arg={'form':form}
        return render(request, self.template_name, arg)

    def post(self, request):
        if request.method == 'POST':
            form = SearchBarForm(request.POST)
            if form.is_valid():
                url=form.cleaned_data['Rechercher']
                datas_to_save=Product(user=request.user, name=url_parser(url)[0], price=url_parser(url)[2], period=url_parser(url)[1])
                datas_to_save.save()
                #saved_datas=Product.objects.all()
                return render(request, self.template_if_valid, {'datas_to_save':Product.objects.all()})
        # if a GET (or any other method) we'll create a blank form
        else:
            form = SearchBarForm()
            args={'form':form}
            return render(request, self.template_name, args)
    
def signup(request):
    total_users=User.objects.all()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request, user)
            return redirect('/') 
                               
    else:
        form=UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form':form, 'user':total_users})

def HistoryViews(request):
    #data_to_delete=''
    researched_products=Product.objects.filter(user=request.user) 
    #print(Product.objects.count())
    if request.method == 'POST':
            form = DeleteHistoryForm(request.POST)
            print(form.errors)
            print(form.is_valid())
            if form.is_valid():        
                data_to_delete=form.cleaned_data['Products_to_delete']
                #print(data_to_delete)
                #test=Product.objects.filter(name=data_to_delete)
                '''for i in range(Product.objects.count()):
                    if Product.objects.filter(id=i)==data_to_delete:
                        Product.objects.filter(id=i).delete()'''
                return render(request, 'AmazonParser/history/history.html', {'form':Product.objects.all()})      
    else:
        form=DeleteHistoryForm()
    return render(request, 'AmazonParser/history/history.html', {'form':form})





            
