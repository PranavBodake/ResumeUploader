from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateResumeForm, UpdateResumeForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Resume

from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'webapp/index.html')


def register(request):
    
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Account created successfully!")

            return redirect("login")

    context = {'form':form}

    return render(request, 'webapp/register.html',  context=context)


def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data = request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                auth.login(request, user)

                messages.success(request, "You have Logged In")

                return redirect("dashboard")

    context = {'form':form}

    return render(request, 'webapp/login.html', context = context)     


@login_required(login_url='login')
def dashboard(request):

    # my_resume = Resume.objects.all()

    # context = {'resume' : my_resume}

    # return render(request, 'webapp/dashboard.html', context=context)

    if request.user.is_authenticated:
        user = request.user
        form = CreateResumeForm()
        resumes = Resume.objects.filter(user = user)
        context = {'form':form, 'resumes':resumes}
        return render(request, 'webapp/dashboard.html', context= context)




@login_required(login_url='login')
def create_resume(request):
    # if request.user.is_authenticated:
    #     user = request.user
    #     print(user)
    #     form = CreateResumeForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         resume = form.save(commit=False)
    #         resume.user = user
    #         resume.save()
    #         return redirect("home")
    #     else:
    #         return render(request, 'webapp/create-resume.html',context={'form':form})







    form = CreateResumeForm()

    if request.method == "POST":
        form = CreateResumeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, " Your Resume Uploaded successfully!")

            return redirect("dashboard")
        
    context = {'form':form}

    return render(request, 'webapp/create-resume.html', context=context)




@login_required(login_url='login')
def update_resume(request, pk):
    
    resume = Resume.objects.get(id = pk)

    form = UpdateResumeForm(instance=resume)
    if request.method == 'POST':
        form = UpdateResumeForm(request.POST,request.FILES, instance=resume)

        if form.is_valid():
            form.save()

            messages.success(request, "Your Resume was Updated!")
            return redirect('dashboard')
    
    else:
        form = UpdateResumeForm(instance=resume)
        
    context = {'form': form}

    return render(request, 'webapp/update-resume.html', context=context)

# @login_required(login_url='login')
# def update_resume(request, pk):
#     resume = Resume.objects.get(id=pk)

#     if resume.user == request.user:  # Check if the resume belongs to the logged-in user
#         form = UpdateResumeForm(instance=resume)
#         if request.method == 'POST':
#             form = UpdateResumeForm(request.POST, instance=resume)

#             if form.is_valid():
#                 form.save()
#                 messages.success(request, "Your Resume was Updated!")
#                 return redirect('dashboard')

#         context = {'form': form}
#         return render(request, 'webapp/update-resume.html', context=context)
#     else:
#         return HttpResponse("You are not authorized to update this resume.")



@login_required(login_url='login')
def view_resume(request, pk):
    all_resume = Resume.objects.get(pk = pk)

    context = {'resume':all_resume}

    return render(request, 'webapp/view-resume.html', context=context)


@login_required(login_url='login')
def delete_resume(request, pk):
    resume = Resume.objects.get(id=pk)

    resume.delete()

    messages.success(request, "Bad to see This!")

    return redirect('dashboard')


def logout(request):
    auth.logout(request)

    messages.success(request, "Logged Out! Visit again !!")
    
    return redirect("login")