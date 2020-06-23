from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.fdashboard,name='fdashboard'),
    path('semesterschedule', views.semesterschedule,name='semesterschedule'),
    path('formguidline', views.formguidline,name='formguidline'),
    path('library', views.library,name='library'),
    path('digitallibrary', views.digitallibrary,name='digitallibrary'),
    path('Phddigitallibrary', views.Phddigitallibrary,name='Phddigitallibrary'),
    path('academiccalendar', views.academiccalendar,name='academiccalendar'),
    path('facultycalendar', views.facultycalendar,name='facultycalendar'),
    path('examresult', views.examresult,name='examresult'),
    path('facultyevaluation', views.facultyevaluation,name='facultyevaluation'),
    path('attendance', views.attendance,name='attendance'),
    path('userstories', views.userstories,name='userstories'),
    path('facultyform', views.facultyform,name='facultyform'),
    path('coursefile', views.coursefile,name='coursefile'),
    path('roomreservation', views.roomreservation,name='roomreservation'),
    path('foodreservation', views.foodreservation,name='foodreservation'),
    path('onlinelecture', views.onlinelecture,name='onlinelecture'),
    path('facultyattendance', views.facultyattendance,name='facultyattendance'),
    path('fvledashboard', views.fvledashboard,name='fvledashboard'),
    path('email', views.email,name='email'),
    path('myclass', views.myclass,name='myclass'),
    path('onlinequery', views.onlinequery,name='onlinequery'),
    path('createquery', views.createquery,name='createquery'),
    # path('mynotification', views.mynotification,name='mynotification'),
    path('myroles', views.myroles,name='myroles'),
    path('classmaterial', views.classmaterial,name='classmaterial'),
    path('onlinelecture', views.onlinelecture,name='onlinelecture'),
    path('onlinebook', views.onlinebook,name='onlinebook'),
    path('onlinequiz', views.Onlinequiz,name='onlinequiz'),
    path('assignment', views.assignment,name='assignment'),
    path('mygrade', views.mygrade,name='mygrade'),
    path('notification', views.notification,name='notification'),
    path('createnotification', views.createnotification,name='createnotification'),
    path('application', views.application,name='application'),
    path('createapplication', views.createapplication,name='createapplication'),
    path('liststudent', views.liststudent,name='liststudent'),
    path('creategradebook', views.creategradebook,name='creategradebook'),
    path('createprogramnoti', views.createprogramnoti,name='createprogramnoti'),
    path('classnotification', views.classnotification,name='classnotification'),
    path('syllabus', views.syllabus,name='syllabus'),
    path('createsyllabus', views.createsyllabus,name='createsyllabus'),
    path('notification', views.notification,name='notification'),
    path('app', views.app,name='app'),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="login"),
    path('verification/<str:verification>/<str:username>',views.verification, name='verification'),
    path('forget/<str:verification>/<str:username>',views.forget, name='forget'),
    path('forgetrequest',views.forgetrequest,name="frequest"),
    path('logout',views.logout,name="logout"),
    path('accounts/',include('allauth.urls')),
    path('becometeacher',views.becometeacher,name="becometeacher"),
    path('showteacher',views.showteacher,name="showteacher"),
    path('editinstructor',views.editinstructor,name="editinstructor"),
    path('RoomReservationinsert',views.RoomReservationinsert,name="RoomReservationinsert"),
    path('menudata',views.menudata,name="menudata"),
    path('showvideo',views.showvideo,name="showvideo"),
    path('AddVideos',views.AddVideos,name="AddVideos"),
    path('examschedule',views.examschedule,name="examschedule"),
    path('resultentry',views.resultentry,name="resultentry"),
    path('studentassignment',views.studentassignment,name="studentassignment"),
    path('videocall',views.videocall,name="videocall"),
    path('onlineclass',views.onlineclass,name="onlineclass"),
    path('Appointment',views.Appointment,name="Appointment"),
    path('chat',views.chat,name="chat"),
    path('deletequiz/<int:id>',views.deletequiz,name="deletequiz"),
    path('check',views.check,name="check"),
    
    
   
]

