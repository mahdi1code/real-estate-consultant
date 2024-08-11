from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UserFormRigester, FormEdit, FormSendcustomermessage,EditFormSendcustomermessage ,CheckForm
from .models import CustomerUser,Customermessage
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


from django.contrib.auth.hashers import make_password
import socket
# Create your views here.

def Gotocontact(request):
    formmsg=FormSendcustomermessage()

    return render(request=request,template_name="contact.html",context={"formmsg":formmsg})

def gotoindex(request):
    return render(request=request,template_name="properties.html")

def gotoProperties(request):
    forms = UserFormRigester()
    return render (request=request,template_name="pagesaveuser.html",context={"form":forms})

def Gotepropertydetails(request):
        listuser = User.objects.all()
        listcustomermessage = Customermessage.objects.all()
        forms =FormEdit()
        formmsg=FormSendcustomermessage()
        return render(request=request,template_name="property-details.html",context={"formmsg":formmsg,"form":forms,"listuser":listuser,
        "listcustomermessage":listcustomermessage})


def  Register(request):
    if request.method == "POST":
        forms=UserFormRigester(request.POST)
        if forms.is_valid():
            UserName=forms.data["usernameform"]
            FullName=forms.data["fullnameform"]
            Password=forms.data["passwordform"]
            result=User(username=UserName,last_name=FullName,password=Password)
            result.set_password(forms.data["passwordform"])
            result.save()
            return HttpResponseRedirect("/gotoProperties")
        else:
            return HttpResponse("فرم isvalid  نیست")
    else:
        return HttpResponse("reqest  پست نیست")

def EditUser(request,id):
    result=User.objects.filter(id=id).first()
    action="/SaveEditUser"
    forms=FormEdit(initial={"id":id, "Username":result.username, "Fullname":result.last_name})
    forms1 = EditFormSendcustomermessage()
    return render(request=request, template_name="Edits.html", context={"form1":forms1,"form":forms,"action":action})


def SaveEditUser(request):
    if request.method == "POST":
        forms=FormEdit(request.POST)
        id=forms.data["id"]
        result=User.objects.filter(id=id).first()
        result.username=forms.data["Username"]
        #result.password=forms.data["pasword"]
        result.last_name=forms.data["Fullname"]
        result.save()
        return HttpResponseRedirect("/Gotepropertydetails")

def DeleteUser(request,id):
    result=User.objects.filter(id=id).first()
    result.delete()
    return HttpResponseRedirect("/Gotepropertydetails")


def Savecustomermessage(request):
    if request.method == "POST":
        formsg=FormSendcustomermessage(request.POST)
        result=Customermessage(FullName=formsg.data["fulname"],Email=formsg.data["email"],Issue=formsg.data["issue"],
        message=formsg.data["message"])
        result.save()
        formmsg=FormSendcustomermessage()
        return render(request=request,template_name="contact.html", context={"formmsg":formmsg})

def Editcustomermessage(request,id):
    result=Customermessage.objects.filter(Id=id).first()
    action="/SaveEditcustomermessage"
    forms1=EditFormSendcustomermessage(initial={"id":id,"fullname":result.FullName,"email":result.Email,"issue":result.Issue,
    "message":result.message})
    forms = FormEdit()
    return render(request=request,template_name="Edits.html",context={"form":forms,"form1":forms1,"action":action})

def SaveEditcustomermessage(request):
    if request.method == "POST":
        forms=EditFormSendcustomermessage(request.POST)
        id=forms.data["id"]
        result=Customermessage.objects.filter(Id=id).first()
        result.FullName=forms.data["fullname"]
        result.Email=forms.data["email"]
        result.Issue=forms.data["issue"]
        result.message=forms.data["message"]
        result.save()
        return HttpResponseRedirect("/Gotepropertydetails")

def Deletecustomermessage(request,id):
    result=Customermessage.objects.filter(Id=id).first()
    result.delete()
    return HttpResponseRedirect("/Gotepropertydetails")

def GotoLoginPage(request):
    forms=CheckForm()
    return render(request=request,template_name="index_1.html", context={"form":forms})


def CheckRegister(request):
    forms=CheckForm(request.POST)
    if forms.is_valid():
        UserName=forms.data["usernamecheck"]
        Password=forms.data["passwordcheck"]
        User=authenticate(request=request,username=UserName,password=Password)
        if User is not None:
            login(request,User)
            return HttpResponseRedirect("/Gotepropertydetails")
        else:
            return HttpResponse("حسابی با این مشخصات یافت نشد")
    else:
        return HttpResponse("فرم ولید نیست")

def Checkout(request):
    if request.user.is_authenticated:
        return HttpResponse("وارد شده است")
    else:
        return HttpResponse("وارد نشده است")

def Logoutuser(request):
    logout(request)
    return HttpResponse("کاربر خارج شد")








