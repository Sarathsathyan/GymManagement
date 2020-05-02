import re
# import pyrebase
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render,redirect
from GymManagement.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from email_validator import validate_email, EmailNotValidError
from django.db.models import Count
from payTm import Checksum
from .models import Contact,Reviews,demo,UserDetails,Register,Courses,customer,payments,OrderUpdate,transformation
from .forms import Demo,AddUserForm,UserLoginForm


MERCHANT_KEY = 'gVbSDvTr7S7mnC1P'
# Create your views here.

# #Firebase API Credentials
# config ={
#
#     'apiKey': "AIzaSyBGHsy7yNPBemEe4Je5kzm-zraVHZ-JQHg",
#     'authDomain': "gymmanagement-f6be8.firebaseapp.com",
#     'databaseURL': "https://gymmanagement-f6be8.firebaseio.com",
#     'projectId': "gymmanagement-f6be8",
#     'storageBucket': "gymmanagement-f6be8.appspot.com",
#     'messagingSenderId': "590822032005",
#     'appId': "1:590822032005:web:96ed5324be302affbc9fec",
#     'measurementId': "G-TSSEP6FNQR"
# }
# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()


###################
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

def Demos(request):
    form = Demo()
    if request.method == 'POST':
        print("submit")
        name = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST['email']
        mobile = request.POST['mobile']
        cname = request.POST['cname']
        number = request.POST['num']
        software = request.POST['soft']
        business = request.POST.get('business')
        print(business)
        messages.success(request,"Submitted successfully ! Admin will contact you")
        data = demo(firstname=name,lastname=lastname,email=email,)
    context ={
        'form' :form,
    }
    return render(request,'GymPages/demo.html',context)

#features
def feature(request):
    return render(request,'GymPages/features.html')

#resources

def resources(request):
    return render(request,'GymPages/resources.html')


#ADD USER

def adduser(request):

    form  = AddUserForm()
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        mobile = request.POST['user_phone']
        username = request.POST['username']
        gender = request.POST['user_gender']
        password = request.POST['password']
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'That email is being used')
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'That username is being used')
            return redirect('register')
        if firstname.isdigit():
            messages.error(request, 'Firstname cannot have numbers')
            return redirect('register')
        if regex.search(firstname):
            messages.error(request, 'Firstname cannot have special characters')
            return redirect('register')
        if lastname.isdigit():
            messages.error(request, 'Lastname cannot have numbers')
            return redirect('register')
        if regex.search(lastname):
            messages.error(request, 'Lastname cannot have special characters')
            return redirect('register')

        try:

            user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname,
                                            last_name=lastname)
            user.save()
            print("saved")
            u_id = User.objects.get(username=username)
            print(u_id)
            addusr = UserDetails(user_id=u_id, user_phone=mobile, user_gender=gender,
                                 user_password=password
                                 )
            addusr.save()
            messages.success(request, "Registered successfully")
            redirect(adduser)

        except:
            usr = User.objects.get(username=username)
            usr.delete()
            messages.error(request,'Some error occured')
            redirect(adduser)

    context ={
        'form' :form
    }
    return render(request,'GymPages/register.html',context)


def Login(request):

    if request.method == 'POST':

        form = AuthenticationForm(request,data =  request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request,'GymPages/login.html',{'form':form})

def Logout(request):
    logout(request)
    messages.info(request,"Loggedout successfully")
    return redirect('index')

def courses(request):
    user = request.user
    print(user.id)
    course = Courses.objects.all()
    context ={
        'course':course,
        'id': user.id,
    }
    return render(request,'GymPages/classes.html',context)


# Single class

def single(request,c_id):
    u_id = request.user
    print(u_id)
    u_id =u_id.id
    user = User.objects.all()
    customers = customer.objects.all()
    courses = Courses.objects.all()
    print(c_id)
    data = Courses.objects.get(id = c_id)
    context ={
        'data':data
    }


    if request.method == 'POST':
        event = request.POST['event']
        state = request.POST['stt']
        district = request.POST['district']
        address = request.POST['address']
        print(event)
        try:
            if Register.objects.get(u_id_id=u_id,event=event):
                messages.error(request,"already registered for this course")
                return redirect('classes')
        except:
            data = Register(u_id_id=u_id, event=event, state=state, district=district, address=address)
            data.save()
            # data2 = customer(user_id=temp1, course_id=temp2)
            # data2.save()
            messages.success(request, "Successfully submitted")
            return redirect('payment')

        # usr = UserDetails.objects.get(id=u_id)
        # temp1 = User.objects.get(username=usr)
        # temp2 = Courses.objects.get(id=c_id)
        # if customer.objects.filter(user_id=temp1).exists():
        #     messages.error(request, 'That intern has an internship')
        #     return redirect('classes')
        # data = Register(u_id_id=u_id,event=event,state=state,district=district,address=address)
        # data.save()
        # data2 = customer(user_id=temp1, course_id=temp2)
        # data2.save()
        # messages.success(request,"Successfully submitted")


    return render(request,'GymPages/single_class.html',context)

# Customer Registered Courses

def customer_courses(request):
    user = request.user
    try:
        registered_course = Register.objects.filter(u_id=user.id)

        if registered_course:
            context={
                'registered' : registered_course,
            }

            return render(request,'GymPages/customer_registered_courses.html',context)
    except:

        return render("registered_course")
    messages.error(request, 'No registered courses now')
    return render(request,'GymPages/customer_registered_courses.html')

# PAYMENT SECTION
def Payment(request):
    user = request.user

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        state = request.POST['stt']
        district = request.POST['district']
        zipcode = request.POST['zip']
        amount = request.POST['amount']

        order = payments(u_id_id=user.id,name=name,email=email,address=address1,address2=address2,state=state,
                         city=district,zip=zipcode,amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.id
        param_dict={
            'MID': 'NwKVhn07526161221188',
            'ORDER_ID': str(order.id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',
        }
        print("hai")
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict,MERCHANT_KEY)
        return render(request,'GymPages/paytm.html',{"param_dict":param_dict})

    return render(request,'GymPages/payments.html')
@csrf_exempt
def handlerequest(request):
    #paytm will send post request
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    print(response_dict['BANKNAME'])
    bank_name = response_dict['BANKNAME']
    order_id = response_dict['ORDERID']
    transaction_id = response_dict['TXNID']
    gateway = response_dict['GATEWAYNAME']
    context ={

        'order_id' :order_id,
        'bank_name' : bank_name,
        'transaction_id' : transaction_id,
        'gateway' : gateway,
        'amount' : response_dict['TXNAMOUNT']
    }
    return render(request, 'GymPages/paymentstatus.html', {'response': response_dict,'context':context})


#Transformation plans

def Transformation(request):

    data = transformation.objects.all()
    context={
        'data':data
    }
    return render(request,'GymPages/transformational.html',context)