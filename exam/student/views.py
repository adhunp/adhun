from django.shortcuts import render,redirect
from student.models import Student
# Create your views here.


def regisert(request):
    if request.method== 'POST':

        sname = request.POST['sname']
        lname = request.POST['lname']
        semail = request.POST['semail']
        birthday = request.POST['birthday']
        phone = request.POST['phone']
        password = request.POST['psw']
        address1=request.POST['address1']
        address2=request.POST['address2']

        email_exist = Student.objects.filter(semail=semail).exists()
        if not email_exist:

            obj = Student(sname=sname,
                           lname=lname,
                           semail=semail,
                           sdob=birthday,
                           sphone=phone,
                           address1=address1,
                           address2=address2,
                           password=password,
                        # teacher_id = request.session['teacher_id']
                        )
            obj.save()
        else:
            msg="" 
    
    return render (request,'registration.html')

def login(request):
     if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw'] 

        try:
            slogin = Student.objects.get(semail=username,password=password)
            request.session['student_id']=slogin.id
            return redirect("student:home")

        except:
            msg = "invalid username or password"
            
            return render(request,"login.html",{"error_message":msg})
     return render (request,'login.html')


def home(request):
    return render (request,'home.html')

