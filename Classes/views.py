from django.shortcuts import render
from django.views import generic
from .models import GymClass, Booking
from .forms import BookingForm

# Create your views here.
class ClassesList(generic.ListView):
    queryset = GymClass.objects.all()
    template_name = "Classes/index.html"
    context_object_name = 'gym_classes'
    paginate_by = 6

#@login_required
def newBooking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Assign the logged-in user to the booking
            booking.save()
            return redirect('booking_list')  # Redirect to booking list or desired success URL
    else:
        form = BookingForm()

    return render(request, 'Classes/booking_form.html', {'form': form})