from django.shortcuts import render,HttpResponse,redirect
from faculty.models import User_Signup,Materialclass,Course,Instructor,NotificationModel,AssigmentModel,Department,Teacher_syllabus,TeacherApplication,Query_Admin,SerTeacher,User_Stories,CourseVideos,Faculty_Development,Exam_Result,Faculty_Evaluation,Semester,Exam_Result,onlinequiz
from student.models import Application,Student_Signup,Student_Course,Student_Profile,Student_Assigment,MeetingAppointment
from library.models import Books
from django.http import HttpResponse
from passlib.hash import pbkdf2_sha256
from django.core.mail import send_mail,EmailMultiAlternatives
from django.core.paginator import Paginator
from administrator.models import AcademicCalendarModel,FacultyCalendarModel,Form,Admin_Notification,role,RoomReservation,Rooms,menu,MenuOrders, menuSer,FacultyAttendence,Faculty_Evaluation_Report,Semester_Schedule,Exam_Schedule,StudentAttendence
import random
import json
from django.db.models import Q
from django.contrib import messages
from django.template import RequestContext
from datetime import datetime


# Create your views here.


def handler404(request,exception):
    return render(request,'page-error.html')

def fdashboard(request):
    try:
        if request.session['role']=="Teacher":
            form=Form.objects.filter(FileCategory="facultyguidline")
            cacform=Form.objects.filter(FileCategory="cacforms")
            instructer_data=User_Signup.objects.get(user_id=request.session['userid']) 
            
            return render(request,'faculty/page-dashboard.html',{'form':form,'cacform':cacform,'instructer_data':instructer_data})

           
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
            

    except:
        return redirect('/')
def check(request):
    return render(request,'superadmin/page-dashboard.html')
    # present=datetime.now()
    # data=Exam_Schedule.objects.get(Exam_Schedule_Id=1)
    # past=data.Year.date()

    # if past <= present.date():
    #     return HttpResponse('login')
    # else:
    #     return HttpResponse('logout')
    
  
   
  

#semester form guidline
def formguidline(request):
    try: 
        if request.session['role']=="Teacher":
            appform=Form.objects.filter(FileCategory="applicationform")
            thesisform=Form.objects.filter(FileCategory="thesisguidline")
            placeform=Form.objects.filter(FileCategory="placementforms")
            return render(request,'faculty/formguidline.html',{'appform':appform,'thesisform':thesisform,'placeform':placeform})

        
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})

    except:
         return redirect('/')
#semester library
def library(request):
    # libary html page data
    try:
        if request.session['role']=="Teacher":
            datas= Books.objects.all().order_by('-BookId')
            paginator = Paginator(datas,1)
            pages=request.GET.get('page',1)
            pagenumber= paginator.get_page(pages)
            if pagenumber.has_next():
                next_url=f'?page={pagenumber.next_page_number()}'
            else:
                next_url=''

            if pagenumber.has_previous():
                previous_url=f'?page={ pagenumber.previous_page_number() }'
            else:
                previous_url=''    
            alldata={
                'data':pagenumber,
                'nextpage':next_url,
                'previouspage':previous_url,
            }
            # end library page data
            if request.method=="POST":
                books=request.POST['BookTitle']
                BookAuthor=request.POST['BookAuthor']
                BookPublisher=request.POST['BookPublisher']
                BookIsbn=request.POST['BookIsbn']
                data=Books.objects.filter(BookTitle__icontains=books , BookPublisher__icontains=BookPublisher ,BookISBN__icontains=BookIsbn,BookAuthorid__BookAuthorFirstName__icontains=BookIsbn)

                alldata={
                    'data':data
                }
                return render(request,'faculty/librarysearch.html',alldata)
        
        
            return render(request,'faculty/library.html',alldata)
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})

    except:
        return redirect('/')
    
#semester library
def digitallibrary(request):
    try: 
        if request.session['role']=="Teacher":
            data= Books.objects.filter(Bookcategory="digitallibrary")
            return render(request,'faculty/digitallibrary.html',{'data':data})
            
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
    except:
        return redirect('/')

#semester Phd digital library
def Phddigitallibrary(request):
    try: 
        if request.session['role']=="Teacher":
            data= Books.objects.filter(Bookcategory="digitallibraryphd")
            return render(request,'faculty/Phddigitallibrary.html',{'data':data}) 
           
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
            
    except:
        return redirect('/')
    

#semester academic calendar
def academiccalendar(request):
    try:
        if request.session['role']=="Teacher":
            data=AcademicCalendarModel.objects.all()
            return render(request,'faculty/academiccalendar.html',{'data':data}) 
            
        
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
    except:
        return redirect('/')
    

       

#semester faculty calendar
def facultycalendar(request):
    try:
        if request.session['role']=="Teacher":
            id=Instructor.objects.get(username=request.session['userid'])
            dep=Department.objects.filter(Instructor_id=id)
            data=FacultyCalendarModel.objects.filter(Department_id__in=dep)
            return render(request,'faculty/facultycalendar.html',{'data':data})
            
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
             
    except:
        return redirect('/')

#semester examresult
def examresult(request):
  
    try:
        if request.session['role']=="Teacher":

            if request.method=="POST":
                department=request.POST['department']
                courses=request.POST['courses']
                request.session['course']=courses
                request.session['depart']=department
                department=request.session['depart']
                course=request.session['course']
                dep=Department.objects.get(Department_name=department)
                depid=dep.Did
                data=Student_Course.objects.filter(Department_id=depid,Courses=courses)
                Instructor_courseid=list()
                for x in data:
                    Instructor_courseid.append(x.Student_ID)
                data2=Exam_Result.objects.filter(Student_ID__in=Instructor_courseid)
                id=request.session['userid']
                course_data=Instructor.objects.get(username=id)
                courses=Course.objects.filter(Instructor_id=course_data.tid)
                return render(request,'faculty/examresult.html',{'data':data,'courses':courses,'department':department,'course':course,'data2':data2})

            id=request.session['userid']
            course_data=Instructor.objects.get(username=id)
            courses=Course.objects.filter(Instructor_id=course_data.tid)
            return render(request,'faculty/examresult.html',{'courses':courses})
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})

    
    
    
    except:
        return redirect('/')
         


def resultentry(request):

    try:
        if request.session['role']=="Teacher":
            if request.method=="POST":
                project=request.POST['project']
                assignment=request.POST['q/a']
                midterm=request.POST['midterm']
                final=request.POST['final']
                total=request.POST['total']
                course=request.POST['course']
                dep=request.POST['depart']
                sid=request.POST['sid']
                cid=Course.objects.get(Cid=course)
                profile=Student_Profile.objects.get(StudentId=sid)
                Instructorid=Instructor.objects.get(username=request.session['userid'])
                check=Exam_Result.objects.filter(Course_id=cid,Student_ID=profile)
                if check:
                    thank=True
                    msg="Already Uploaded"
                    id=request.session['userid']
                    course_data=Instructor.objects.get(username=id)
                    courses=Course.objects.filter(Instructor_id=course_data.tid)
                    return render(request,'faculty/examresult.html',{'thank':thank,'msg':msg,'courses':courses})
                else:
                    
                    data=Exam_Result(Course_id=cid,Project_Marks=project,Quiz_Assignment_Marks=assignment,Midterm_Marks=midterm,Final_Marks=final,Total_Marks=total,InstructerId=Instructorid,Department_id=Department.objects.get(Department_name=dep),Student_ID=profile)
                    data.save()
                    thank=True
                    msg="Result upload sucessfully"
                    id=request.session['userid']
                    course_data=Instructor.objects.get(username=id)
                    courses=Course.objects.filter(Instructor_id=course_data.tid)
                    return render(request,'faculty/examresult.html',{'thank':thank,'msg':msg,'courses':courses})
        
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})

    except:
        return redirect('/')




#semester userstories
def facultyform(request):
    try:
        if request.session['role']=="Teacher":
            if request.method=="POST":
                checkboxlist=list()
                name=request.POST['name']
                depart=request.POST['department']
                courses=request.POST['courses']
                degree=request.POST['Degress']
                experties=request.POST['expertise']
                corearea=request.POST['corearea']
                ratio=request.POST['ratio']
                Area=request.POST['Area']
                id=request.session['userid']
                checkbox=request.POST.getlist('checkbox1')
                course_data=Instructor.objects.get(username=id)
                tid=course_data.tid
                checkboxlist.append(checkbox)
                data=Faculty_Development(Name=name,Highest_Degree=degree,Department=depart,Subject=courses,Course_you_Teach=experties,Core_Area_to_you_would_like_to_develop=corearea,Teacher_Research_Ratio=ratio,particular_area_of_work=Area,Instructor_id=Instructor.objects.get(username=id),area_of_expertise=checkboxlist)
                data.save()
                thank=True
                msg="Your Response is Recorded"
                return redirect('/faculty/')

            id=request.session['userid']
            course_data=Instructor.objects.get(username=id)
            depart=Department.objects.filter(Instructor_id=course_data.tid)
            courses=Course.objects.filter(Instructor_id=course_data.tid)
            teacher_name=course_data.First_Name
            return render(request,'faculty/facultyform.html',{'depart':depart,'courses':courses,'course_data':teacher_name}) 
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
    
    except:
        return redirect('/')
        

#semester coursefile
def coursefile(request):
    try:
        if request.session['role']=="Teacher":
            id=request.session['userid']
            course_data=Instructor.objects.get(username=id)   
            courses=Course.objects.filter(Instructor_id=course_data.tid)
            return render(request,'faculty/coursefile.html',{'data':courses})
           
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
           
    except:
        return redirect('/')
       


     

#semester roomreservation
def roomreservation(request):
    try:
        if request.session['role']=="Teacher":
            data= Rooms.objects.all()
            alldata={
                'data':data
            }
            return render(request,'faculty/roomreservation.html',alldata) 
            
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
    except:
        return redirect('/')

        

#semester foodreservation
def foodreservation(request):
    try:
    
        if request.session['role']=="Teacher":
            data= menu.objects.all()
            alldata={
                'data':data
            }
            return render(request,'faculty/foodreservation.html',alldata) 
        
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
    
    
    except:
        return redirect('/')



#semester dashboard
def fvledashboard(request):
    try:
        if request.session['role']=="Teacher":
            return render(request,'faculty/fvledashboard.html') 
            
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
    except:
        return redirect('/')

        



#semester myclass
def myclass(request):
    try:
        if request.session['role']=="Teacher":
            return render(request,'faculty/myclass.html') 
            
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
    except:
        return redirect('/')

         

def classmaterial(request):
    try:
        if request.session['role']=="Teacher":
            if request.method=="POST":

                title=request.POST['title']
                category=request.POST['category']
                course=Course.objects.get(Cid=request.POST['course']) 
                File=request.FILES['file']
                instructor_id=Instructor.objects.get(username=request.session['userid'])
                
                data3=Materialclass(Title=title,Category=category,MaterailFile=File,Course_id=course,Instructor_id=instructor_id)
                data3.save()
                thank=True
                msg="Successfully Uploaded"
                return render(request,'faculty/page-dashboard.html',{'thank':thank,'msg':msg})
            
            id=request.session['userid']
            course_data=Instructor.objects.get(username=id)   
            courses=Course.objects.filter(Instructor_id=course_data.tid)
            return render(request,'faculty/classmaterial.html',{'data':courses})
        
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})

    
    except:
        return redirect('/')



#Online Lecture 
def onlinelecture(request):
    try:
        if request.session['role']=="Teacher":
            course_data=Instructor.objects.get(username=request.session['userid'])  
            material=Materialclass.objects.filter(Instructor_id=course_data.tid,Category="lectures")
            return render(request,'faculty/onlinelecture.html',{'material':material})
            
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
            
    except:
        return redirect('/')
    

#OnlineBook
def onlinebook(request):
    try:
        if request.session['role']=="Teacher":
            course_data=Instructor.objects.get(username=request.session['userid'])  
            material=Materialclass.objects.filter(Instructor_id=course_data.tid,Category="ebooks")
            return render(request,'faculty/onlinebook.html',{'material':material})
           
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
            
    except:
        return redirect('/')
    

#Onlinequiz
def Onlinequiz(request):
    try:

        if request.session['role']=="Teacher":
            if request.method=="POST":

                coursename=request.POST['category']
                department=request.POST['department']
                semester=request.POST['semester']
                semesterdata=Semester.objects.get(Samester_Name=semester)
                semestername=semesterdata.SamesterId
                Instructor_id=Instructor.objects.get(username=request.session['userid'])
                link=request.POST['link']
                data=onlinequiz(semester=semester,Course_id=Course.objects.get(Cid=coursename),Instructor_id=Instructor.objects.get(username=request.session['userid']),Department_id=Department.objects.get(Department_name=department),quizlink=link)
                data.save()
                messages.success(request, 'Quiz Successfully Added')    
                return redirect('/faculty/onlinequiz')
                    
                    

            Instructor_id=Instructor.objects.get(username=request.session['userid'])
            courses=Course.objects.filter(Instructor_id=Instructor_id.tid)
            data=onlinequiz.objects.filter(Instructor_id=Instructor_id.tid)
            return render(request,'faculty/onlinequiz.html',{'courses':courses,'data':data})

        
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})

    except:
        return redirect('/')

def deletequiz(request,id):
    try:
        if request.session['role']=="Teacher":
            data=onlinequiz.objects.get(onlinequizid=id)
            data.delete()
            Instructor_id=Instructor.objects.get(username=request.session['userid'])
            courses=Course.objects.filter(Instructor_id=Instructor_id.tid)
            data=onlinequiz.objects.filter(Instructor_id=Instructor_id.tid)
            messages.error(request,"Delete Quiz Successfully")
            return render(request,'faculty/onlinequiz.html',{'courses':courses,'data':data})
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
    except:
        return redirect('/')


        



#mygrade
def mygrade(request):
    try:
        if request.session['role']=="Teacher":
            course_data=Instructor.objects.get(username=request.session['userid'])   
            courses=Course.objects.filter(Instructor_id=course_data.tid)
            return render(request,'faculty/mygrade.html',{'course':courses})
           
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
        
    
    except:
        return redirect('/')



#notification    
def notification(request):
    try:
        if request.session['role']=="Teacher":
            if request.method=="POST":
                title=request.POST['title']
                notifycategory=request.POST['notify']
                category=Course.objects.get(Cid=request.POST['category'])
                description=request.POST['description']
                instructor_id=Instructor.objects.get(username=request.session['userid'])
                data3=NotificationModel(NotificationTitle=title,Category=notifycategory,NotificationDesc=description,Course_id=category,Instructor_id=instructor_id)
                data3.save()
                thank=True
                msg="Notification Successfully Post"
                return redirect('/faculty/myclass')

            course_data=Instructor.objects.get(username=request.session['userid'])  
            notification=NotificationModel.objects.filter(Instructor_id=course_data.tid)
            courses=Course.objects.filter(Instructor_id=course_data.tid)
            return render(request,'faculty/mynotification.html',{'courses':courses,'notification':notification})
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})

    
    except:
        return redirect('/')
        

#createnotification
def createnotification(request):
    try:
        if request.session['role']=="Teacher":
            course_data=Instructor.objects.get(username=request.session['userid'])  
            notification=NotificationModel.objects.filter(Instructor_id=course_data.tid,Category="Section")
            return render(request,'faculty/createnotification.html',{'notification':notification})
            
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
            
    except:
         return redirect('/')
    



#Application
def application(request):
    try:
        if request.session['role']=="Teacher":
            if request.method=="POST":
                title=request.POST['title']
                message=request.POST['message']
                img=request.FILES['file']
                id=Instructor.objects.get(username=request.session['userid'])
                data=TeacherApplication(ApplicationTitle=title,ApplicationMessage=message,ApplicationAttachment=img,Instructor_id=id)
                data.save()
                thank=True
                msg="Application Submitted"
                return render(request,'faculty/myclass',{'thank':thank,'msg':msg})


            data=TeacherApplication.objects.filter(Instructor_id=request.session['userid'])
            return render(request,'faculty/application.html',{'data':data})    
        
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})

    except:
         return redirect('/')
    


#Create Application
def createapplication(request):
    try:
        if request.session['role']=="Teacher":
            return render(request,'faculty/createapplication.html')
        
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})

    except:
        return redirect('/')
    
        


 
 
#create createprogramnotification
def createprogramnoti(request):
    try:
        if request.session['role']=="Teacher":
            course_data=Instructor.objects.get(username=request.session['userid'])  
            notification=NotificationModel.objects.filter(Instructor_id=course_data.tid,Category="program")
            return render(request,'faculty/createprogramnoti.html',{'notification':notification})
   
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
            
    except:
        return redirect('/')

#create student application
def app(request):
    try:
        if request.session['role']=="Teacher":
            id=Instructor.objects.get(username=request.session['userid'])
            data=Application.objects.filter(Instructor_id=id)
            return render(request,'faculty/app.html',{'data':data})
            
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
            
    except:
         return redirect('/')

###############Shoaib khan##########################   
def signup(request):
    if request.method=="POST":
        try:
        
            username=request.POST['username']
            email=request.POST['email']
            checkbox1=request.POST.get('checkbox1','off')
            checkbox2=request.POST.get('checkbox2','off')
            password=request.POST['password1']
            password1=request.POST['password2']
            if password!=password1:
                thank=True
                msg="The Two Password Fields Doesnot Match"
                return render(request,'index.html',{'msg':msg,'thank':thank})

            if checkbox1=="on" and checkbox2=="on":
                thank=True
                msg="Please Select Only One"
                return render(request,'index.html',{'msg':msg,'thank':thank})
            elif checkbox1=="off" and checkbox2=="off":
                thank=True
                msg="Please Select Atleast One Teacher or Student"
                return render(request,'index.html',{'msg':msg,'thank':thank})
            elif checkbox1=="on":
                password_encrpt=pbkdf2_sha256.hash(password)
                checkuser_name = User_Signup.objects.filter(username=username)
                checkuser_email = User_Signup.objects.filter(email=email)
                if checkuser_name or checkuser_email:
                    thank=True
                    msg="The username or email is already"
                    return render(request,'index.html',{'msg':msg,'thank':thank})
                    
                data=User_Signup(username=username,email=email,password=password_encrpt)
                data.save()
                thank=True
                msg="Signup Sucessfully"
                return render(request,'index.html',{'msg':msg,'thank':thank})
            elif checkbox2=="on":
                password_encrpt=pbkdf2_sha256.hash(password)
                checkuser_name = Student_Signup.objects.filter(username=username)
                checkuser_email =Student_Signup.objects.filter(email=email)
                if checkuser_name or checkuser_email:
                    thank=True
                    msg="The username or email is already"
                    return render(request,'index.html',{'msg':msg,'thank':thank})
                    
                data=Student_Signup(username=username,email=email,password=password_encrpt)
                data.save()
                thank=True
                msg="Signup Sucessfully"
                return render(request,'index.html',{'msg':msg,'thank':thank})
        
        except:
            return redirect('/')

  
def login(request):
    if request.method=="POST":
        checkbox=request.POST.get('checkbox','off')
        email=request.POST['email']
        password=request.POST['password']
        if checkbox=="on":
            try:
                data=User_Signup.objects.get(email=email)
                try:
                    image=Instructor.objects.get(tid=data.user_id)
                    request.session['senderimg']=str(image.img)
                except:
                    None
              
    
                if data:
                    encrpt=data.password
                    role=data.role
                    encrpt=pbkdf2_sha256.verify(password,encrpt)
                if encrpt and role=="null":
                    data=User_Signup.objects.get(email=email)
                    request.session['username'] = data.username
                    request.session['userid'] = data.user_id
                    request.session['role'] = data.role
                    request.session['userrole'] = data.role
                    thank=True
                    msg="Successfully Login"
                    return render(request,'index.html',{'thank':thank,'msg':msg})
                elif encrpt:

                    data=User_Signup.objects.get(email=email)
                    request.session['username'] = data.username
                    request.session['userid'] = data.user_id
                    request.session['userrole'] = data.role
                   

                    request.session['role'] = data.role
                   
                    return redirect('/faculty/')
                

                else:
                    thank=True
                    msg="Password Incorrect"
                    return render(request,'index.html',{'thank':thank,'msg':msg})
                
                
            except:
                thank=True
                msg="Email Doesnot Exist"
                return render(request,'index.html',{'thank':thank,'msg':msg})
        else:
            try:
                data=Student_Signup.objects.get(email=email)
                try:
                    image=Student_Profile.objects.get(User_id=data.user_id)
                    request.session['senderimg']=str(image.Profile)
                except:
                    None
               
                
                # k=list()
                # for i in image:
                #     k.append(i.Profile)
                # ab=json.dumps(str(k))
        
                # request.session['senderimg']=k
                # return HttpResponse(ab)
               
            
                if data:
                    encrpt=data.password
                    role=data.role
                    encrpt=pbkdf2_sha256.verify(password,encrpt)
                if encrpt and role=="null":
                    data=Student_Signup.objects.get(email=email)
                    request.session['username'] = data.username
                    request.session['userid'] = data.user_id
                    request.session['userrole'] = data.role
                    request.session['role'] = data.role
                    thank=True
                    msg="Successfully Login"
                    return render(request,'index.html',{'thank':thank,'msg':msg})
                if encrpt:
                    data=Student_Signup.objects.get(email=email)
                    request.session['username'] = data.username
                    request.session['userid'] = data.user_id
                    request.session['userrole'] = data.role
                    request.session['role'] = data.role
                                         
                    return redirect('/student/')              
               

                else:
                    thank=True
                    msg="Password Incorrect"
                    return render(request,'index.html',{'thank':thank,'msg':msg})
                
                
            except Student_Signup.DoesNotExist:
                thank=True
                msg="Email Doesnot Exist"
                return render(request,'index.html',{'thank':thank,'msg':msg})

            
            


# verification 
def verification(request,verification,username):
    try:
        if request.session['role']=="Teacher":
            data= User_Signup.objects.get(username=username)
        
            if data.token==verification:
                updata= User_Signup.objects.get(username=username)
                updata.verify='verified'
                updata.save()
                return redirect('/login')

        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
        

    except:
        return redirect('/')


def forgetrequest(request):
    try:
        if request.session['role']=="Teacher":
    
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
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})

    
    except:
        return redirect('/')


def forget(request,verification,username):
    try:
        if request.session['role']=="Teacher":
            token=verification
            username=username
            return render(request,'forget.html',{'token':token,'username':username})
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})


    except:
        return redirect('/')


def logout(request):
    try:
    
   
        if request.session.has_key('role'):
            del request.session['role']
            del request.session['userrole']
            del request.session['username']
            del request.session['userid']
            del request.session['senderimg']
        return redirect('/')
        if request.session.has_key("senderid"):
            del request.session['senderid']
            del request.session['sendername']
            del request.session['senderimg']
        return redirect('/')
    
    except:
        return redirect('/')

#Assignment
def assignment(request):
    try:
        if request.session['role']=="Teacher":
            if request.method=="POST":
                title=request.POST['title']   
                desct=request.POST['desct']   
                coursename=Course.objects.get(Cid=request.POST['category'])  
                mfile=request.FILES['mfile']
                instructor_id=Instructor.objects.get(username=request.session['userid'])
                data=AssigmentModel(AssigmentTitle=title,AssigmentDesc=desct,AssigmentFile=mfile,Course_id=coursename,Instructor_id=instructor_id)
                data.save()
                thank=True
                msg="Assigment Uploaded Successfully"
                return render(request,'faculty/myclass.html',{'thank':thank,'msg':msg})

            
            course_data=Instructor.objects.get(username=request.session['userid'])   
            courses=Course.objects.filter(Instructor_id=course_data.tid)
            assignment=AssigmentModel.objects.filter(Instructor_id=course_data.tid)
            return render(request,'faculty/assignments.html',{'courses':courses,'assignment':assignment})
            
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})

    except:
        return redirect('/')

#create creategradebookon
def creategradebook(request):
    try:
        if request.session['role']=="Teacher":
            if request.method=="POST":
                coursename=request.POST['category']
                department=request.POST['department']
                total_marks=request.POST['Total_Marks']
                Total_Marks=request.POST['Total_Marks']
                Obtain_Marks=request.POST['Obtain_Marks']
                semester=request.POST['semester']
                semesterdata=Semester.objects.get(Samester_Name=semester)
                semestername=semesterdata.SamesterId
                Instructor_id=Instructor.objects.get(username=request.session['userid'])
                data=Course(Course_name=coursename,Total_Marks=total_marks,Obtain_Marks=Obtain_Marks,Instructor_id=Instructor_id,Department_id=Department.objects.get(Department_name=department),Semester_id=Semester.objects.get(SamesterId=semestername))
                
                # return HttpResponse(semester)
                data.save()
                thank=True
                msg="Grade Uploaded Successfully"
                return render(request,'faculty/myclass.html',{'thank':thank,'msg':msg})

            Instructor_id=Instructor.objects.get(username=request.session['userid'])
            courses=Course.objects.filter(Instructor_id=Instructor_id.tid)
            return render(request,'faculty/creategradebook.html',{'courses':courses})

    except:
        return redirect('/')
    
   
def classnotification(request):

    try:
        if request.session['role']=="Teacher":
            course_data=Instructor.objects.get(username=request.session['userid'])  
            notification=NotificationModel.objects.filter(Instructor_id=course_data.tid,Category="class")
            return render(request,'faculty/classnotification.html',{'notification':notification})
           
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
            
    except:
        return redirect('/')


#syllabus
def syllabus(request):
    try:
        if request.session['role']=="Teacher":
            course_data=Instructor.objects.get(username=request.session['userid'])  
            syllabus=Teacher_syllabus.objects.filter(Instructor_id=course_data.tid)
            return render(request,'faculty/syllabus.html',{'syllabus':syllabus})
           
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
            
    except:
        return redirect('/')


    

#Create syllabus
def createsyllabus(request):
    try:
        if request.session['role']=="Teacher":
            if request.method=="POST":
                title=request.POST['semester']
                coursename=request.POST['category']
                department=request.POST['department']
                img=request.FILES['file']
                data=Teacher_syllabus(semester=title,outline=img,Course_id=Course.objects.get(Cid=coursename),Department_id=Department.objects.get(Did=department),Instructor_id=Instructor.objects.get(username=request.session['userid']))
                data.save()
                thank=True
                msg="Syllabus Successfully Uploaded"
                return render(request,'faculty/myclass.html',{'thank':thank,'msg':msg})
                
        
            Instructor_id=Instructor.objects.get(username=request.session['userid'])
            courses=Course.objects.filter(Instructor_id=Instructor_id.tid)
            department=Department.objects.filter(Instructor_id=Instructor_id.tid)
            return render(request,'faculty/createsyllabus.html',{'courses':courses,'department':department})
        
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})



  
            
    except:
        return redirect('/')
    

    


#semester myclass
def onlinequery(request):
    try:
        if request.session['role']=="Teacher":
            course_data=Instructor.objects.get(username=request.session['userid'])   
            query=Query_Admin.objects.filter(Instructor_id=course_data.tid)
            return render(request,'faculty/onlinequery.html',{'query':query}) 
         
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
           
    except:
        return redirect('/')



        



def createquery(request):
    try:
        if request.session['role']=="Teacher":
            if request.method=="POST":
                querytitle=request.POST['querytitle']
                querymessage=request.POST['querymessage']
                instructor_id=Instructor.objects.get(username=request.session['userid'])
                data=Query_Admin(querytitle=querytitle,querymessage=querymessage,Instructor_id=instructor_id)
                data.save()
                thank=True
                msg="Query Send Successfully"
                return render(request,'faculty/myclass.html',{'thank':thank,'msg':msg})
        
        
            return render(request,'faculty/createquery.html')
    
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})

    except:
        return redirect('/')      
   
def myroles(request):
    try:
        if request.session['role']=="Teacher":
            id=Instructor.objects.get(username=request.session['userid'])
            data=role.objects.filter(Instructor_id=id)
            return render(request,'faculty/myroles.html',{'data':data})
           
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
          
    except:
        return redirect('/')   
    
#semester userstories
def userstories(request):
    try:
        if request.session['role']=="Teacher":
            if request.method=="POST":
                I_want_to=request.POST['I_want_to']
                So_that_I_can=request.POST['So_that_I_can']
                category=request.POST['category']
                instructor_id=Instructor.objects.get(username=request.session['userid'])
                data=User_Stories(I_want_to=I_want_to,Category=category,So_that_I_can=So_that_I_can,Instructor_id=instructor_id)
                data.save()
                thank=True
                msg="Successfully Add"
                return render(request,'faculty/page-dashboard.html',{'thank':thank,'msg':msg})

            id=request.session['userid']
            course_data=Instructor.objects.get(username=id)   
            courses=User_Stories.objects.filter(Instructor_id=course_data.tid)
            return render(request,'faculty/userstories.html',{'data':courses})
        
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
    except:
        return redirect('/')   

 #semester facultyattendance
def facultyattendance(request):
    try:
        if request.session['role']=="Teacher":
    
            if request.method=="POST":
                Month=request.POST['Month']
                Year=request.POST['Year']
                id=request.session['userid']
                course_data=Instructor.objects.get(username=id)   
                courses=FacultyAttendence.objects.filter(Instructor_id=course_data.tid,FacultyAttendenceYear=Year,FacultyAttendenceMonth=Month)
                return render(request,'faculty/facultyattendance.html',{'data':courses})


            id=request.session['userid']
            course_data=Instructor.objects.get(username=id)   
            courses=FacultyAttendence.objects.filter(Instructor_id=course_data.tid)
            return render(request,'faculty/facultyattendance.html',{'data':courses})
        
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})

    except:
        return redirect('/')  




#semester facultyevaluation
def facultyevaluation(request):
    try:
        if request.session['role']=="Teacher":
            if request.method=="POST":
                Report=Faculty_Evaluation_Report.objects.get(Faculty_Evaluation_Report_ID=request.POST['report'])
                reportname=Report.Report_Name
                file=Report.Report_File
                department=Department.objects.get(Did=request.POST['depart'])
                course=Course.objects.get(Cid=request.POST['course']) 
                instructor_id=Instructor.objects.get(username=request.session['userid'])
                data3=Faculty_Evaluation(Report_Name=reportname,Department_id=department,Course_id=course,InstructerId=instructor_id,Report_File=file)
                data3.save()
                thank=True
                msg="Successfully Uploaded"
                return redirect('/faculty/')

            id=request.session['userid']
            course_data=Instructor.objects.get(username=id)   
            courses=Course.objects.filter(Instructor_id=course_data.tid)
            depart=Department.objects.filter(Instructor_id=course_data.tid)
            report=Faculty_Evaluation_Report.objects.filter(Department_id=course_data.tid)
            return render(request,'faculty/facultyevaluation.html',{'data':courses,'depart':depart,'report':report})
        

        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
    except:
        return redirect('/')  



#semester schedule page
def semesterschedule(request):
        
    try:
        if request.session['role']=="Teacher":
            id=request.session['userid']
            course_data=Instructor.objects.get(username=id) 
            courses=Course.objects.filter(Instructor_id=course_data.tid)
            a=[]
            for i in courses:
                a.append(i.Department_id)
            data=Semester_Schedule.objects.filter(Department_id__in=a)
            return render(request,'faculty/semesterschedule.html',{'data':data})
          
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
        
    except:
        return redirect('/') 



def examschedule(request):
    try:
        if request.session['role']=="Teacher":
            id=request.session['userid']
            course_data=Instructor.objects.get(username=id) 
            courses=Course.objects.filter(Instructor_id=course_data.tid)
            a=[]
            for i in courses:
                a.append(i.Department_id)
            data=Exam_Schedule.objects.filter(Department_id__in=a)
            return render(request,'faculty/examschedule.html',{'data':data}) 
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
             
    except:
        return redirect('/')


#semester attendancet

def attendance(request):
    try:
        if request.session['role']=="Teacher":
            if request.method=="POST":
                courses=request.POST['courses']
                year=request.POST['year']
                month=request.POST['month']
                instructer_data=Instructor.objects.get(username=request.session['userid'])  
                course_data=Course.objects.filter(Instructor_id=instructer_data.tid)
                Instructor_courseid=list()
                for x in course_data:
                    Instructor_courseid.append(x.Cid)
                data=StudentAttendence.objects.filter(Course_id=courses,StudentAttendenceYear=year,StudentAttendenceMonth=month)
                data2=StudentAttendence.objects.filter(Course_id__in=Instructor_courseid)
                return render(request,'faculty/attendance.html',{'course_data':course_data,'data':data,'data2':data2})
            
            instructer_data=Instructor.objects.get(username=request.session['userid'])  
            course_data=Course.objects.filter(Instructor_id=instructer_data.tid)
            Instructor_courseid=list()
            for x in course_data:
                Instructor_courseid.append(x.Cid)
            data=StudentAttendence.objects.filter(Course_id__in=Instructor_courseid)
            data2=StudentAttendence.objects.filter(Course_id__in=Instructor_courseid)
            return render(request,'faculty/attendance.html',{'course_data':course_data,'data':data,'data2':data2})



        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
    except:
        return redirect('/')

   


        

def email(request):
    try:
        if request.session['role']=="Teacher":
            instructer_data=User_Signup.objects.get(user_id=request.session['userid']) 
            return render(request,'faculty/page-dashboard.html',{'instructer_data':instructer_data})  
            
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
            
    except:
        return redirect('/')
 
def studentassignment(request):
    try:
        if request.session['role']=="Teacher":
            if request.method=="POST":
                courseid=request.POST['courses']
                data=Student_Assigment.objects.filter(Course_id=courseid)
                instructer_data=Instructor.objects.get(username=request.session['userid'])  
                course_data=Course.objects.filter(Instructor_id=instructer_data.tid)
                Instructor_courseid=list()
                for x in course_data:
                    Instructor_courseid.append(x.Cid)
                return render(request,'faculty/studentassignments.html',{'course':course_data,'data':data})

            
            instructer_data=Instructor.objects.get(username=request.session['userid'])  
            course_data=Course.objects.filter(Instructor_id=instructer_data.tid)
            Instructor_courseid=list()
            for x in course_data:
                Instructor_courseid.append(x.Cid)
            data=Student_Assigment.objects.filter(Course_id__in=Instructor_courseid)
            return render(request,'faculty/studentassignments.html',{'course':course_data,'data':data})

        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})

    except:
        return redirect('/')
        
        


def videocall(request):
    try:
        if request.session['role']=="null":
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
        else:
            return render(request,'videocalling/index.html')
    except:
        return redirect('/')


def Appointment(request):
    try:
        if request.session['role']=="Teacher":
            instructer_data=Instructor.objects.get(username=request.session['userid'])
            course_data=Course.objects.filter(Instructor_id=instructer_data.tid)
            Instructor_courseid=list()
            for x in course_data:
                Instructor_courseid.append(x.Cid)
            data=MeetingAppointment.objects.filter(Course_id__in=Instructor_courseid)
            return render(request,'faculty/Appointment.html',{'data':data})


        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
    except:
        return redirect('/')



def chat(request):
    try:
    
        if request.session['role']=="null":
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
        else:
            return redirect('chat/')
    

    except:
        return redirect('/')


def onlineclass(request):
    try:
        if request.session['role']=="Teacher":
            return redirect('https://solutions.agora.io/education/web/')
            
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
    except:
        return redirect('/')

        

###################End Shoaib khan################################

####################shakeeb#######################################
def becometeacher(request):
 
    try:
        if request.session['role']=="Teacher":
            if request.method=="POST":
                img=request.FILES['image']
                firstname=request.POST['firstname']
                lastname=request.POST['lastname']
                gender=request.POST['gender']
                address=request.POST['address']
                phone=request.POST['phone']
                birth=request.POST['birth']
                username=request.session['username']
                user=User_Signup.objects.get(username=username)
                data=Instructor(First_Name=firstname,Last_Name=lastname,Gender=gender,Address=address,Phone_Number=phone,Dob=birth,img=img,username=user)
                data.save()
                user.role="Teacher"
                user.save()
                images=Instructor.objects.get(username=request.session['userid'])
                request.session['senderimg']= str(images.img)
                thank=True
                msg="Your Profile Sucessfully Created"
                return redirect('/faculty/')
            
    
            data=Instructor.objects.filter(username=request.session['userid'])
            if data:
                Thank=True
                return render(request,'faculty/becomeinstructor.html',{'thank':Thank})
                
            else:
                return render(request,'faculty/becomeinstructor.html')
            
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})   
    except:
        return redirect('/')

 

    
def showteacher(request):
    try:
        if request.session['role']=="Teacher":
            userdata = list()
            data=Instructor.objects.filter(username=User_Signup.objects.get(username=request.session['username']))
            if data:
                for x in data:
                    datas=SerTeacher(x)
                    userdata.append(datas.data)
                return HttpResponse(json.dumps(userdata))
            
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
            
    except:
        return redirect('/')

def editinstructor(request):
    try:
        if request.method=="POST":
            data=Instructor.objects.filter(username=User_Signup.objects.get(username=request.session['username'])).update(First_Name=request.POST['firstname'],Last_Name=request.POST['lastname'],Gender=request.POST['gender'],Phone_Number=request.POST['phone'],Address=request.POST['address'],Dob=request.POST['birth'])
            
            return HttpResponse('Update Profile Suceesfully')
    except:
        return redirect('/')

def AddVideos(request):
    try:
        if request.session['role']=="Teacher":
            if request.method =='POST':
                title= request.POST['title']
                description= request.POST['description']
                course=request.POST['course']
                videofile= request.FILES['video']
                id=request.session['userid']
                teacherdata=Instructor.objects.get(username=id)   
                courses=Course.objects.get(Cid=course)
                data=CourseVideos(VideoTitle=title,VideoDesc=description,VideoFile=videofile,CourseId=courses,InstructerId=teacherdata)
                data.save()
                return HttpResponse("Video uploaded successfully")
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
    
    except:
        return redirect('/')


def showvideo(request):
    try:
        if request.session['role']=="Teacher":
            id=request.session['userid']
            course_data=Instructor.objects.get(username=id)   
            video=CourseVideos.objects.filter(InstructerId=course_data.tid)
            return render(request,'faculty/showvideo.html',{'video':video})
          
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
            
    
    except:
        return redirect('/') 

###################End Shakeeeb################################


###################Baloch################################



#create liststudent
def liststudent(request):
    try:
        if request.session['role']=="Teacher":
            if request.method=="POST":
                instructer_data=Instructor.objects.get(username=request.session['userid'])  
                course_data=Course.objects.filter(Instructor_id=instructer_data.tid)
                courses=request.POST['courses']
                data=Student_Course.objects.filter(Courses=courses).distinct()
                return render(request,'faculty/liststudent.html',{'data':data,'course_data':course_data})

            instructer_data=Instructor.objects.get(username=request.session['userid'])  
            course_data=Course.objects.filter(Instructor_id=instructer_data.tid)
            Instructor_courseid=list()
            for x in course_data:
                Instructor_courseid.append(x.Cid)
            data=Student_Course.objects.filter(Courses__in=Instructor_courseid).distinct()
            return render(request,'faculty/liststudent.html',{'data':data,'course_data':course_data})
        
        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
    
    except:
        return redirect('/') 


    



  

def RoomReservationinsert(request):
    try:
        if request.session['role']=="Teacher":
            if request.method =="POST":
                roomid = Rooms.objects.get(RoomId= request.POST['roomid'])
                Participants = request.POST['Participants']
                starttime = request.POST['starttime']
                Endtime = request.POST['Endtime']
                Comments = request.POST['Comments']
                Date = request.POST['date']
                data=RoomReservation(ReservationParticipants=Participants,ReservationComments=Comments,ReservationStartDate=Date,ReservationStartTime=starttime,ReservationEndTime=Endtime,RoomId=roomid)
                data.save()
                bookdata=Rooms.objects.get(RoomId= request.POST['roomid'])
                bookdata.RoomStatus="Booked"
                bookdata.save()
                return HttpResponse(Date)

        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
    
    except:
        return redirect('/') 
    

# menu card 
def menudata(request):
    try:
        if request.session['role']=="Teacher":

            Participants = request.POST['Participants']
            starttime = request.POST['starttime']
            Endtime = request.POST['Endtime']
            Comments = request.POST['Comments']
            Date = request.POST['date']
            foods= request.POST.getlist('food')
            data=MenuOrders(OrderParticipants=Participants,OrderComments=Comments,OrderList=foods,OrderStartDate=Date,OrderStartTime=starttime,OrderEndTime=starttime)
            data.save()
            return HttpResponse(foods)

        else:
            thank=True
            msg='Your are not a Teacher'
            return render(request,'index.html',{'thank':thank,'msg':msg})
    
    except:
        return redirect('/') 
###################End Baloch################################
