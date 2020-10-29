from django.shortcuts import render,redirect
from .models import Studentdatabase
from .forms import StudentForm,StudentupdateForm,StudentDeleteForm
from django.http.response import HttpResponse
from django.contrib import messages

# Create your views here.
def home_view(request):

    context ={}
    return render(request, 'CurdOperation/index.html', context)


def Create_view(request):
    if request.method == 'POST':
        student = StudentForm(request.POST)
        if student.is_valid():
            Roll_number = request.POST.get('Roll_number')
            First_name = request.POST.get('First_name')
            Last_name = request.POST.get('Last_name')
            Email = request.POST.get('Email')
            School_name = request.POST.get('School_name')
            Class_name = request.POST.get('Class_name')
            Section_name = request.POST.get('Section_name')
            Telugu_marks = request.POST.get('Telugu_marks')
            Hindi_marks = request.POST.get('Hindi_marks')
            English_marks = request.POST.get('English_marks')
            Maths_marks = request.POST.get('Maths_marks')
            Science_marks = request.POST.get('Science_marks')
            Social_marks = request.POST.get('Social_marks')
            data = Studentdatabase(
                Roll_number=Roll_number,
                First_name=First_name,
                Last_name=Last_name,
                Email=Email,
                School_name=School_name,
                Class_name=Class_name,
                Section_name=Section_name,
                Telugu_marks=Telugu_marks,
                Hindi_marks=Hindi_marks,
                English_marks=English_marks,
                Maths_marks=Maths_marks,
                Science_marks=Science_marks,
                Social_marks=Social_marks
            )
            data.save()
            student = StudentForm()
            context = {'student': student}
            return render(request, 'CurdOperation/Createpage.html', context)


        else:
            return HttpResponse('Invalid Data')
            
    else:
        student = StudentForm()
        context ={'student':student}
        return render(request,'CurdOperation/Createpage.html',context)


def Retrieve_view(request):
    student = Studentdatabase.objects.all()
    context = {'student':student}
    return render(request, 'CurdOperation/Retrievepage.html', context)





def Update_view(request):
    if request.method == 'POST':
        student = StudentupdateForm(request.POST)
        if student.is_valid():
            Roll_number = request.POST.get('Roll_number')
            Section_name = request.POST.get('Section_name')
            sid = Studentdatabase.objects.filter(Roll_number=Roll_number)
            if not sid:
                return HttpResponse('Not data')
            else:
                sid.update(Section_name=Section_name)
                student = StudentupdateForm()
                context = {'student': student}
                return render(request, 'CurdOperation/Upadtepage.html', context)

    else:
        student = StudentupdateForm()
        context = {'student':student}
        return render(request,'CurdOperation/Upadtepage.html',context)


def delete_view(request):
    if request.method == 'POST':
        student = StudentDeleteForm(request.POST)
        if student.is_valid():
            Roll_number = request.POST.get('Roll_number')
            sid = Studentdatabase.objects.filter(Roll_number=Roll_number)

        if not sid:
            sid.delete()
            student=StudentDeleteForm()
            context = {'student':student}
            return render(request,'CurdOperation/Deletepage.html',context)
        else:
            messages.warning(request,'Incorrect Employee Id')
            return redirect('delete')




    else:
        student = StudentDeleteForm()
        context = {'student': student}
        return render(request,'CurdOperation/Deletepage.html',context)
