from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Todo
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def app(request):
    context = {}
    all_todo = Todo.objects.filter(user=request.user).order_by('-timestamp')
    if all_todo:
        context = {
            'all_todo': all_todo,
        }
    return render(request, 'app.html', context)


@login_required(login_url='/login')
def add_todo(request):
    user = request.user
    item = request.POST.get('item')
    if item is not None and item is not '':
        Todo.objects.create(user=user, item=item)
    return redirect('app:app')


@login_required(login_url='/login')
def delete_todo(request, todo_id):
    Todo.objects.get(user=request.user, id=todo_id).delete()
    return redirect('app:app')


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('app:login')
    return render(request, 'register.html')


@login_required(login_url='/login')
def profile(request):
    return render(request, 'profile.html')


def user_log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('app:app')
        else:
            context = {
                'message': "Didn't match with any user we have",
            }
            return render(request, 'login.html', context)
    context = {}

    return render(request, 'login.html', context)


def user_log_out(request):
    logout(request)
    return redirect('app:app')
