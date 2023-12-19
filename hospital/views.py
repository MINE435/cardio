from django.shortcuts import render
from .models import Slider, Service, Doctor
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render
from .models import Appointment  # Import the Appointment model
from django.contrib.auth.decorators import login_required
class HomeView(ListView):
    template_name = 'hospital/index.html'
    queryset = Service.objects.all()
    context_object_name = 'services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['sliders'] = Slider.objects.all()
        context['experts'] = Doctor.objects.all()
        return context



def aboutus_view(request):
    return render(request, 'hospital/aboutus.html')



# You can keep other frontend-related views as needed.
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def doctor(request):
    return render(request,'heart/doctor.html')

@login_required
def appointment(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        doctor = request.POST.get('doctor')
        date = request.POST.get('Date')
        time = request.POST.get('Time')
        mobile_number = request.POST.get('mobile_number')
        message = request.POST.get('message')
        print(doctor)
        print("---------------------------------------")
        print(mobile_number)
        print(date)
        # Check if the required fields are not empty before saving
            # Save the data to the Appointment model
        appointment = Appointment(patient_name=patient_name,doctor=doctor,date=date,time=time,mobile_number=mobile_number,message=message)
            # Optionally, you can also save the appointment instance to update the database
        appointment.save()
        return redirect('success')
        
        
         # Create an error page to inform the user

    return render(request, 'heart/appointment.html')

    
def cardiologist(request):
    return render(request,'heart/cardiologist.html')
def ecg(request):
    return render(request,'heart/ecg.html')
def seniorheartsurger(request):
    return render(request,'heart/seniorheartsurger.html')    
def gallery(request):
    return render(request,'heart/gallery.html') 
def home(request):
    return render(request,'heart/home.html')
def succes(request):
    return render(request,'heart/sucess.html')
    
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login_user')
    return render(request, 'register.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']  # Corrected this line

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Corrected this line
            return redirect('index')
        else:
            return render(request, 'login.html')    

    return render(request, 'login.html')

def logout_user(request):
    logout(request)  
    return redirect('home')  # Corrected this line
          