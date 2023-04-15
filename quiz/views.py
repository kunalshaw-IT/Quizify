from django.shortcuts import render, redirect
from quiz.models import questions, player
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return redirect('/login_home')   
    else:
        return render(request,"home.html")

        
    

def login_home(request):
    return render(request,'login_home.html')

def question(request):
    return render(request,'questions.html')


def leaderboard(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        players=player.objects.all()
        context={'players':players}
        return render(request,"leaderboard.html",context)
    else:
        return redirect('/')



def thankyou(request,score):
    context={'score':score}
    players = player.objects.get(username=request.user)
    players.points=score
    players.save()
    return render(request,"thankyou.html",context)



def loginUser(request):
    if request.method=="POST":
        username =request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            messages.error(request, 'Login successfull')
            return redirect("/")
        else:
            # No backend authenticated the credentials
            messages.error(request, 'Login unsuccessfull')
            
    return render(request, 'login.html')


def signupUser(request):
    if request.method=="POST":
        username =request.POST.get('username')
        password=request.POST.get('password')
        rpassword=request.POST.get('rpassword')
        if(password==rpassword):
            user = User.objects.create_user(username,'',password)
            players = player(username=username,points='5')
            players.save()
            return redirect('/login')
        else:
            messages.error(request, 'Password does not matched')
    return render(request, 'signup.html')

def logoutUser(request):
    logout(request)
    return redirect("/")

