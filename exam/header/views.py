from django.shortcuts import render
from student.models import Student
# Create your views here.

def vstudent(request):
    student = Student.objects.all()
    print(student)
    return render (request,'view_students.html',{'student_list':student})

def de_students(request):
    student = Student.objects.all()
    print(student)
    return render (request,'delete.html',{'student_details':student})

def del_student(request,student_id):
    student = Student.objects.get(id = student_id)
    students = Student.objects.all()
    student.delete()
    msg='student deletyed succesfully'
    return render (request,'delete.html',{'student_details':students,'status':msg })

def edit(request,mid):
    student = Student.objects.get(id=student_id)
    msg=''
    if request.method=='POST':
        
        student.sname = request.POST['sname']
        student.lname = request.POST['lname']
        student.semail = request.POST['semail']
        student.birthday = request.POST['birthday']
        student.phone = request.POST['phone']
        student.password = request.POST['psw']
        student.address1=request.POST['address1']
        student.address2=request.POST['address2']
        student.save()
        msg='student edited succesfully'

    return render (request,'edit.html',{'student_details':student})