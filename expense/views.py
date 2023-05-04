from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
import json
from expense.models import Features
from django.views.decorators.csrf import csrf_exempt
from validate_email import validate_email
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from .utils import account_activation_token
from django.urls import reverse
from django.contrib import auth


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "POST":
        data = json.loads(request.body)
        firstname = data['firstname']
       
        if not str(firstname).isalpha():
            return JsonResponse({ "user_error": "type error"}, status=409)
            
        else:
            return JsonResponse({"user": True})
    
        


    return render(request, "expense/index.html" )
@csrf_exempt
def second(request):
    if request.method == 'POST':
        data2 = json.loads(request.body)
        surname = data2['surname']

        if not str(surname).isalpha():
            return JsonResponse({'user_error': 'only alphabets'}, status=409)
       
        else:
          return JsonResponse({'user': True})
    

def post(request):
        if request.method == 'POST':
            data3 = json.loads(request.body)
            email = data3['email']
            if not validate_email(email):
                return JsonResponse({'email_error': 'Email is invalid'}, status=400)
            
            return JsonResponse({'email_valid': True})
@csrf_exempt        
def passw(request):
        if request.method == 'POST':
            data4 = json.loads(request.body)
            password = data4['password']
            if len(password) <= 8:
                return JsonResponse({'password_error': 'password must contain more than eight characters'}, status=400)
            
            return JsonResponse({'password': True})
        
def postin(request):
        # GET USER DATA
        # VALIDATE
        # create a user account
        if request.method == 'POST':

            firstname = request.POST['firstname']
            surname = request.POST['surname']
            email = request.POST['email']
            password = request.POST['password']

            context = {
                'fieldValues': request.POST
            }

            if not User.objects.filter(surname=surname).exists():
                if not User.objects.filter(email=email).exists():
                    if len(password) < 6:
                        messages.info(request, 'Password too short')
                        return render(request, 'expense/index.html', context)

                    user = User.objects.create_user(firstname=firstname, surname=surname, password=password, email=email)
                    user.is_active = False
                    user.save()
                    current_site = get_current_site(request)
                    email_body = {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': account_activation_token.make_token(user),
                    }

                    link = reverse('activate', kwargs={
                                'uidb64': email_body['uid'], 'token': email_body['token']})

                    email_subject = 'Activate your account'

                    activate_url = 'http://'+current_site.domain+link

                    email = EmailMessage(
                        email_subject,
                        'Hi '+user.surname + ', Please the link below to activate your account \n'+activate_url,
                        'noreply@semycolon.com',
                        [email],
                    )
                    email.send(fail_silently=False)
                    messages.success(request, 'Account successfully created')
                    return render(request, 'expense/register.html')

            return render(request, 'expense/register.html')



def tokin(request, uidb64, token):
    try:
        id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=id)

        if not account_activation_token.check_token(user, token):
            return redirect('login'+'?message='+'User already activated')

        if user.is_active:
            return redirect('login')
        user.is_active = True
        user.save()

        messages.info(request, 'Account activated successfully')
        return redirect('login')

    except Exception as ex:
        pass

    return redirect('login')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.info(request, 'Welcome, ' +
                                        user.username+' you are now logged in')
                    return redirect('main')
                messages.info(
                    request, 'Account is not active,please check your email')
                return render(request, 'expense/login.html')
            messages.info(
                request, 'Invalid credentials,try again')
            return render(request, 'expense/login.html')

        messages.info(
            request, 'Please fill all fields')
        return render(request, 'expense/login.html')
    return render(request, 'expenses/login.html')



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.info(request, 'You have been logged out')
        return redirect('login')



    












        


