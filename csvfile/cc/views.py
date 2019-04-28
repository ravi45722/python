from django.shortcuts import render
from django.http import HttpResponse
from .forms import contactform

def contact(request):

    if request.method =='POST':
        form = contactform(request.POST)
        if form.is_valid():
            rollno=form.cleaned_data['rollno']
            name= form.cleaned_data['name']

            print(name,rollno)

    form = contactform()
    return render(request,'form.html',{'form':form})



