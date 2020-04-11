import re
from django.shortcuts import render,redirect
from GymManagement.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib import messages
from email_validator import validate_email, EmailNotValidError
from .models import Register,Contact,Reviews
from .forms import demo

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        if name.isdigit():
            messages.error(request,'Enter valid name')
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if regex.search(name):
            messages.error(request, 'Name cannot have special characters')
            return redirect('contact')
        if Reviews.objects.filter(email=email).exists():
            messages.error(request, 'Review is already submitted by using this Email ID')
            return redirect('index')
        try:
            v = validate_email(email)
            val_email = v["email"]
        except EmailNotValidError as e:
            messages.error(request, 'Invalid Email ID')
            return redirect('admin_add_user')
        data = Reviews(name=name, email=email, message=message)
        data.save()
        messages.success(request,'Review submitted successfully')

    return render(request,'GymPages/index.html')

def courses(request):
    return render(request,'GymPages/classes.html')


# Single class
def single(request,id):
    if id == 1:
        img =1;
        name = "Kettlebell"
        time = '9.00 - 10.00'
        notes = "You're building muscle, increasing power endurance, and getting lean all at once. By bridging the gap between cardio and strength training," \
                " your overall physical fitness levels will skyrocket, getting you to the best shape of your life"
    if id ==2:
        img=2;
        name = "Conjugate methods"
        time = '10.00 - 11.00'
        notes = "The conjugate system sees you utilize the same movement pattern over and over, but frequently varies how you train that pattern. So while you may " \
                "know that the main lift in a given workout will be a squat, it could be a Front Squat, Zercher Squat, Back Squat, etc"
        print(time)
    if id == 3:
        img = 3;
        name = "Advanced Gymnastic"
        time = '10.00 -12.00'
        notes = "Gymnastics is a sport that includes exercises requiring balance, strength, flexibility, agility, coordination, and endurance. The movements involved " \
                "in gymnastics contribute to the development of the arms, legs, shoulders, back, chest, and abdominal muscle groups. Alertness, precision, " \
                "daring, self-confidence, and self-discipline are mental traits that can also be developed through gymnastics"
    if id == 4:
        img =4;
        name = "Normal Excercises"
        time = '4.00 - 5.00'
        notes = "Best for chest exercise: The push-up, Best exercise for glutes: The squat, Best exercise for abs: The bicycle manoeuvre," \
                "Best exercise for the back: Pull-up, Best exercise for hamstrings: Swiss ball hamstring curl,Best exercise for thighs: The lunge"
    if id == 5:
        img =5
        name ="Body Pump"
        time = '5.00 - 7.00'
        notes = "In a nutshell, BODYPUMP is a 30-, 45-, or 55-minute resistance workout that uses a barbell with very light weights and very high reps. ... During the workout, " \
                "you go through five or " \
                "six specific exercises, in different combinations, and end up completing approximately 800 to 1000 reps in one 55-minute session"
    if id == 6:
        img =6
        name ="Cardio"
        time = '7.00 - 9.00'
        notes = "40-Minute Walking and Running Workout: The fastest pace in this workout is 5.8 miles per hour, and the running intervals never top two minutes. " \
                "60-Minute Workout Mixing Walking and Jogging: Perfect for when you're ready to push your endurance, this hour-long workout will burn close to 300 calorie"

    context ={
        'name' :name,
        'time':time,
        'notes':notes,
        'img':img,
    }

    if request.method == 'POST':
        event = request.POST['event']
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        state = request.POST['stt']
        district = request.POST['district']
        address = request.POST['address']

        if name.isdigit():
            messages.error(request,"Name is not valid")
            print("errror")
            return redirect('single',id)
        data = Register(event=event,name=name,phone=mobile,email=email,state=state,district=district,address=address)
        data.save()
        messages.success(request,"Successfully submitted")


    return render(request,'GymPages/single_class.html',context)


def contact(request):
    if request.method == 'POST':
        print('start')
        name = request.POST['name']
        user_mob = request.POST['phone']
        user_message = request.POST['message']
        message2 ="Message from Admin : Thanks for your response ! We will go through your requirements"
        phone = "For any queries you can contact : 9539247954 "
        email = request.POST['email']
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if regex.search(name):
            messages.error(request, 'Name cannot have special characters')
            return redirect('contact')
        try:
            v = validate_email(email)
            val_email = v["email"]
        except EmailNotValidError as e:
            messages.error(request, 'Invalid Email ID')
            return redirect('contact')
        data = Contact(name=name, phone=user_mob, email=email, message=user_message)
        data.save()

        send_mail(message2,phone,EMAIL_HOST_USER,[email],fail_silently=False)
        print('sucess')
        messages.success(request,"Successfully submitted")
        return render(request,'GymPages/contact.html')

    return render(request,'GymPages/contact.html')


def about(request):
    return render(request,'GymPages/about.html')


# DEMO

def Demo(request):
    form = demo()
    context ={
        'form' :form,
    }
    return render(request,'GymPages/demo.html',context)

#features
def feature(request):
    return render(request,'GymPages/features.html')