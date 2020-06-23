from django.shortcuts import render, HttpResponse, redirect
from .models import Contact,User_Signup
from django.http import HttpResponse
from passlib.hash import pbkdf2_sha256
from django.core.mail import send_mail,EmailMultiAlternatives
from instructor.models import CourseCategory

import random

# Create your views here.
def home(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        data=User_Signup.objects.get(username=username)
        password_encrpt=pbkdf2_sha256.hash(password)
        data.password=password_encrpt
        data.save()
        return redirect('/')
    data=CourseCategory.objects.all()
    return render(request,'index.html',{'data':data})

    
        

    
    
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        subject=request.POST['subject']
        data=Contact(Full_name=name,Email=email,subject=subject,Message=message)
        if data:
            data.save()
            Thank = True
            message="Your Response is Recorded"
            return render(request,'page-contact.html',{'message':message,'Thank':Thank})  
        else:
            
            message="Please Fill Correctly"
            return render(request,'page-contact.html',{'message':message,'Thank':Thank})  
    return render(request,'page-contact.html')
    

def pagecoursev2(request):
    return render(request,'page-course-v2.html')

def instructor(request):
    return render(request,'page-instructors.html')
def instructorsingle(request):
    return render(request,'page-instructors-single.html')

def coursev1(request):
    return render(request,'page-course-v1.html') 

def coursev2(request):
    return render(request,'page-course-v2.html') 

def coursev3(request):
    return render(request,'page-course-v3.html') 

def blog1(request):
    return render(request,'page-blog-v1.html')

def blog2(request):
    return render(request,'page-blog-grid.html')

def blog3(request):
    return render(request,'page-blog-list.html')

def single_post(request):
    return render(request,'page-blog-single.html')

def signup(request):
    if request.method=="POST":
        
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password1']
        password_encrpt=pbkdf2_sha256.hash(password)
        checkuser_name = User_Signup.objects.filter(username=username)
        checkuser_email = User_Signup.objects.filter(email=email)
        if checkuser_name or checkuser_email:
            thank=True
            msg="The username or email is already"
            return render(request,'index.html',{'msg':msg,'thank':thank})
           
        # mail verification
        token=random.randint(1000,100000)

        
        html_content=f'''
            <h1 style="text-align:center; font-family: 'Montserrat', sans-serif;">Finish creating your account</h1>
                <p> 
        Your email address has been registered with lms. To validate your account and activate your ability to send email campaigns, please complete your profile by clicking the link below:</p>
            <div style='width:300px; margin:0 auto;'> <a href='http://127.0.0.1:8000/verification/{token}/{username}' style=" background-color:#0066ff; border: none;  color: white; padding: 15px 32px;  text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; font-family: PT Sans, sans-serif;" >click here</a>
        </div>
            '''
        
        data=User_Signup(username=username,email=email,password=password_encrpt,token=token)
        data.save()
        thank=True
        msg="your account is successfully created please check your email and verify your account"
        subject, from_email, to = 'Verify Account', 'no-replay@gwadarengineeringworks.com', email
        msgsend = EmailMultiAlternatives(subject, html_content, from_email, [to])
        msgsend.attach_alternative(html_content, "text/html")
        msgsend.send()
        
        return render(request,'index.html',{'msg':msg,'thank':thank})
        

    return redirect('/')
       


  
def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        try:
            data=User_Signup.objects.get(email=email)
            if data:
                encrpt=data.password
                role=data.role
                encrpt=pbkdf2_sha256.verify(password,encrpt)
            if encrpt and role=="null":
                data=User_Signup.objects.get(email=email)
                request.session['username'] = data.username
                request.session['userid'] = data.sno
                request.session['role'] = data.role
                thank=True
                msg="Successfully Login"
                return render(request,'index.html',{'thank':thank,'msg':msg})
            elif encrpt and role=="Teacher":
                data=User_Signup.objects.get(email=email)
                request.session['username'] = data.username
                request.session['userid'] = data.sno
                request.session['role'] = data.role
                thank=True
                msg="Successfully Login"
                return render(request,'dashboard/page-dashboard.html',{'thank':thank,'msg':msg})

            else:
                thank=True
                msg="Password Incorrect"
                return render(request,'index.html',{'thank':thank,'msg':msg})
               
            
        except User_Signup.DoesNotExist:
            thank=True
            msg="Email Doesnot Exist"
            return render(request,'index.html',{'thank':thank,'msg':msg})

            
            
    return redirect('/')

     
       
      
    return redirect('/')

# verification 
def verification(request,verification,username):
    data= User_Signup.objects.get(username=username)
   
    if data.token==verification:
        updata= User_Signup.objects.get(username=username)
        updata.verify='verified'
        updata.save()
        return redirect('/login')
        
# end verification

# def error(request,slug):
#     return render(request,'page-error.html')

def forgetrequest(request):
    
    email=request.GET.get('email')
  
    token=random.randint(1000,100000)
 
    data=User_Signup.objects.get(email=email)
    username=data.username
    data.token=token
    data.save()

    subject, from_email, to = 'Forget Password', 'no-replay@gwadarengineeringworks.com', email
    html_content = f'''
            <h1 style="text-align:center; font-family: 'Montserrat', sans-serif;">Finish creating your account</h1>
                <p> 
        Your email address has been registered with lms. To validate your account and activate your ability to send email campaigns, please complete your profile by clicking the link below:</p>
            <div style='width:300px; margin:0 auto;'> <a href='http://127.0.0.1:8000/forget/{token}/{username}' style=" background-color:#0066ff; border: none;  color: white; padding: 15px 32px;  text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; font-family: PT Sans, sans-serif;" >click here</a>
        </div>
            '''
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return HttpResponse('sent')

def forget(request,verification,username):
    token=verification
    username=username
    return render(request,'forget.html',{'token':token,'username':username})

# def forgetcomplete(request):
#     if request.method=="POST":
#         username=request.POST['username']
#         password=request.POST['password']
#         data=User_Signup.objects.get(username=username)
#         password_encrpt=pbkdf2_sha256.hash(password)
#         data.password=password_encrpt
#         data.save()
#         return HttpResponse('change')
#     return HttpResponse('not work')


def logout(request):
    del request.session['role']
    del request.session['username']
    del request.session['userid']
    return redirect('/')


def base(request):
    return render(request,'user/checking.html')

