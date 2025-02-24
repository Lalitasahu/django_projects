from datetime import datetime
from app.models import Room, Booking, Profile, Images
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required 
from rest_framework.response import Response  
from rest_framework import status  
from .serializer import RoomSerializer, UserSerializer, BookingSerializer
from rest_framework import viewsets


class RoomSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class UserSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookingSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

@login_required(login_url='/userlogin')
def homepage(request):
    
    profile = Profile.objects.get(user=request.user)
    if profile.is_vendor:
        rooms = Room.objects.filter(user=request.user)
        booking = Booking.objects.filter(user=request.user)
        return render(request, 'Index.html', {'rooms': rooms, 'booking': booking})
    else:
        rooms = Room.objects.all()
        return render(request, 'Index.html', {'rooms': rooms, 'user': request.user})

def DeleteImage(request,id):
    print(request.POST)

    image_ids = request.POST.getlist('images')

    for _id in image_ids:
        # breakpoint()
        img = Images.objects.get(id = _id)
        # breakpoint()
        img.delete()

    return HttpResponseRedirect(f'/room_edit/{id}')

def detail(request,id):
    rooms = Room.objects.get(id=id)
    return render(request, 'detail.html',{'rooms':rooms})

def room_edit(request,id, Add_rooms=True):
    rooms = Room.objects.get(id=id)
    booking = None  # Initialize `booking` to avoid the error
    # print(request.POST)
    if request.method == 'POST':
        R_no = request.POST['Room_no']
        R_type = request.POST['Room_type']
        R_description = request.POST['Room_description']
        P_p_night = request.POST['Price_per_night']
        R_available = request.POST['Room_available']  
        room_pic = request.FILES.getlist('image')

        # update the informatio
        rooms.Room_no = R_no
        rooms.Room_type = R_type
        rooms.Room_description = R_description
        rooms.Price_per_night = P_p_night
        rooms.Room_available = R_available
        
        rooms.save() 
        for  img in room_pic:
            image = Images.objects.create(room=rooms,image=img)

        profile = Profile.objects.get(user=request.user)
        if profile.is_vendor:
            booking = Booking.objects.all()
            return HttpResponseRedirect('/')
     
    return render(request, 'Bookingform.html', {'rooms':rooms, 'booking':booking, 'Add_rooms':Add_rooms})

def Add_rooms(request):
    rooms = Room.objects.all()
    if request.method == 'GET':
        return render(request, 'Bookingform.html', {'rooms': rooms})
    R_no = request.POST['Room_no']
    R_type = request.POST['Room_type']
    R_description = request.POST['Room_description']
    P_p_night = request.POST['Price_per_night']
    R_available = request.POST['Room_available']
    room_pic = request.FILES.getlist('image')
    rooms = Room.objects.create( Room_no= R_no, Room_type= R_type, Room_description=R_description, 
                                Price_per_night=P_p_night,Room_available=R_available,user = request.user)
    rooms.save()
    for  img in room_pic:
        images = Images.objects.create(room=rooms,image=img)

    return HttpResponseRedirect('/')

def delete_rooms(request,id):
    rooms = Room.objects.get(id=id)
    rooms.delete()
    return HttpResponseRedirect('/')

@login_required(login_url='/userlogin')
def booking_history(request):
    try:
        profile = Profile.objects.get(user=request.user)
        if profile.is_vendor:
            booking = Booking.objects.all()        
    except Profile.DoesNotExist:
        return HttpResponseRedirect('/userlogin')
    return render(request, 'booking_history.html', {'booking': booking})

def check_out_view(request,id):
    booking = get_object_or_404(Booking, id=id)
    return render(request,  'booking_history.html', {'booking':booking})


@login_required(login_url='/userlogin')
def cancel_booking(request,id):
    booking = Booking.objects.get(id=id)
    booking.status = "Cancelled"
    booking.Room.Room_available = True
    booking.Room.save()
    booking.save()
    return HttpResponseRedirect('/')

@login_required(login_url='/userlogin')
def check_out(request,id):
    booking = Booking.objects.get(id=id)
    booking.status = "Completed"
    booking.Room.Room_available = True
    booking.Room.save()
    booking.save()
    return HttpResponseRedirect('/')

def detail_confirm_booking(request,id):
    booking = Booking.objects.get(id=id)
    return render(request, 'detail_confirm_booking.html', {'booking':booking})

@login_required(login_url='/userlogin')
def Confirm_booking(request, id):
    room = get_object_or_404(Room, id=id)
    
    if request.method == "POST":
        check_in_date = request.POST.get('Check_in')
        check_out_date = request.POST.get('Check_out')
        N_of_Person = int(request.POST.get('Num_of_Person'))
        room_price = int(room.Price_per_night)
        total_price = N_of_Person * room_price
        status = request.POST.get('status')
        # Create a booking
        booking = Booking.objects.create(
            Room=room,
            user=request.user,  
            Booking_date=now(),
            Check_in=check_in_date,
            Check_out=check_out_date,
            Num_of_Person=N_of_Person,
            Total_price=total_price,
            status = status
        )
        booking.save()
        room.Room_available = False
        room.save()
        return HttpResponseRedirect('/')
    return render(request, 'book.html', {'room': room, 'price_per_night': room.Price_per_night})


def Edit_confirm_booking(request, id):
    booking = get_object_or_404(Room, id=id)
    room = get_object_or_404(Room, id=id)
    if request.method == "POST":
        check_in_date = request.POST.get('Check_in')
        check_out_date = request.POST.get('Check_out')
        status = request.POST.get('status')
        N_of_Person = int(request.POST.get('Num_of_Person'))
        room_price = int(room.Price_per_night)
        total_price = N_of_Person * room_price
        # update the date
        booking.Check_in = check_in_date
        booking.Check_out = check_out_date
        booking.Total_price = total_price
        booking.Num_of_Person = N_of_Person
        booking.room.id = room
        booking.status = status
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
        # print(request.POST)
        # print(request.FILES['image'])
        username = request.POST['username']
        last_name = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']
        phone_no = request.POST['phone_number']
        is_vendor = request.POST['is_vendor']
        profile_pic = request.FILES['image']

        if User.objects.filter(username=username).exists():
            return HttpResponse("Error: Username already exists. Please enter another username.")

        user = User.objects.create(
            username=username,
            last_name=last_name,
            email=email
        )
        user.set_password(password)
        user.save()

        profile = Profile.objects.create(
            phone_number = phone_no,
            is_vendor = is_vendor,
            profile_pic = profile_pic,
            user = user
        )
        profile.save()

        return HttpResponseRedirect("/")
    else:
        return render(request,'createuser.html')


def get_profile(request):
    return render(request,'profile.html',{'user':request.user})