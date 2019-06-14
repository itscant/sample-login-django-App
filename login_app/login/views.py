from django.shortcuts import render
from login import  models
from django.shortcuts import redirect
# Create your views here.

def signin(request):

    context = {}
    context['message'] = ''

    if request.method == 'POST':

        user_email = request.POST['email']
        user_password = request.POST['password']

        subscribers = models.User.objects.filter(email__exact=user_email).filter(password__exact=user_password)
        if subscribers.count() == 1:
            return redirect('home')
        else:
            context['message'] = 'You are not registered user, please sign up!'

    else:
        pass

    return render(request, 'login/signin.html/', context)


def signup(request):

    context = {}
    context['message'] = ''

    if request.method == 'POST':

        user_email = request.POST['email']
        user_password = request.POST['password']

        subscribers = models.User.objects.filter(email__exact=user_email).filter(password__exact=user_password)

        if subscribers.count() == 1 :
            context['message'] = 'You are already registered please sign in!'
        else:
            user = models.User(email=user_email, password = user_password)
            user.save()
            context['message'] = 'You are successfully registered now !'
    else:
        pass

    return render(request, 'login/signup.html/', context)


def home(request):
        return render(request, 'login/home.html/', {})
