from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import GymClass, Booking
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ClassesList(generic.ListView):
    queryset = GymClass.objects.all()
    template_name = "Classes/index.html"
    context_object_name = 'gym_classes'
    paginate_by = 6

#@login_required
def newBooking(request, gym_class_id):
    gym_class = get_object_or_404(GymClass, id=gym_class_id)  # Fetch the GymClass instance
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Assign the logged-in user to the booking
            booking.gym_class = gym_class  # Assign the GymClass to the booking
            booking.save()
            return redirect('booking_list')  # Redirect to booking list or desired success URL
    else:
        form = BookingForm(initial={'gym_class': gym_class})  # Prepopulate the form with GymClass
    
    return render(request, 'Classes/booking_form.html', {'form': form, 'gym_class': gym_class})

class BookingListView(LoginRequiredMixin, generic.ListView):
    model = Booking
    template_name = "Classes/booking_list.html"
    context_object_name = "bookings"

    def get_queryset(self):
        # Filter bookings for the logged-in user
        return Booking.objects.filter(user=self.request.user)