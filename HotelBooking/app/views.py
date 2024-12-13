from datetime import datetime
from app.models import Room, Booking
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required 
 

def homepage(request):
    rooms = Room.objects.all()  
    return render(request, 'Index.html',{'rooms':rooms,'user':request.user})

def detail(request,id):
    rooms = Room.objects.get(id=id)
    return render(request, 'detail.html',{'rooms':rooms})

def Booking_edi(request,id):
    rooms = Room.objects.get(id=id)
    if request.method == 'POST':
        R_no = request.POST['Room_no']
        R_type = request.POST['Room_type']
        R_description = request.POST['Room_description']
        P_p_night = request.POST['Price_per_night']
        R_available = request.POST['Room_available']  
        # update the informatio
        rooms.Room_no = R_no
        rooms.Room_type = R_type
        rooms.Room_description = R_description
        rooms.Price_per_night = P_p_night
        rooms.Room_available = R_available
        rooms.save()    
        return HttpResponseRedirect('/')
    return render(request, 'Bookingform.html', {'rooms':rooms})

# @login_required(login_url='/userlogin')
def Add_rooms(request):
    rooms = Room.objects.all()
    if request.method == 'GET':
        return render(request, 'Bookingform.html', {'rooms': rooms})
    R_no = request.POST['Room_no']
    R_type = request.POST['Room_type']
    R_description = request.POST['Room_description']
    P_p_night = request.POST['Price_per_night']
    R_available = request.POST['Room_available']
    rooms = Room.objects.create( Room_no= R_no, Room_type= R_type, Room_description=R_description, Price_per_night=P_p_night,Room_available=R_available)
    rooms.save()
    return HttpResponseRedirect('/')

def delete_rooms(request,id):
    rooms = Room.objects.get(id=id)
    rooms.delete()
    return HttpResponseRedirect('/')

@login_required(login_url='/userlogin')
def booking_history(request):
    if request.user.is_authenticated:
        booking = Booking.objects.filter(user=request.user)
    return render(request,  'booking_history.html', {'booking':booking})

def detail_confirm_booking(request,id):
    booking = Booking.objects.get(id=id)
    return render(request, 'detail_confirm_booking.html', {'booking':booking})

@login_required(login_url='/userlogin')
def Confirm_booking(request, id):
    room = get_object_or_404(Room, id=id)
    
    if request.method == "POST":
        check_in_date = request.POST.get('Check_in')
        check_out_date = request.POST.get('Check_out')
        # total_price = request.POST.get('Total_price')
        total_price = (datetime.strptime(check_out_date, '%Y-%m-%d') - datetime.strptime(check_in_date, '%Y-%m-%d')).days * room.Price_per_night
        # Create a booking
        booking = Booking.objects.create(
            Room=room,
            user=request.user,  
            Booking_date=now(),
            Check_in=check_in_date,
            Check_out=check_out_date,
            Total_price=total_price,
        )
        booking.save()
        room.Room_available = False
        room.save()
        return HttpResponseRedirect('/')
    return render(request, 'book.html', {'room': room})

def Edit_confirm_booking(request, id):
    booking = get_object_or_404(Room, id=id)
    room = get_object_or_404(Room, id=id)
    if request.method == "POST":
        check_in_date = request.POST.get('Check_in')
        check_out_date = request.POST.get('Check_out')
        # total_price = request.POST.get('Total_price')
        total_price = (datetime.strptime(check_out_date, '%Y-%m-%d') - datetime.strptime(check_in_date, '%Y-%m-%d')).days * room.Price_per_night
        # update the date
        booking.Check_in = check_in_date
        booking.Check_out = check_out_date
        booking.Total_price = total_price
        booking.room.id = room
        booking.reques.user = User
        booking.save()
        return HttpResponseRedirect('/')
    return render(request, 'book.html', {'booking': booking})
    
def Delete_confirm_booking(request,id):
    booking = Booking.objects.get(id=id)
    booking.delete()
    return HttpResponseRedirect('/')
    # return render(request, 'booking_history.html', {'booking':booking})

def userlogout(request):
    logout(request)
    return HttpResponseRedirect("/")

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('User or password is not valid')
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return render(request,'loginpage.html')


def createuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        last_name = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create(
            username=username,
            last_name=last_name,
            email=email
        )
        user.set_password(password)
        user.save()
        return HttpResponseRedirect("/")
    else:
        return render(request,'createuser.html')


    
    
    

    