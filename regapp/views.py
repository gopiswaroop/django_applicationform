from django.shortcuts import render
from regapp.forms import studentform
from regapp.forms import vendorform


# Create your views here.
def homepage(request):
    return render(request, 'index.html')


def logoutuser(request):
    return render(request, logout.html)


def addstudent(request):
    form = studentform
    dict = {'form': form}
    if request.method == 'POST':
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
            return homepage(request)
    return render(request, 'registration.html', dict);


def addvendor(request):
    form = vendorform
    dict = {'form':form}
    if request.method == 'POST':
        form = vendorform(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['contact'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['password1'])
            print(form.cleaned_data['password2'])
        return homepage(request)
    return render(request, 'addvendor.html', dict);
