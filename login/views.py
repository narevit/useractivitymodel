from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import Login
import random,string,json
from passlib.hash import bcrypt_sha256
from useractivitymodel.settings import CURRENT_SITE_URL
from django.utils import timezone
from django.conf import settings 
# Create your views here.
from django.utils.timezone import get_current_timezone
from cryptography.fernet import Fernet

def register(request):
    return render(request, 'register.html', {"CURRENT_SITE_URL":CURRENT_SITE_URL})


def registersuccess(request):
    context = {}

    if (request.method == 'POST'):
        
        context['error'] = False
        name = request.POST['name']
        useremail = request.POST['email']
        password = request.POST['password']
        tz = request.POST['tz']
        User_email_count = Login.objects.filter( useremail = useremail ).count()
        if User_email_count == 1:
            context['error'] = True
            context['errorMsg'] = "This email is already registered with us."
        # try:
        date_now = timezone.now()

        # create entry for register new users
        encrypt_pswd = bcrypt_sha256.using(rounds=12).hash(password)
        userid = ''.join(random.choices(string.ascii_lowercase, k=10))
        userauth = Login(randomkey=userid,name=name , useremail=useremail, password=encrypt_pswd,createdon = date_now,loginattempts=0 )
        userauth.save()
        storeuserdata = {
            "id": userid,
            "real_name": name,
            "tz": tz,
            "activity_periods":[]
        }
        with open("useractivitydata.json", 'r+') as f:
            json_get = json.load(f)
            print("sss",storeuserdata)
            json_get['members'].append(storeuserdata)
            # update json here
            f.seek(0)
            f.truncate()
            json.dump(json_get, f)

        # except Exception as e:
        #     print(repr(e))
        #     context['error'] = True
        #     context['errorMsg'] = "Something went wrong.Please try again later."

        return JsonResponse(context)


def login(request):
    return render(request, 'login.html', {"CURRENT_SITE_URL":CURRENT_SITE_URL})

FERNET_KEY = 'H-gvBa89So7ZUjtvYeY7q5xYPIytGnLOLcBpRbASyao='

def loginsuccess(request):
    email = request.POST['email']
    password = request.POST['password']
    context = {}
    try:
        name,userid, saltedpswd = Login.objects.values_list('name','randomkey','password').get(useremail = email)
        if bcrypt_sha256.verify(password, saltedpswd):
            request.session['start_time'] = timezone.now().strftime("%b %d %Y  %I:%M %p")
            request.session['name'] = name
            request.session['userid'] = userid
            context['error'] = False
        else:
            context['error'] = True
            context['msg'] = "Invalid email or password"
    except Exception as e:
        print(repr(e))
        context['error'] = True
        context['msg'] = "Invalid email or password"

    return JsonResponse(context)

def dashboard(request):
    return render(request, 'userdashboard.html') 

def logout(request):
    userid = request.session['userid']
    with open("useractivitydata.json", 'r+') as f:
        json_get = json.load(f)
        
        for data in json_get["members"]:
            if data['id'] == userid:
                activity = {
                    "start_time": request.session['start_time'],
					"end_time": timezone.now().strftime("%b %d %Y  %I:%M %p")
                }
                data['activity_periods'].append(activity)
        # update json here
        f.seek(0)
        f.truncate()
        json.dump(json_get, f)

    del request.session['userid']
    del request.session['name']
    del request.session['start_time']
    return HttpResponseRedirect(reverse('login:login'))