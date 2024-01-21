from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, UserEvent
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import RegForm, LoginForm, EventForm, UserPForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User


def post_event(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user  # Assign the User instance to the foreign key field
            event.save()
            return render(request, 'add_event.html', {'msg': 'Event added successfully'})
        else:
            print("not valid", form.errors.as_data())
            return render(request, 'add_event.html', {'msg': 'Form invalid', 'form': form})
    context = {'form': form}
    return render(request, 'add_event.html', context)

# Create your views here.


def home(request):
    return render(request, 'home.html')


def register(request):
    print("here")
    if request.method == 'POST':
        form = RegForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {'msg': 'Registration Successful'})
        else:
            return render(request, 'home.html', {'error': form.errors.items})
    else:
        form = RegForm()
    context = {'form': form}
    print("gaga")
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        # print(form)
        if form.is_valid():
            auth_login(request, form.get_user())
            return render(request, 'home.html', {'msg': 'Login Successful'})
        else:
            print(form.errors.as_data())
            return render(request, 'home.html', {'msg': form.errors.as_data()})
    else:
        form = LoginForm()
    print("enter")
    context = {'form': form}
    return render(request, 'login.html', context)


def logout(request):
    auth_logout(request)
    return render(request, 'home.html')


def dashboard(request):
    user_events = UserEvent.objects.filter(user=request.user)

    context = {
        'user_events': user_events,
    }

    return render(request, 'dashboard.html', context)


def post_event(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user  # Assign the User instance to the foreign key field
            event.save()
            return render(request, 'add_event.html', {'msg': 'Event added successfully'})
        else:
            print("not valid", form.errors.as_data())
            return render(request, 'add_event.html', {'msg': 'Form invalid', 'form': form})
    context = {'form': form}
    return render(request, 'add_event.html', context)


def get_event(request):
    event_data = Event.objects.all().order_by('event_date', 'event_time')
    print(event_data)
    main = {'event': event_data, }
    return render(request, 'event.html', main)


def details(request, id):
    event_set = Event.objects.filter(id=id)
    context = {'event_set': event_set}
    return render(request, 'details.html', context)


def add_dashboard(request, name, id):
    event = get_object_or_404(Event, id=id, event_name=name)
    if UserEvent.objects.filter(user=request.user, event=event).exists():
        # Event already exists in the user's dashboard, handle the case as desired
        return render(request, 'details.html', {'event_exists': True})
    user_event = UserEvent(user=request.user, event=event)
    user_event.save()

    # Fetch the updated events for the dashboard
    user_events = UserEvent.objects.filter(user=request.user)

    context = {
        'user_events': user_events,
    }

    return render(request, 'dashboard.html', context)


def del_dashboard(request, user_id, event_id, user_event_id):
    event_set = UserEvent.objects.filter(
        event_id=event_id, user_id=user_id, id=user_event_id)
    if (event_set.count() == 0):
        print("yes")
        return render(request, 'dashboard.html', {'msg': 'not available for deletion'})
    print(event_set)
    event_set.delete()
    return render(request, 'dashboard.html', {'msg': 'deleted successfully'})


def add_userdetails(request):
    if request.method == 'POST':
        form = UserPForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                prj = form.save(commit=False)
                prj.user = request.user
                prj.save()
                return redirect('dashboard')
            else:
                return render(request, 'dashboard.html', {'msg': 'User not authenticated'})
        else:
            return render(request, 'dashboard.html', {'msg': 'Form invalid', 'form': form})
    else:
        form = UserPForm()
        return render(request, 'update_profile.html', {'form': form})


def mod_event(request):
    event_data = Event.objects.all().order_by('event_date', 'event_time')
    print(event_data)
    main = {'event': event_data, }
    return render(request, 'mod_event.html', main)


def del_event(request, name, id):
    event_set = Event.objects.filter(
        id=id, event_name=name)
    if (event_set.count() == 0):
        print("yes")
        return render(request, 'mod_event.html', {'msg': 'not available for deletion'})
    print(event_set)
    event_set.delete()
    return render(request, 'mod_event.html', {'msg': 'deleted successfully'})


def upd_event(request, name, id):
    event = get_object_or_404(Event, event_name=name, id=id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return render(request, 'mod_event.html', {'msg': 'updated successfully'})
    else:
        form = EventForm(instance=event)

    context = {
        'form': form,
        'event': event,
    }
    return render(request, 'update_event.html', context)
