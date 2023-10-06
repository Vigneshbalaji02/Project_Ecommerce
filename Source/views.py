from django.shortcuts import render
from django.contrib import messages
from Source.form import CustomUserForm
from django.shortcuts import HttpResponse,HttpResponseRedirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
import json
def home(request):
    product=Product.objects.filter(Trending=1)
    return render(request,"home.html",{"product":product})
def collections(request):
    catagory=Catagory.objects.filter(Status=0)
    return render(request,"collections.html",{"catagory":catagory})
def view(request,Name):
    if(Catagory.objects.filter(Name=Name,Status=0)):
       product=Product.objects.filter(Catagory__Name=Name)
       return render(request,"products.html",{"product":product,"Catagory__Name":Name})
    else:
        messages.warning(request,"No Such Catagory Found")
        return render(request,"collections.html")
    
def product_details(request,cname,pname):
    if(Catagory.objects.filter(Name=cname,Status=0)):
        if(Product.objects.filter(Name=pname,Status=0)):
            product=Product.objects.filter(Name=pname,Status=0).first()
            return render(request,"productsdetails.html",{"product":product})
        else:
            messages.warning(request,"No Such Catagory Found")
            return render(request,"collections.html")

    else:
         messages.warning(request,"No Such Catagory Found")
         return render(request,"collections.html")
    
def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success You Can Login Now....!")
            return HttpResponseRedirect('/login')
    return render(request,"register.html",{"form":form})

def login_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(request,"home.html")
    else:
        if request.method=="POST":
            name=request.POST.get("username")
            pwd=request.POST.get("password")
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged In Succesddfully")
                return HttpResponseRedirect("/")
            else:
                messages.error(request,"Invalid User Name or Password")
                return HttpResponseRedirect("/login")
        return render(request,"login.html")
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out Successful")
        return HttpResponseRedirect("/")
    
def add_to_cart(request):
    if request.headers.get('X-Requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            Product_qty=(data['Product_qty'])
            Product_id=(data['pid'])
            product_status=Product.objects.get(id=Product_id)
            if product_status:
                if Cart.objects.filter(user=request.user.id,Product_id=Product_id):
                    return JsonResponse({'status':'Product Already in cart'},status=200)
                else:
                    if product_status.Quantity>=Product_qty:
                        Cart.objects.create(user=request.user,Product_id=Product_id,Product_qty=Product_qty)
                        return JsonResponse({'status':'Product Added to cart'},status=200)
                    else:
                        return JsonResponse({'status':'Stock Not Avaliable'},status=200)
    
        else:
            return JsonResponse({'status':"Login to Add Cart"}, status=200)
    else:
        return JsonResponse({'status':"Invalid Access"}, status=200)



def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request,"cart.html",{"cart":cart})
    else:
        return HttpResponseRedirect("/")
    
def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return HttpResponseRedirect("/cart")

def fav_page(request):
    if request.headers.get('X-Requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            Product_id=(data['pid'])
            product_status=Product.objects.get(id=Product_id)
            if product_status:
                if Favourite.objects.filter(user=request.user.id,Product_id=Product_id):
                    return JsonResponse({'status':"Product Already in Favourite"}, status=200)
                else:        
                    Favourite.objects.create(user=request.user,Product_id=Product_id)
                    return JsonResponse({'status':"Product Added to Favourite"}, status=200)
        else:
            return JsonResponse({'status':"Login to Add Favourite"}, status=200)
    else:
        return JsonResponse({'status':"Invalid Access"}, status=200)

def favviewpage(request):
    if request.user.is_authenticated:
        fav=Favourite.objects.filter(user=request.user)
        return render(request,"fav.html",{"fav":fav})
    else:
        return HttpResponseRedirect("/")
    
def remove_fav(request,rfav):
    faviteam=Favourite.objects.get(id=rfav)
    faviteam.delete()
    return HttpResponseRedirect("/favviewpage")