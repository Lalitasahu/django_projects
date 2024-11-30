from django.shortcuts import render, HttpResponse
from app.models import Blog

# Create your views here.
def HomePage(request):
    Title = "<h3> model (data layer) view (logic layer) and template (presentation layer) interact is crucial. <h3>"
    return HttpResponse(Title)
    


def createForm(request):
    if request.method == 'GET':
        return render(request,'create_form.html')
    else:
        t = request.POST['title']
        d = request.POST['discription']
        u = request.POST['User']

        blog = Blog.objects.create(title=t,discription=d, User=u)
        blog.save()

        return HttpResponse('Blog is created')


def Aboutpage(request):
    # about = 'Learn how Django handles HTTP requests and sends responses, including the role of middleware in processing requests and responses.'
    # return HttpResponse(about)
    blogs = Blog.objects.all()
    return render(request, 'index.html' ,{'blogs':blogs})

def SumPro(request,val1,val2):
    sum = val1+val2
    return HttpResponse(sum)

def SubPro(request,val1,val2):
    if val1 >val2:
        sub = val1 - val2
    else:
        sub = 'Value is not Correct'
    return HttpResponse( f'this is the final output after cut the value of {val1} and {val2} then final {sub}')

def MultProduct(request,val1,val2):
    multi = val1*val2
    return HttpResponse(multi)

def prime(request,val1):
    flag=False
    for i in range(2,val1):
        if val1%i==0 :        
            flag=True
            break
    if flag == True:
        return HttpResponse("This is not prime")
    else: 
        return HttpResponse("This is pirme")


def pattern(request,val1):
    response_text = ""
    for i in range(val1+1):
        for j in range(1, i + 1):
            # response_text += "*"
            response_text += str(i)
        response_text += "<br>" 
    return HttpResponse(response_text)


def series(request,val1,val2):
    series = list(range(val1, val2+1))  
    output = ', '.join(map(str, series))  
    # return HttpResponse(f"Series: {output}")
    return HttpResponse(output)
 

# def create():
    # get the value by form 
    # show the data on the home page 
    