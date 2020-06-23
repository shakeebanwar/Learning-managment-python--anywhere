from django.db import models
from rest_framework import serializers
from datetime import datetime
# from student.models import Student_Profile,Student_Course
MATERAIL=(
    ("ebooks","E-BOOKS"),
    ("lectures","Online Lecture"),
)
NOTIFICATION=(
    ("class","Class Notification"),
    ("Section","Section Notification"),
    ("program","Program Notification"),
)
STORY_CATEGORY=(
    ("new","NEW"),
    ("old","OLD"),
)

# Create your models here.
class User_Signup(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255,default="")
    email = models.CharField(max_length=100,default="")
    password = models.TextField(default='')
    role=models.CharField(max_length=50,default="null")
    verify=models.CharField(max_length=100,default="unverified")
    def __str__(self):
        return self.username
     

class Instructor(models.Model):
    tid=models.AutoField(primary_key=True)
    username=models.ForeignKey(User_Signup, on_delete=models.CASCADE,default=0)
    First_Name=models.CharField( max_length=255,default='')
    Last_Name=models.CharField(max_length=255,default='')
    Gender=models.CharField(max_length=255,default='')
    Address=models.CharField(max_length=255,default='')
    Phone_Number=models.CharField(max_length=25,default='')
    Dob=models.CharField(max_length=20,default='')
    img=models.ImageField(upload_to='upload/',default="dummy.jpg")

    def __str__(self):
        return self.First_Name
    
class SerTeacher(serializers.ModelSerializer):
    class Meta:
        model= Instructor
        fields=('First_Name','Last_Name','Gender','Address','Phone_Number','Dob')
    

class Department(models.Model):
    Did = models.AutoField(primary_key=True)
    Department_name = models.CharField(max_length=255,default="")
    Dep_Description=models.TextField(default='')
    Instructor_id=models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.Department_name

# Create your models here.
class Semester(models.Model):
    SamesterId=models.AutoField(primary_key=True)
    Samester_Name=models.CharField(max_length=50, default="1st Samester")
    Samester_Code=models.CharField(max_length=20,default="CS001")
    Samester_Year=models.DateField()
    def __str__(self):
        return self.Samester_Name

class Course(models.Model):
    Cid = models.AutoField(primary_key=True)
    Course_name = models.CharField(max_length=255,default="")
    Course_Description=models.TextField(default='')
    Course_code = models.CharField(max_length=20,default="")
    Issue_Date=models.DateTimeField(auto_now_add=True)
    Total_Marks=models.IntegerField(default=0)
    Obtain_Marks=models.IntegerField(default=0)
    MidTerm_Marks=models.IntegerField(default=0)
    Department_id=models.ForeignKey(Department, on_delete=models.CASCADE)
    Instructor_id=models.ForeignKey(Instructor, on_delete=models.CASCADE)
    Semester_id=models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return self.Course_name
  
class Materialclass(models.Model):
    Materailid=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=100, default="Title")
    Category=models.CharField(max_length=100, choices=MATERAIL)
    MaterailFile=models.FileField(upload_to="InstructorMaterials",default="Notdata")
    Course_id=models.ForeignKey(Course, on_delete=models.CASCADE)
    Instructor_id=models.ForeignKey(Instructor, on_delete=models.CASCADE)
    def __str__(self):
        return self.Title


# Assigment Model
class AssigmentModel(models.Model):
    AsssigmentId= models.AutoField(primary_key=True)
    AssigmentTitle=models.CharField(max_length=100, default="Title")
    AssigmentDesc=models.TextField(max_length=400, default="Assigment Description")
    AssigmentFile=models.FileField(upload_to="Assigments/" , default="#")
    Course_id=models.ForeignKey(Course, on_delete=models.CASCADE)
    Instructor_id=models.ForeignKey(Instructor, on_delete=models.CASCADE)

# Notitications Model
class NotificationModel(models.Model):
    NotificationId=models.AutoField(primary_key=True)
    NotificationTitle=models.CharField(max_length=100, default="Notification Title")
    NotificationDesc=models.TextField(max_length=200, default="Notification Description")
    Category=models.CharField(max_length=100, choices=NOTIFICATION,default="")
    Course_id=models.ForeignKey(Course, on_delete=models.CASCADE)
    Instructor_id=models.ForeignKey(Instructor, on_delete=models.CASCADE)
    def __str__(self):
        return self.NotificationTitle

class Teacher_syllabus(models.Model):
    syllabusId=models.AutoField(primary_key=True)
    semester=models.CharField(max_length=100,default="")
    outline=models.FileField(upload_to="Assigments/" , default="#")
    Course_id=models.ForeignKey(Course, on_delete=models.CASCADE)
    Instructor_id=models.ForeignKey(Instructor, on_delete=models.CASCADE)
    Department_id=models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.semester


    
    


# Seralizer list
class CourseSeralizer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields= '__all__'


class InstructorSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'
######Teacher Application

class TeacherApplication(models.Model):
    ApplicationId=models.AutoField(primary_key=True)
    ApplicationTitle=models.CharField(max_length=50, default="Reason Title")
    ApplicationMessage=models.TextField(max_length=350, default="Reason application")
    ApplicationAttachment=models.FileField(upload_to='ApplicationAttachment/',default='reason.pdf')
    ApplicationDate=models.DateTimeField(default=datetime.now(), blank=True)
    ApplicationStatus=models.CharField(max_length=30, default='Pendding')
    Instructor_id=models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.ApplicationTitle

class User_Stories(models.Model):
    storyid=models.AutoField(primary_key=True)
    I_want_to=models.CharField(max_length=200,default="")
    So_that_I_can=models.CharField(max_length=500,default="")
    Category=models.CharField(max_length=100, choices=STORY_CATEGORY)
    Instructor_id=models.ForeignKey(Instructor, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.Instructor_id

class Query_Admin(models.Model):
    queryid=models.AutoField(primary_key=True)
    querytitle=models.CharField(max_length=50, default="Reason Title")
    querymessage=models.TextField(max_length=350, default="Reason query")
    querydate=models.DateTimeField(default=datetime.now(), blank=True)
    querystatus=models.CharField(max_length=30, default='Pendding')
    Instructor_id=models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.Instructor_id


#Course videos
class CourseVideos(models.Model):
    VideoId= models.AutoField(primary_key=True)
    VideoTitle= models.CharField(max_length=100 , default="Video Title")
    VideoDesc= models.TextField(max_length=100, default="Description")
    VideoFile=models.FileField(upload_to="facultyvideo/", default="Video.mp4")
    CourseId=models.ForeignKey(Course,on_delete=models.CASCADE)
    InstructerId=models.ForeignKey(Instructor,on_delete=models.CASCADE)

class Faculty_Development(models.Model):
    Faculty_Development_ID = models.AutoField(primary_key=True)
    Name =  models.CharField(max_length=100 , default="Name")
    Department =  models.CharField(max_length=100 , default="Department")
    Highest_Degree = models.CharField(max_length=100 , default="Degree")
    Subject = models.CharField(max_length=100 , default="Subject")
    Course_you_Teach= models.CharField(max_length=100 , default="Subject")
    Core_Area_to_you_would_like_to_develop = models.CharField(max_length=100 , default="Skills")
    Teacher_Research_Ratio= models.TextField(max_length=450, default="research")
    particular_area_of_work = models.CharField(max_length=100 , default="Area")
    area_of_expertise = models.TextField(max_length=450, default="expertise")
    Instructor_id=models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

class Faculty_Evaluation(models.Model):
    Faculty_Evaluation_ID = models.AutoField(primary_key=True)
    Report_Name = models.CharField(max_length=200, default="Name")
    Report_File = models.FileField(upload_to="report",default="Notdata")
    Department_id=models.ForeignKey(Department, on_delete=models.CASCADE)
    Course_id=models.ForeignKey(Course, on_delete=models.CASCADE)
    InstructerId=models.ForeignKey(Instructor,on_delete=models.CASCADE)

    

class Exam_Result(models.Model):
    Exam_Result_id=models.AutoField(primary_key=True)
    Course_id=models.ForeignKey(Course, on_delete=models.CASCADE)
    Project_Marks = models.IntegerField(default="")
    Quiz_Assignment_Marks = models.IntegerField(default="")
    Midterm_Marks = models.IntegerField(default="")
    Final_Marks = models.IntegerField(default="")
    Total_Marks = models.IntegerField(default="")
    Status = models.CharField(max_length=20,default="null")
    InstructerId=models.ForeignKey(Instructor,on_delete=models.CASCADE)
    Department_id=models.ForeignKey(Department, on_delete=models.CASCADE)
    Student_ID=models.ForeignKey('student.Student_Profile', on_delete=models.CASCADE)
    GPA=models.CharField(max_length=20,default="null")

class onlinequiz(models.Model):
    onlinequizid=models.AutoField(primary_key=True)
    semester=models.CharField(max_length=100,default="")
    Course_id=models.ForeignKey(Course, on_delete=models.CASCADE)
    Instructor_id=models.ForeignKey(Instructor, on_delete=models.CASCADE)
    Department_id=models.ForeignKey(Department, on_delete=models.CASCADE)
    quizlink=models.CharField(max_length=1000,default="link")



    
    
    

    











