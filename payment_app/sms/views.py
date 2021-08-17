from typing import get_origin
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from rest_framework import serializers, generics
from .forms import *
from django.core.mail import send_mail
from .models import *
import random
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response



# Create your views here.

def home(request):
    form = cxform()
    if request.method == "POST":
        form = cxform(request.POST)
        if form.is_valid():
            form.save()
            mail = form.cleaned_data.get("email")
            cx = customer.objects.get(email=mail)
            return render(request, "sms/otpcall.html", {"cx":cx})         
    return render(request, "sms/home.html",{"form":form})        

def upload(request, id, type):
    if type == "all":
        if request.method == "GET":
            form = docform( initial={"email":id})
            return render(request, "sms/upload.html", {"form":form})
        if request.method == "POST":
            form = docform(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse("<html><body><h1>Thank You for your interest in Easy Credit</h1></body></html>")
    
    if type == "poi":
        if request.method == "GET":
            form = poiForm(initial={"email":id})
            return render(request, "sms/upload.html", {"form":form})
        if request.method == "POST":
            doc = documents.objects.get(email=id)
            doc.poi = request.FILES["poi"]
            doc.save()
            return HttpResponse("<html><body><h1>Thank You for your interest in Easy Credit</h1></body></html>")

    if type == "poaFront":
        if request.method == "GET":
            form = poaFrontForm(initial={"email":id})
            return render(request, "sms/upload.html", {"form":form})
        if request.method == "POST":
            doc = documents.objects.get(email=id)
            doc.poaFront = request.FILES["poaFront"]
            doc.save()
            return HttpResponse("<html><body><h1>Thank You for your interest in Easy Credit</h1></body></html>")

    if type == "poaBack":
        if request.method == "GET":
            form = poaBackForm(initial={"email":id})
            return render(request, "sms/upload.html", {"form":form})
        if request.method == "POST":
            doc = documents.objects.get(email=id)
            doc.poaBack = request.FILES["poaBack"]
            doc.save()
            return HttpResponse("<html><body><h1>Thank You for your interest in Easy Credit</h1></body></html>")

    if type == "livePic":
        if request.method == "GET":
            form = livePicForm(initial={"email":id})
            return render(request, "sms/upload.html", {"form":form})
        if request.method == "POST":
            doc = documents.objects.get(email=id)
            doc.livePic = request.FILES["livePic"]
            doc.save()
            return HttpResponse("<html><body><h1>Thank You for your interest in Easy Credit</h1></body></html>")

    if type == "bankProof":
        if request.method == "GET":
            form = bankProofForm(initial={"email":id})
            return render(request, "sms/upload.html", {"form":form})
        if request.method == "POST":
            doc = documents.objects.get(email=id)
            doc.bankProof = request.FILES["bankProof"]
            doc.save()
            return HttpResponse("<html><body><h1>Thank You for your interest in Easy Credit</h1></body></html>")
    if type == "nachMandate":
        if request.method == "GET":
            form = nachMandateForm(initial={"email":id})
            return render(request, "sms/upload.html", {"form":form})
        if request.method == "POST":
            doc = documents.objects.get(email=id)
            doc.nachMandate = request.FILES["nachMandate"]
            doc.save()
            return HttpResponse("<html><body><h1>Thank You for your interest in Easy Credit</h1></body></html>")

    if type == "loanAgreement":
        if request.method == "GET":
            form = loanAgreementForm(initial={"email":id})
            return render(request, "sms/upload.html", {"form":form})
        if request.method == "POST":
            doc = documents.objects.get(email=id)
            doc.loanAgreement = request.FILES["loanAgreement"]
            doc.save()
            return HttpResponse("<html><body><h1>Thank You for your interest in Easy Credit</h1></body></html>")

 
def display(request, email):
    cx = customer.objects.get(id=email)
    #res = documents.objects.get(email=email)
    res = get_object_or_404(documents, email=email)

    return render(request, "sms/display.html",{"cx":cx, "res":res})

def softApproved(request):
    return render(request, "sms/softApproved.html")   

def check(request, id):
    cx = customer.objects.get(id=id)
    res = documents.objects.filter(email=id)
    if res.exists():
        return render(request, "sms/success.html", {"cx":cx})                
    else:
        HttpResponse("Docs not yet submitted")
        return render(request, "sms/process.html", {"cx":cx})

def reupload(request, id, type):

    res = get_object_or_404(documents, email=id)     
    cx = customer.objects.get(id=id)
    mail = cx.email
    send_mail(
            'no_reply _upload kyc documents for Easy Credit loan',
            f"Thank You for choosing Easy Credit, kindly upload your kyc documents using this link http://127.0.0.1:8000/upload/{id}/{type}",
            None,
            [mail],
            fail_silently=False,
            )
    return render(request, "sms/display.html", {"cx":cx, "res":res})

def otp(request, id):
    if request.method == "GET":
        cx = customer.objects.get(id=id)
        number = random.randint(1000,9999)
        send_mail(
        'no_reply _email_verification',
        f"OTP for your email verification is {number}",
        None,
        [cx.email],
        fail_silently=False,
        )
        return render(request, "sms/otp.html", {"cx":cx, "no":number})
  
def checkotp(request, id, no):
    cx = customer.objects.get(id=id)
    if request.method == "POST":
        num = request.POST.get("otp")
        if int(num) == int(no):
            send_mail(
            'no_reply _email_verification',
            f"Thank You for choosing Easy Credit, kindly upload your latest three months bank statements  using this link http://127.0.0.1:8000/statUpload/{id}",
            None,
            [cx.email],
            fail_silently=False,
            )
            return render(request, "sms/statProcess.html",{"cx":cx})

        else:
            return render(request, "sms/otpcall.html",{"cx":cx})  

def index(request):
    if request.method =="POST":
        # Get the post parameters
        username=request.POST['UserName']
        email=request.POST['email']
        pass1=request.POST['password']
        pass2=request.POST['password_confirm']

        # check for errorneous input
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('index')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('index')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('index')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('index')

    return render(request, "sms/index.html")

def list(request):
    return render(request, "sms/list.html")

def logout(request):
    return render(request,"sms/logout.html")

def statCheck(request,id):
    cx = customer.objects.get(id=id)
    res = get_object_or_404(statements, email=id)

    if request.method == "POST":
        loan_status = request.POST["loan-status"]
        res.loanStatus = loan_status
        return render(request, "sms/statResponse.html",{"loan_status" : loan_status})

    return render(request, "sms/statDisplay.html",{"cx":cx, "res":res})

def statUpload(request, id,):
    if request.method == "GET":
        form = statementsForm()
        return render(request, "sms/statUpload.html", {"form":form})
    if request.method == "POST":
        form = statementsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<html><body><h1>Thank You for your interest in Easy Credit</h1></body></html>")
        
        
        
            

def statUploadCheck(request, id):
    cx = customer.objects.get(id=id)
    res = statements.objects.filter(email=id)
    if res.exists():
        send_mail(
        f'Loan approval request of {cx.email}',
        f"Check the statements for loan approval at http://127.0.0.1:8000/statCheck/{id}",
        None,
        ["abhi30ml@gmail.com"],
        fail_silently=False,
        )
        return render(request, "sms/loanApproval.html", {"cx":cx})                
    else:
        return render(request, "sms/statProcess.html", {"cx":cx})

def loanApproval(request, id):
    cx = customer.objects.get(id=id)
    res = get_object_or_404(statements, email=id)
    if res.loanStatus == "Approved":
        send_mail(
        'no_reply _email_verification',
        f"Thank You for choosing Easy Credit, kindly upload your KYC documents  using this link http://127.0.0.1:8000/upload/{id}/all",
        None,
        [cx.email],
        fail_silently=False,
        )
        return render(request, "sms/process.html", {"cx":cx})

    else:
        return render(request, "sms/loanRejected.html", {"cx":cx})


# API views

class customerList(APIView):
    def get(self, request, format = None):
        cx = customer.objects.all()
        serializer = customerSerializer(cx, many=True)
        return Response(serializer.data)

class statementsView(generics.RetrieveAPIView):
    def get(self, request,id,format = None):
        stat = statements.objects.get(email = id)
        serializer = statementSerializer(stat)
        return Response(serializer.data)

