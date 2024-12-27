from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import generic
from .models import GymClass, Booking
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
class ClassesList(generic.ListView):
    queryset = GymClass.objects.all()
    template_name = "Classes/index.html"
    context_object_name = 'gym_classes'
    paginate_by = 6

@login_required
def newBooking(request, gym_class_id):
    gym_class = get_object_or_404(GymClass, id=gym_class_id)  # Fetch the GymClass instance
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Create the booking object but don't save it yet
            booking = form.save(commit=False)
            booking.user = request.user  # Assign the logged-in user to the booking
            booking.gym_class = gym_class  # Assign the GymClass to the booking
            booking.date = gym_class.date  # Assuming GymClass has a 'date' field
            booking.time = gym_class.time  # Assuming GymClass has a 'time' field
            booking.save()
            # Add a success message
            messages.success(
                request,
                f"Your booking for {gym_class.name} on {gym_class.date} at {gym_class.time} has been confirmed! "
                f"<a href='/edit-booking/{booking.id}/' class='btn btn-primary btn-sm'>Edit Booking</a> "
                f"<a href='/delete-booking/{booking.id}/' class='btn btn-danger btn-sm'>Delete Booking</a>",
                extra_tags='booking'
            )
            return redirect('booking_list')  # Redirect to booking list or desired success URL
    else:
         # Prepopulate the form with the GymClass date and time
        form = BookingForm(initial={'gym_class': gym_class})  
    
    return render(request, 'Classes/booking_form.html', {'form': form, 'gym_class': gym_class})

class BookingListView(LoginRequiredMixin, generic.ListView):
    model = Booking
    template_name = "Classes/booking_list.html"
    context_object_name = "bookings"

    def get_queryset(self):
        # Filter bookings for the logged-in user
        return Booking.objects.filter(user=self.request.user).order_by('gym_class__date', 'gym_class__time')

@login_required
def edit_booking(request, booking_id):
    # Fetch the booking object, ensure it belongs to the logged-in user
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking has been updated!", extra_tags='booking')
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    
    return render(request, 'Classes/edit_booking.html', {'form': form, 'booking': booking})

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    messages.success(request, "Your booking has been deleted.", extra_tags='booking')
    return redirect('booking_list')