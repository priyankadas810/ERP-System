from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from .models import user_register, admin_register, user_notifications, membership
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
import math
import random
import smtplib
import qrcode
import qrcode.image.svg
from io import BytesIO
from datetime import datetime
from rest_framework.renderers import JSONRenderer
import logging
logger = logging.getLogger('idento')

# Create your views here.


def send_otp(email):
    digits="0123456789"
    OTP=""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    otp = OTP + " is your OTP"
    msg= otp
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('daspriyank000@gmail.com', 'rrdvendfboltlmov')
    s.sendmail('daspriyank000@gmail.com',email, msg)
    return OTP


@login_required(login_url='login')  
def qr_generator(request):
    users = user_register.objects.get(user = request.user)
    print(users)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    factory = qrcode.image.svg.SvgImage
    qr_string = { "name": users.name,
                 "username": users.username,
                 "email": users.email,
                 "contact": users.contact,
                 "gender": users.gender,
                 "time": dt_string
                 }
    img = qrcode.make(qr_string, image_factory=factory, box_size=10)
    stream = BytesIO()
    img.save(stream)
    context = {
    'qrcode': stream.getvalue().decode()
    }

    
    return render(request, "User/qr_generator.html", context)

@login_required(login_url='login')  
def user_info(request):
    return render(request, "User/user_info.html")



@login_required(login_url='login')  
def user_profile(request):
    return render(request, "User/user_profile.html")


@login_required(login_url='login')           
def user_home(request):
    retrieve_user = user_register.objects.all()
    print(retrieve_user)
    # if user_notifications.objects.get():
    #     pass

    return render(request, "User/user_home.html", {'retrieve_user': retrieve_user})

@login_required(login_url='login')           
def admin_home(request):
    

    return render(request, "Admin/admin_home.html")


def index(request):
    
    return render(request, "main.html")

@login_required(login_url='login') 
def admin_info(request):

    display_admin = admin_register.objects.get(user = request.user)
    display_users = user_register.objects.filter(name_of_org = display_admin)
    user_count = display_users.count()
    print(display_admin)
    return render(request, "Admin/admin_info.html", {'retrieve_info': display_users, 'count_no':user_count})

@login_required(login_url='login') 
def admin_profile(request):
    retrieve_admin = admin_register.objects.filter(user = request.user)
    print(retrieve_admin)
    return render(request, "Admin/admin_profile.html", {'retrieve_admin': retrieve_admin})


def userRegistration(request):
    data = admin_register.objects.all().order_by('name_of_org')     #picking from admin to display name of organisation
    if request.method == 'POST':
        postData = request.POST
        name = postData.get('name')
        gender = postData.get('gender')
        username = postData.get('username')
        email  = postData.get('email')
        password1 = postData.get('psw')
        password2 = postData.get('psw-repeat')
        name_of_org = postData.get('org')
        date_of_birth = postData.get('dob')
        contact = postData.get('contact')
        
        print(name_of_org)
        
        member_id = random.randint(111111,999999)
        print(member_id)
        
        if user_register.objects.filter(member_id = member_id).exists():
            member_id = random.randint(111111,999999)
            print(member_id)

        print(user_register.objects.all().values())
        org = admin_register.objects.filter(name_of_org = name_of_org)[0]

        if password1 == password2:
            if User.objects.filter(username=username).exists():

                    print("first")
                    if  User.objects.filter(username=username, email = email).exists() and admin_register.objects.filter(username=username, email = email).exists():
                        print("second")
                        #admin_check = admin_register.objects.get(username = username)
                        if user_register.objects.get(username=username, email = email).verify == False : #if user has not put verified otp  
                            User.objects.filter(email = email).delete() #then delete it so that it can get created again
                            print("heloo its done")
                            OTP = send_otp(email)
                            # user = User.objects.create_user(username = username,email= email, password= password1)
                            # register2 = admin_register(otp = OTP, name_of_org= name_of_org,year_of_foundation= year_of_foundation, contact_number= contact_number,username=username, email=email, user=user)
                            # register2.save()
                            new_regg = user_register.objects.filter(username = username).first()
                            new_regg.otp = OTP
                            new_regg.save()
                            new_regg = user_register.objects.filter(username = username).first()
                            
                            return redirect(f'/user_otp/{ new_regg.uid}')
                        else:    
                            messages.error(request,"Username already exists")
                            return render(request, "User/user_register.html")
                    else:    
                        messages.error(request,"Username already exists")
                        return render(request, "User/user_register.html")

            if  User.objects.filter(email = email).exists() :
                print("first")
                if  User.objects.filter(username=username, email = email).exists():
                    print("second")
                #admin_check = admin_register.objects.get(username = username)
                    if user_register.objects.get(username=username, email = email).verify == False : #if user has not put verified otp  
                        User.objects.filter(email = email).delete() #then delete it so that it can get created again
                        print("heloo its done")
                        OTP = send_otp(email)
                        # user = User.objects.create_user(username = username,email= email, password= password1)
                        # register2 = admin_register(otp = OTP, name_of_org= name_of_org,year_of_foundation= year_of_foundation, contact_number= contact_number,username=username, email=email, user=user)
                        # register2.save()
                        new_regg = user_register.objects.filter(username = username).first()
                        new_regg.otp = OTP
                        new_regg.save()
                        new_regg = user_register.objects.filter(username = username).first()
                    
                        return redirect(f'/user_otp/{ new_regg.uid }')
                    else:    
                        messages.error(request,"Email already exists")

                    return render(request, "User/user_register.html")
                else:    
                    messages.error(request,"Email already exists")
                    return render(request, "User/user_register.html")
            
            else:  
                OTP = send_otp(email)
                user = User.objects.create_user(username = username,email= email, password= password1)
                print(user)
                register1 = user_register(otp = OTP, name= name, gender=gender, username=username, email=email, contact = contact, date_of_birth = date_of_birth,user=user, name_of_org= org, member_id= member_id)
                register1.save()
                print(register1)
                new_regg = user_register.objects.filter(username = username).first()
                
                return redirect(f'/user_otp/{ new_regg.uid}')
            
        else:
            messages.error(request,"Password does not match")
            return render(request,"User/user_register.html")
      
    return render(request,"User/user_register.html", {'data': data})



                    




            # if password1 == password2:
            #     if User.objects.filter(username=username).exists(): 
            #         org = user_register.objects.get(username = username) #adding instance from admin_register
            #         if User.objects.filter(email = email).exists() and org.verify == False : #if user has not put verified otp  
            #             User.objects.filter(email = email).delete() #then delete it so that it can get created again
            #             print("heloo its done")
            #             OTP = send_otp(email)
            #             user = User.objects.create_user(username = username,email= email, password= password1)
            #             register1 = user_register(otp = OTP, name= name, gender=gender, username=username, email=email,user=user, name_of_org= org)
            #             register1.save()
            #             new_reg = user_register.objects.filter(username = username).first()
                    
            #             return redirect(f'/user_otp/{ new_reg.id}')
            #         messages.error(request,"Username already exists")
            #         return render(request, "User/user_register.html")


            #     else:   
            #         OTP = send_otp(email)
            #         user = User.objects.create_user(username = username,email= email, password= password1)
            #         register1 = user_register(otp = OTP, name= name, gender=gender, username=username, email=email,user=user, name_of_org= org)
            #         register1.save()
            #         new_reg = user_register.objects.filter(username = username).first()
                    
            #         return redirect(f'/user_otp/{ new_reg.ID}')
                
            # else:
            #     messages.error(request,"Password does not match")
            #     return render(request,"User/user_register.html")
            
        
            
def user_otp(request, id):
    #if request.method == 'POST':
    if 'submit' in request.POST:
        postData = request.POST
        otp = postData.get('sendotp')
        print(otp)
        value= user_register.objects.get(uid=id) 
        print(value.otp)
        if otp == str(value.otp):
            print("verified")
            value.verify = True
            value.save() 
            return redirect('user_signin')        
        else:
            print("Incorrect otp")            
        return redirect(f'/user_otp/{id}') 
    elif 'resend' in request.POST:
        value= user_register.objects.get(uid=id) 
        OTP = send_otp(str(value.email))
        value.otp = OTP
        value.save()
        return redirect(f'/user_otp/{id}')
    return render(request,"otp.html")

def admin_otp(request, id):
    #if request.method == 'POST':
    if 'submit' in request.POST:
        postData = request.POST
        otp = postData.get('sendotp')
        print(otp)
        value= admin_register.objects.get(id=id) 
        #value = user_register.objects.get(id=ID) #first id is from models second id is the value UUID
        print(value.otp)
        if otp == str(value.otp):
            print("verified")
            value.verify = True
            value.save() 
            return redirect('admin_signin')        
        else:
            print("Incorrect otp")            
        return redirect(f'/admin_otp/{id}') 
    elif 'resend' in request.POST:
        value= admin_register.objects.get(id=id) 
        OTP = send_otp(str(value.email))
        value.otp = OTP
        value.save()
        return redirect(f'/admin_otp/{id}')
    return render(request,"otp.html")    


def adminRegistration(request):
     
        if request.method == 'POST':
            postData = request.POST
            name_of_org = postData.get('nameoforganization')
            year_of_foundation = postData.get('foundationyear')
            contact_number = postData.get('contact')
            username = postData.get('username')
            email  = postData.get('email')
            password1 = postData.get('psw')
            password2 = postData.get('psw-repeat')
            print("Name of user", username) #retrieving the query object with username=value from models 
             
            
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    print("first")
                    if  User.objects.filter(username=username, email = email).exists() and admin_register.objects.filter(username=username, email = email).exists():
                        print("second")
                    #admin_check = admin_register.objects.get(username = username)
                        if admin_register.objects.get(username=username, email = email).verify == False : #if user has not put verified otp  
                            User.objects.filter(email = email).delete() #then delete it so that it can get created again
                            print("heloo its done")
                            OTP = send_otp(email)
                            # user = User.objects.create_user(username = username,email= email, password= password1)
                            # register2 = admin_register(otp = OTP, name_of_org= name_of_org,year_of_foundation= year_of_foundation, contact_number= contact_number,username=username, email=email, user=user)
                            # register2.save()
                            new_reg = admin_register.objects.filter(username = username).first()
                            new_reg.otp = OTP
                            new_reg.save()
                            new_reg = admin_register.objects.filter(username = username).first()
                        
                            return redirect(f'/admin_otp/{ new_reg.id}')
                        else:    
                            messages.error(request,"Username already exists")
                            return render(request, "Admin/admin_register.html")
                    else:    
                        messages.error(request,"Username already exists")
                        return render(request, "Admin/admin_register.html")

                if  User.objects.filter(email = email).exists() :
                    print("first")
                    if  User.objects.filter(username=username, email = email).exists():
                        print("second")
                    #admin_check = admin_register.objects.get(username = username)
                        if admin_register.objects.get(username=username, email = email).verify == False : #if user has not put verified otp  
                            User.objects.filter(email = email).delete() #then delete it so that it can get created again
                            print("heloo its done")
                            OTP = send_otp(email)
                            # user = User.objects.create_user(username = username,email= email, password= password1)
                            # register2 = admin_register(otp = OTP, name_of_org= name_of_org,year_of_foundation= year_of_foundation, contact_number= contact_number,username=username, email=email, user=user)
                            # register2.save()
                            new_reg = admin_register.objects.filter(username = username).first()
                            new_reg.otp = OTP
                            new_reg.save()
                            new_reg = admin_register.objects.filter(username = username).first()
                        
                            return redirect(f'/admin_otp/{ new_reg.id}')
                        else:    
                            messages.error(request,"Email already exists")

                        return render(request, "Admin/admin_register.html")
                    else:    
                        messages.error(request,"Email already exists")
                        return render(request, "Admin/admin_register.html")
                  
                else:  
                    OTP = send_otp(email)
                    user = User.objects.create_user(username = username,email= email, password= password1)
                    register2 = admin_register(otp = OTP, name_of_org= name_of_org,year_of_foundation= year_of_foundation, contact_number= contact_number,username=username, email=email, user=user)
                    register2.save()
                    new_reg = admin_register.objects.filter(username = username).first()
                    
                    return redirect(f'/admin_otp/{ new_reg.id}')
                
            else:
                messages.error(request,"Password does not match")
                return render(request,"Admin/admin_register.html")
            
        return render(request,"Admin/admin_register.html")

def user_signin(request):
    if request.method == 'POST':
        postData = request.POST
        username = postData.get('username')
        password1 = postData.get('psw')
        user = authenticate(username= username, password= password1) 
        print(username)  
        print(password1)
        print(user)              
        if user is not None:
            login(request, user)
            
            logger.info(f'User has successfully logged in with username: {username}') 
            return redirect('user_home')    #enters into dashboard page             
        else:
            logger.info(f'User login failed with username: {username}') 
            messages.error(request,"Invalid username or password!")
            return render(request, "User/user_signin.html") 
    else:
             
        #logger.info(f'###################################### sign in')
        return render(request, "User/user_signin.html")

def admin_signin(request):
    if request.method == 'POST':
        postData = request.POST
        username = postData.get('username')
        password1 = postData.get('psw')
        user = authenticate(username= username, password= password1) 
        print(username)  
        print(password1)
        print(user)              
        if user is not None:
            login(request, user)
            messages.success(request," You have logged in successfully")
            return redirect('admin_home')    #enters into dashboard page             
        else:
            messages.error(request,"Invalid username or password!")
            return render(request, "Admin/admin_signin.html") 
    else:
              
        return render(request, "Admin/admin_signin.html")        

def signout(request):
    logout(request)
    return redirect('index')

   #check for validity

    #     if (not name):
    #         messages.error(request,"Required name")
    #     elif len(name)<= 4:
    #         messages.error(request,"Name should be greater than equal to 10")
    #     elif not email:
    #         messages.error(request,"Required email") 
    #     elif len(email)<6:
    #         messages.error(request,"Required email length more than 6")    
    #     elif (not password1):   
    #         messages.error(request,"Required first password") 
    #     elif (not password2):   
    #         messages.error(request,"Required second password") 
    #     elif  password1!= password2:   
    #         messages.error("Entered password does not matches")   
    #     elif User.objects.filter(name = self.cleaned_data['name'], email = self.cleaned_data ['email']).exists:
    #         messages.error(request,"Already exists")
    #    # check if previously registered with same creds or not
       
    #     if not messages:
    #         register = userRegistration(name, email, password1, password2)
    #         register.save()
        
    #     return render('login', register)

def membership_details(request):
    if request.method == 'POST':
        postData = request.POST
        membership_type = postData.get('membership_type')
        description = postData.get('description')
        original_price = postData.get('original_price')
        discount_percentage = postData.get('discount_percentage')
        discounted_price = postData.get('discounted_price')
        

        show_op = admin_register.objects.filter(user = request.user).first()
        org = show_op.name_of_org
        print(org, "this is org name attached")
        
        count = False
        if membership.objects.filter(name_of_org = org, membership_type = membership_type).exists:
            print(f"This data for membership type:{membership_type} is already exists please move to upgrade section to upgrade the existing memberships")
            count = True
            # if count == 0:
            #     count = 1
            #     print("membership slready exists re- enter details for upgradation")
            # else:
            #     membership.objects.filter(name_of_org = org, membership_type = membership_type).update(membership_type = membership_type, description = description, original_price= original_price, discount_percentage = discount_percentage, discounted_price = discounted_price, name_of_org = org )
            
        else:
            
            membership.objects.create(membership_type = membership_type, description = description, original_price= original_price, discount_percentage = discount_percentage, discounted_price = discounted_price, name_of_org = org  )
            #return render(request, "Admin/membership_details.html")
        return render(request, "Admin/membership_details.html", {'count': count})
    

    return render(request, "Admin/membership_details.html")

def show_memberships_user(request):
    retrieve_data = user_register.objects.get(user = request.user)
    print(retrieve_data)
    get_value = membership.objects.filter(name_of_org = retrieve_data.name_of_org)
    print(get_value)
    
    return render(request, "User/user_memberships.html", {'get_value': get_value})

def membership_upgrade(request):  

    return render(request, "Admin/membership_upgrade.html"  )

   
           
        
