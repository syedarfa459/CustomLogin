from django.shortcuts import render,redirect
from .models import UserLogin
from .forms import UserLoginForm
from django.contrib.auth import logout,authenticate
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def loginView(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        pwd = request.POST.get('pass')
    

        user_records = UserLogin.objects.all()
        for user in user_records:
            # u_pass = check_password(user.password)
            if user.email == email:
                u_pass = check_password(pwd,user.password)
                if u_pass == True:
                    return render(request, 'user_login_app/success.html', context={'user_email':user.email})


        # for user in user_records:
        #     print("Ye dekho ",user.password)
        #     if user.email == email and user.password == pwd:
        #         print('done')
        #         return render(request, 'user_login_app/success.html', context={'user_email':user.email})

    return render(request, 'user_login_app/index.html')

def logoutView(request):

    logout(request)
    return redirect('/')

def registerView(request):

    if request.method == 'POST':
        fm = UserLoginForm(request.POST)
        if fm.is_valid():
            # if u want encrypted password uncomment the lines
            fm = fm.save(commit=False)
            pwd = fm.password
            fm.password = make_password(pwd)
            fm.save()
    else:
        fm = UserLoginForm()

    return render(request,'user_login_app/register.html', context={'fm':fm})