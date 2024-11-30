

from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from app.models import Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Display all students
def home(request):
    stud = Student.objects.all()
    return render(request, 'Indexpage.html', {'stud': stud})

def detail(request,id):
    student = Student.objects.get(id = id)
    return render(request, 'detail.html', {'student':student})



def Userlogout(request):
    logout(request)
    return HttpResponseRedirect("/")


def Userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/")
            # return HttpResponse("user and password is correct")
        else:
            return HttpResponse("user or password is not valid")

    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        return render(request,'login.html')


def createUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            # password=password,
            email=email
        )

        user.set_password(password)

        user.save()
        return HttpResponseRedirect("/")


    else:
        return render(request,'createuser.html')



def New_student(request):
    # st = Student.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'st_form.html')

    else:
        request.method == "POST"
        n = request.POST['name']
        a = request.POST['address']
        p = request.POST['phone_no']

        stud = Student.objects.create(name=n, address=a, phone_no=p)
        stud.save()

        return HttpResponse('Successfully Saved')


def edit_info(request, id):
    Info_update = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        n = request.POST['name']
        a = request.POST['address']
        p = request.POST['phone_no']

        # Update student details
        Info_update.name = n
        Info_update.address = a
        Info_update.phone_no = p
        Info_update.save()

        # Redirect back to home page
        return HttpResponseRedirect('/')

    # Render the form pre-filled with the student's data
    return render(request, 'st_form.html', {"Info_update": Info_update})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()  
    return HttpResponseRedirect('/')