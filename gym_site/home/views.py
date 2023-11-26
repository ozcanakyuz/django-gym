from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render

from home.forms import LoginForm, SignUpForm
from home.models import ContactFormMessage, UserProfileForm, UserProfile
from product.models import Comment


def index(request):
    #! BMI CALCULATE
    if request.method=='POST':
        weight = int(request.POST["weight"])
        height = int(request.POST["height"])
        bmi = (weight)/((height*height)) * 10000
        print(bmi)
        # if bmi < 18.5:
        #     print("You are weak.")
        # elif 18.5 <= bmi < 25:
        #     normal = 'You are at normal level.'
        # elif bmi > 30:
        #     owerveight = 'You are owerveight.'
        context = {'page': 'Home',
                   'bmi': bmi}
        return render(request, 'index.html', context)
    
    context = {'page': 'Home'}
    return render(request, 'index.html', context)


def about(request):
    context = {'page': 'About'}
    return render(request, 'about.html', context)

def feature(request):
    context = {'page': 'Feature'}
    return render(request, 'feature.html', context)

def classes(request):
    #! BMI CALCULATE
    if request.method=='POST':
        weight = int(request.POST["weightClass"])
        height = int(request.POST["heightClass"])
        bmi = (weight)/((height*height)) * 10000
        print(bmi)
        context = {'page': 'Classes',
                   'bmiClass': bmi}
        return render(request, 'classes.html', context)
    
    context = {'page': 'Classes'}
    return render(request, 'classes.html', context)


def contact(request):
    context = {'page': 'Contact'}
    return render(request, 'contact.html', context)
def blog(request):
    context = {'page': 'Blog',}
    return render(request, 'blog.html', context)

def single(request):
    context = {'page': 'Detail',}
    return render(request, 'single.html', context)

#! LOG IN - LOG OUT & SIGN UP  
def login_view(request):
    if request.method == 'POST':  # check post
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                #? messages.success(request, "Başarılı şekilde oturum açtınız {}".format(user.username))
                return HttpResponseRedirect('/home')
            else:
                messages.warning(request, "Girilen Bilgiler Hatalı Tekrar Deneyiniz {}".format(username))
                return HttpResponseRedirect('/login')

    form = LoginForm
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() #completed sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create data in profile table for user
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="images/users/user.png"
            data.save()
            # messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/signup')

    form = SignUpForm()
    context = {'form': form}
    return render(request, 'signup_form.html', context)

def userProfile_view(request):
    if request.method == 'POST':  # check post
        form = UserProfileForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()  # create relation with model
            data.name = form.cleaned_data['name']  # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            
            data.save()  # save data to table
            messages.success(request, "Your message has been sent. Thank you for your message.")
            return HttpResponseRedirect('/user_profile')

    form = UserProfileForm
    context = {'form': form}
    return render(request, 'userprofile.html', context)




