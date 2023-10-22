from django.shortcuts import render,HttpResponse,redirect
from ecom.models import Destinations,Details,Booking,BookingForm
from .models import UserForm,LoginForm
from django.contrib import messages as msg
from django.contrib.auth import login,logout,authenticate 
from django.contrib.auth.models import User
   




# Create your views here.
def home(request):
    dest=Destinations.objects.all()
    d={'dest':dest}

    return render(request,'base.html',d)
def about(request):
    return render(request,'about1.html') 

def register(request):
    if request.method=='POST':
        obj=UserForm(request.POST)
        obj.save()
        msg.success(request, "Login Successfull")
        return redirect("/")
    else:
        d={'forms':UserForm}  
        return render(request,'forms.html',d)  

def loginn(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        pswd=request.POST.get("pswd")
        user=authenticate(request,username=uname,password=pswd)
        if user is not None:
            request.session["id"]=user.id
            print(request.session.get("id"))
            login(request,user)
            # if 'q' in request.GET:
            #     q=request.GET['q']
            #     print(q)
            #     obj=Destinations.objects.filter(name__icontains=q)
        
            obj=Destinations.objects.all()
            print(obj)
            d={'dest':obj}

            # return redirect("/")
            return render(request,'booking.html',d)
        else:
             d={"forms":LoginForm}
             msg.info(request,'invalidcredentials')
             return render(request,"login.html",d)
            #  return redirect('loginn')

    else:
        d={"forms":LoginForm}
        return render(request,"login.html",d)
    
def logoutt(request):
    logout(request)
    return redirect("/")
def explore(request,eid):
    user=request.session.get('id')
    # obj_user=User.objects.get(id=user)
    if user is None:
         d={"forms":LoginForm}

         return render(request,'login.html',d)

    else:
       obj=Details.objects.filter(Dest=eid)
       d={'data':obj}
       return render(request,'dest.html',d)
    
def userhome(request):
    obj=Destinations.objects.all()
    d={'dest':obj}

    return render(request,'booking.html',d) 
def booking(request,eid):

    amount=Destinations.objects.get(id=eid)
    # print(amount.price)
    user_id=request.session.get("id")
    obj_user=User.objects.get(id=user_id)
    if request.method=='POST':
        
        textval=int(request.POST.get('No_of_Persons'))
        amount1=int(request.POST.get("amount"))
        ta=textval*amount1
        print(ta)

        obj=BookingForm(request.POST)
        data=obj.save(commit=False)
        data.user=obj_user
        data.price=amount1
        data.total=ta
        data.save()
        da=Booking.objects.filter(user=user_id)

        return render(request,'viewbooking.html',{'da':da})
    else:
        d={'forms':BookingForm}
        return render(request,'forms1.html',{'forms':BookingForm,'amount':amount.price})
def viewbooking(request):
    obj=request.session.get("id")
    da=Booking.objects.filter(user=obj)
    # ds=Booking.objects.get(user=obj)
    # if ds=="":

    #     return HttpResponse("your ticket has been cancelled")
    # else:
    #   a=ds.No_of_Persons
    #   b=ds.price
    #   ta=a*b
    return render(request,'viewbooking.html',{'da':da})



    


    

    # a=Booking.objects.filter(No_of_Persons=obj)

    # b=Booking.objects.filter(price=obj)

    # ta=a*b



    


    # textval=request.POST.get('No_of_Persons')
    # amount1=request.POST.get("amount")
    # total_amount=textval*amount1


    


def edit(request,eid):
     user_id=request.session.get("id")

     obj=Booking.objects.get(id=eid)
     ta=obj.price
    
     if request.method=='POST':
         textval=int(request.POST.get('No_of_Persons'))
         amount1=int(request.POST.get("amount"))
         totalp=textval*amount1
         print(totalp)
         obj1=BookingForm(request.POST,instance=obj)
         data=obj1.save(commit=False)
         data.total=totalp
         data.save()
         
         da=Booking.objects.filter(user=user_id)

         


         return render(request,'viewbooking.html',{'da':da})
        #  return redirect("/acc-viewbooking")
     else:
        d={'forms':BookingForm(instance=obj)}
        return render(request,'forms1.html',{'forms':BookingForm(instance=obj),'amount':ta})
def delete(request,eid):
        obj=Booking.objects.get(id=eid)
        obj.delete()
        return redirect("/acc-viewbooking")

def search(request):
    # ids=request.session.get('id') 
    srch=request.POST.get('srch') 
    obj=Destinations.objects.filter(name=srch) 
    d={'dest':obj} 
    print(obj)
    return render(request,'booking.html',d)
    
    


    # obj_user=request.session.get("id")
    # obj=User.objects.get(id=obj_user)
    # if obj is not None:
    #     obj2=Details.objects.filter()

    #     if  obj2.dest=='tajmahal':
    #         d={'data':obj2}
    #         return render(request,'dest.html',d)
    #     elif obj2.dest=='mumbai':

            
    #         d={'data':obj2}
    #         return render(request,'dest.html',d)
 
    # else:
    #     return HttpResponse("please login")

