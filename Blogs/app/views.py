from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from app.models import Student

# Create your views here.
def homepage(request, id):
    Students = Student.objects.get(id=id)

    Students = Student.objects.all()
    return render(request,'Firstpage.html',{'Students':Students})

def detailpage(request,id):
    Students = Student.objects.get(id=id)
    return render(request,'detail.html',{'Student':Students})
    
def formpages(request):
    if request.method == 'GET':
        return render(request,'form.html')
    else:
        N = request.POST['name']
        E = request.POST['email']
        M = request.POST['message']

        _Student = Student.objects.create(name=N,email=E,message=M)
        _Student.save()
    
        return HttpResponse('Date is stored')


def edit_student(request, id):
    st = Student.objects.get(id=id)
    if request.method == 'POST':
        n = request.POST.get('name')
        e = request.POST.get('email')
        m = request.POST.get('message')
        
        Student_updat = Student.objects.get(id = id)

        Student_updat.name = n
        Student_updat.email = e
        Student_updat.message = m

        # Student_updat = Student.objects.update(name=n,email=e,message=m)
        Student_updat.save()
        
        # return redirect('detail.html', id=id)
        return HttpResponseRedirect(f'/home/{id}')
    
    return render(request, 'Edit.html', {'student': st})

