from django.shortcuts import render , HttpResponse , redirect
from student.models import Student_Course,Student_Profile ,SerStudentProfile
from faculty.models import Instructor , InstructorSerlizer,Course
from .models import messages,sermessages
import json
from datetime import datetime

import pusher
pusher_client = pusher.Pusher(
  app_id='980079',
  key='088b51ea5617a50f8ad0',
  secret='b2a51edb2c8eebe2aad7',
  cluster='ap2',
  ssl=True
)
# Create your views here.
def index(request):
   
    
    print(request.session['userid'])
    try:
        if request.session['role'] =='Student':
            stdprofile = Student_Profile.objects.get(User_id=request.session['userid'])
            request.session['senderid']= stdprofile.StudentId
            request.session['senderimg']= str(stdprofile.Profile)
            request.session['sendername']= stdprofile.First_name
        elif request.session['role'] =='Teacher':
            course_data=Instructor.objects.get(username=request.session['userid'])
            
            request.session['senderid'] = course_data.tid
            request.session['sendername']= course_data.First_Name
            request.session['senderimg']= str(course_data.img)
    except:
        if request.session['role'] =='Student':
            return redirect('studentdashboard')
        elif request.session['role'] =='Teacher':
            return redirect('fdashboard')
    return render(request,'chat/index.html')
    


def users(request):
    
    if request.session['userrole']=='Student':
        teacherid = list()
        userid = request.session['userid']
        student = Student_Profile.objects.get(User_id=userid)
        studentid= student.StudentId
        courses= Student_Course.objects.get(Student_ID=studentid)
        for x in courses.Courses.all():
            teacherid.append(x.Instructor_id.tid)
        data = Instructor.objects.filter(tid__in=teacherid)
        serdata = InstructorSerlizer(data , many=True)
        return HttpResponse(json.dumps(serdata.data))
    elif request.session['userrole']=='Teacher':
        instructer_data=Instructor.objects.get(username=request.session['userid'])  
        course_data=Course.objects.filter(Instructor_id=instructer_data.tid)
        
        Instructor_courseid=list()
        for x in course_data:
            Instructor_courseid.append(x.Cid)
    
        stdid = list()
        data=Student_Course.objects.filter(Courses__in=Instructor_courseid).distinct()
        for std in data:
            stdid.append(std.Student_ID.StudentId)
        
        studentdata = Student_Profile.objects.filter(StudentId__in=stdid)
        serdata = SerStudentProfile(studentdata , many=True)
        return HttpResponse(json.dumps(serdata.data))


# sender data
def sendmsg(request):
    if request.method == 'POST':
        sendername= request.session['sendername']
        sender = request.POST['sender']
        recever = request.POST['recever']
        msg = request.POST['msg']
        x= datetime.now()
        sendtime=x.strftime("%b %d %Y %H:%M:%S %p")
       
       
        pusher_client.trigger('chat', 'my-event', {'message': msg,'sender':sender,'recevier':recever,'sendername':sendername,'datetime':sendtime})
        data = messages(msgfrom=sender , msgto=recever , msg=msg , sender_name=sendername,created_at= sendtime)
        data.save()
        # chat data insert into database
        return HttpResponse(msg)



# all user messages
def oldmessages(request):

    if request.method =='GET':
        senderid=request.GET['sender']
        recevierid=request.GET['recevier']
        chatuser=[senderid,recevierid]
        print(chatuser)
        msg = messages.objects.filter(msgfrom__in=chatuser)
        data = sermessages(msg ,  many=True)
        return HttpResponse(json.dumps(data.data))
