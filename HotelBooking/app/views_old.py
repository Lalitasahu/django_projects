# from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
# from django.contrib.auth.decorators import login_required


from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from app.models import Room, Booking
from datetime import datetime


def homepage(request):
    rooms = Room.objects.all()
    # rooms = Room.objects.filter(Room_available=True)  # Use the correct field
    return render(request, 'Index.html',{'rooms':rooms})



def detail(request,id):
    room = Room.objects.get(id=id)
    return render(request, 'detail.html',{'room':room})

def booking_confirmation(request, id):
    booking = get_object_or_404(Booking, id=id)
    return render(request, 'confirm_booking.html', {'booking': booking})

def room_booking(request):
    # Fetch the specific room using its ID
    # room = get_object_or_404(Room)
    room = Room.objects.all()

    if request.method == 'GET':
        # Render the booking form for the selected room
        return render(request, 'Bookingform.html', {'room': room})

    elif request.method == 'POST':
        # Ensure the form has submitted both 'Check_in' and 'Check_out' fields
        check_in = request.POST.get('Check_in')
        check_out = request.POST.get('Check_out')

        if not check_in or not check_out:
            return render(request, 'Bookingform.html', {'room': room, 'error': 'Please fill in both dates.'})

        # Convert strings to date objects
        check_in_date = datetime.strptime(check_in, '%Y-%m-%d').date()
        check_out_date = datetime.strptime(check_out, '%Y-%m-%d').date()

        # Calculate the total number of days and price
        days = (check_out_date - check_in_date).days
        if days <= 0:
            return render(request, 'Bookingform.html', {'room': room, 'error': 'Check-out date must be after check-in date.'})

        total_price = days * room.Price_per_day

        # Create a booking entry
        booking = Booking.objects.create(
            customer=request.user,
            room=room,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            total_price=total_price,
            status='Pending'
        )
        booking.save()

    
        return HttpResponseRedirect('booking:booking_confirmation',{'booking':booking} )



# def room_booking(request):
#     # room = get_object_or_404(Room)
#     room = Room.objects.all()
#     if request.method == 'GET':
#         return render(request, 'Bookingform.html', {'room': room})
#     request.method == 'POST'
#     check_in = request.POST['Check_in']
#     check_out = request.POST['Check_out']
#     check_in_date = datetime.strptime(check_in, '%Y-%m-%d').date()
#     check_out_date = datetime.strptime(check_out, '%Y-%m-%d').date()
#     days = (check_out_date - check_in_date).days
#     total_price = days * room.Price_per_day
#     # Create a booking entry
#     booking = Booking.objects.create(
#         customer=request.user,
#         room=room,
#         check_in_date=check_in_date,
#         check_out_date=check_out_date,
#         total_price=total_price,
#         status='Pending'
#     )
#     return HttpResponseRedirect('booking:booking_confirmation', booking.id)

    

# def room_booking(request):
#     if request.method == 'GET':
#         return render(request, 'Bookingform.html')
#     else:
#         R_no = request.POST['Room_no']
#         R_type = request.POST['Room_type']
#         R_description = request.POST['Room_description']
#         P_p_day = request.POST['Price_per_day']
#         R_available = request.POST['Room_available']
#         rooms = Room.objects.create( Room_no= R_no, Room_type= R_type, Room_description=R_description, Price_per_day=P_p_day,
#                                     Room_available=R_available)

#         rooms.save()

#         return HttpResponseRedirect('/')
