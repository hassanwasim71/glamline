from django.shortcuts import render
from django.http import HttpResponse
from .models import product,Contact,Orders,orderupdate,Blog
#from .filters import product
import json
# Create your views here.
def index(request):


    prod = product.objects.filter(category='carousel1')
    prod2 = product.objects.filter(category='newarrival')

    dic2={'allprods':prod,'prods':prod2}
    return render(request,'shop/index.html',dic2)

def productpage(request):
    if request.method == "POST":
        categ = request.POST.get('category', "")
        pric = request.POST.get('pricee', "")
        colr = request.POST.get('color', "")
        if pric=="htl" and categ != "Category" and colr != "Color":
            prod3 = product.objects.filter(types=categ)
            prod2 = prod3.filter(colour=colr)
            prod=prod2.order_by('-price')
            print(prod)
            dic = {'allprods': prod}
            return render(request, 'shop/shop.html', dic)
        elif pric=="lth" and categ != "Category" and colr != "Color":
            prod3 = product.objects.filter(types=categ)
            prod2 = prod3.filter(colour=colr)
            prod=prod2.order_by('price')
            print(prod)
            dic = {'allprods': prod}
            return render(request, 'shop/shop.html', dic)
        elif pric=="htl" and categ != "Category":
            prod3 = product.objects.filter(types=categ)

            prod=prod3.order_by('-price')
            print(prod)
            dic = {'allprods': prod}
            return render(request, 'shop/shop.html', dic)
        elif pric=="lth" and categ != "Category":
            prod3 = product.objects.filter(types=categ)
            prod=prod3.order_by('price')
            print(prod)
            dic = {'allprods': prod}
            return render(request, 'shop/shop.html', dic)
        elif categ != "Category" and colr != "Color":
            prod2 = product.objects.filter(types=categ)
            prod = prod2.filter(colour=colr)
            dic = {'allprods': prod}
            return render(request, 'shop/shop.html', dic)
        elif pric=="htl"  and colr != "Color":

            prod2 = product.objects.filter(colour=colr)
            prod=prod2.order_by('-price')
            print(prod)
            dic = {'allprods': prod}
            return render(request, 'shop/shop.html', dic)
        elif pric=="lth"  and colr != "Color":
            prod2 = product.objects.filter(colour=colr)
            prod=prod2.order_by('price')
            print(prod)
            dic = {'allprods': prod}
            return render(request, 'shop/shop.html', dic)
        elif colr != "Color":
            prod = product.objects.filter(colour=colr)
            dic = {'allprods': prod}
            return render(request, 'shop/shop.html', dic)
        elif categ != "Category" and colr=="Color":
            print(categ)
            prod = product.objects.filter(types='shirt')
            dic = {'allprods': prod}
            return render(request, 'shop/shop.html', dic)
        elif pric=="htl"  and colr == "Color":


            prod=product.objects.order_by('-price')
            print(prod)
            dic = {'allprods': prod}
            return render(request, 'shop/shop.html', dic)
        elif pric=="lth"  and colr == "Color":

            prod=product.objects.order_by('price')
            print(prod)
            dic = {'allprods': prod}
            return render(request, 'shop/shop.html', dic)
        else:
            prod = product.objects.filter(category='newarrival')

            # myFilter=productFilter()
            dic = {'allprods': prod}
            return render(request, 'shop/shop.html', dic)





    else:
        prod = product.objects.filter(category='newarrival')

        # myFilter=productFilter()
        dic = {'allprods': prod}
        return render(request, 'shop/shop.html', dic)


def contact(request):
    if request.method=="POST":
        print("selected")
        message = request.POST.get('message', "")
        name=request.POST.get('name',"")
        email=request.POST.get('email',"")
        subject=request.POST.get('subject',"")


        contact=Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
        thanks = True
        return render(request, 'shop/contact.html', {'thanks': thanks})
    return render(request,'shop/contact.html')

def about(request):
    return render(request,'shop/about.html')

def search(request):
    return render(request,'shop/index.html')

def prodview(request,myid):
    prod=product.objects.filter(id=myid)
    print(prod)
    return render(request,'shop/product_details.html',{'product':prod[0]})

def track(request):
    if request.method=="POST":
        orderid=request.POST.get('orderId',"")
        email=request.POST.get('email',"")

        try:
            order=Orders.objects.filter(order_id=orderid,cs_email=email)
            if len(order)>0:
                update=orderupdate.objects.filter(order_id=orderid)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response=json.dumps(updates,default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('')
        except Exception as e:
            return HttpResponse('')
    return render(request,'shop/tracker.html')

def checkout(request):
    if request.method=="POST":
        orderitems=request.POST.get('itemsJson',"")
        firstname=request.POST.get('firstName',"")
        lastname=request.POST.get('lastName',"")
        email=request.POST.get('email',"")
        address=request.POST.get('address',"")
        tel=request.POST.get('tel',"")

        country=request.POST.get('country',"")
        state=request.POST.get('state',"")
        zip_code=request.POST.get('zip',"")


        order=Orders(

        order_items =orderitems,
        cs_firstname =firstname,
        cs_lastname =lastname,
        cs_email =email,
        cs_address =address,
        cs_tel =tel,

        cs_country =country,
        cs_state =state,
        cs_zip =zip_code,

        )
        order.save()
        update=orderupdate(order_id=order.order_id,update_desc="the order has been placed")
        update.save()
        thanks=True
        return render(request, 'shop/checkout.html',{'thanks': thanks})
    return render(request,'shop/checkout.html')

def blog(request):
    if request.method == "POST":
        search1 = request.POST.get('search', "")
        prod = Blog.objects.filter(blog_name__contains=search1)
        dic = {'allprods': prod}
        return render(request, 'shop/blog.html', dic)
    else:
        prod = Blog.objects.all()
        dic = {'allprods': prod}
        return render(request,'shop/blog.html',dic)

def blogdet(request, myid):
    prod = Blog.objects.filter(id=myid)
    return render(request,'shop/blog_details.html', {'product': prod[0]})

def proddet(request, myid):
    prod = product.objects.filter(id=myid)
    print(prod)
    return render(request, 'shop/product_details.html', {'product': prod[0]})
